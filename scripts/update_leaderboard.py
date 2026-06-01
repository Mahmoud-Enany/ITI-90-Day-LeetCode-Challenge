import os
import re

PROBLEM_FOLDER = re.compile(r"^\d{2}-")
SKIP_NAMES = {"readme.md", ".gitkeep"}
SOLUTION_EXTENSIONS = {
    ".c", ".cpp", ".cc", ".cxx", ".py", ".java", ".kt", ".kts", ".scala",
    ".groovy", ".js", ".mjs", ".jsx", ".ts", ".tsx", ".cs", ".fs", ".fsx",
    ".vb", ".go", ".rs", ".zig", ".nim", ".d", ".v", ".swift", ".m", ".mm",
    ".rb", ".php", ".lua", ".pl", ".pm", ".tcl", ".hs", ".ml", ".mli", ".clj",
    ".erl", ".ex", ".exs", ".dart", ".r", ".R", ".jl", ".pas", ".cr", ".coffee",
    ".f90", ".f95", ".adb",
}


def is_solution_file(filename: str) -> bool:
    if filename.startswith(".") or filename.lower() in SKIP_NAMES:
        return False
    _, ext = os.path.splitext(filename)
    return ext.lower() in SOLUTION_EXTENSIONS


def author_from_filename(filename: str) -> str | None:
    """YourName.ext inside a problem folder."""
    stem = os.path.splitext(filename)[0]
    if not stem or "_" in stem:
        return None
    return stem.strip().capitalize()


def author_from_legacy(filename: str) -> tuple[str, str] | None:
    """ProblemName_Author.ext at week root (backward compatible)."""
    stem = os.path.splitext(filename)[0]
    parts = stem.split("_")
    if len(parts) < 2:
        return None
    author = parts[-1].strip().capitalize()
    problem = "_".join(parts[:-1])
    return author, problem


def main():
    # author -> set of (week, problem_id) — one count per problem, not per language
    solved = {}

    week_folders = sorted(
        d for d in os.listdir(".") if os.path.isdir(d) and d.startswith("Week-")
    )

    for week in week_folders:
        week_path = os.path.join(".", week)

        for entry in os.listdir(week_path):
            entry_path = os.path.join(week_path, entry)

            if os.path.isdir(entry_path) and PROBLEM_FOLDER.match(entry):
                for fname in os.listdir(entry_path):
                    if not is_solution_file(fname):
                        continue
                    author = author_from_filename(fname)
                    if not author:
                        continue
                    solved.setdefault(author, set()).add((week, entry))
                continue

            if os.path.isfile(entry_path) and is_solution_file(entry):
                legacy = author_from_legacy(entry)
                if legacy:
                    author, problem = legacy
                    solved.setdefault(author, set()).add((week, problem))

    user_counts = {author: len(problems) for author, problems in solved.items()}
    sorted_users = sorted(user_counts.items(), key=lambda x: x[1], reverse=True)

    table_content = "\n| Rank | ✨ Participant | 📈 Problems Solved | Status |\n"
    table_content += "| :---: | :--- | :---: | :---: |\n"

    for rank, (user, count) in enumerate(sorted_users, 1):
        emoji = "🏆" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else "🔥"
        table_content += f"| {rank} | **{user}** | {count} | {emoji} |\n"

    if not sorted_users:
        table_content += "| - | No solutions merged yet | 0 | 🎯 |\n"

    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print("README.md not found!")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    if "<!-- LEADERBOARD_START -->" not in content or "<!-- LEADERBOARD_END -->" not in content:
        print("Leaderboard markers not found in README.md!")
        return

    pattern = r"(<!-- LEADERBOARD_START -->).*?(<!-- LEADERBOARD_END -->)"
    replacement = f"\\1\n{table_content}\n\\2"
    updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated_content)
    print("Leaderboard successfully updated in README.md!")


if __name__ == "__main__":
    main()
