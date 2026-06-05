"""
highlight_today.py
Runs daily at midnight Cairo time (21:00 UTC via cron).
Marks the current day's section in the active Week README.
"""

import os
import re
from datetime import date, timedelta

# ── CONFIG ──────────────────────────────────────────────────────────────────
# First day of the challenge (Week 01, Day 1)
START_DATE = date(2026, 5, 28)
DAYS_PER_WEEK = 10
TOTAL_WEEKS = 13

# Marker strings — must stay in sync with the README headings
TODAY_HEADING_SUFFIX = " ⚡ TODAY"
TODAY_BLOCKQUOTE = "> 👇 **This is today's challenge — let's go! 🚀**"
# ────────────────────────────────────────────────────────────────────────────


def compute_today() -> tuple[int, int]:
    """Return (week_number, day_in_week) — both 1-indexed."""
    today = date.today()
    elapsed = (today - START_DATE).days  # 0 on Day 1
    if elapsed < 0:
        raise ValueError(f"Challenge hasn't started yet (starts {START_DATE})")
    week = elapsed // DAYS_PER_WEEK + 1
    day  = elapsed % DAYS_PER_WEEK + 1
    return week, day


def week_readme_path(week: int) -> str:
    return os.path.join(".", f"Week-{week:02d}", "README.md")


def clear_today_markers(content: str) -> str:
    """Remove all existing TODAY markers from a README string."""
    # Remove ⚡ TODAY suffix from any heading
    content = content.replace(TODAY_HEADING_SUFFIX, "")
    # Remove the blockquote line (with optional trailing whitespace)
    content = re.sub(
        r"\n" + re.escape(TODAY_BLOCKQUOTE) + r"[ \t]*",
        "",
        content,
    )
    return content


def add_today_marker(content: str, day: int) -> str:
    """
    Find '### 📅 Day {day}' or '### 🏁 Day {day}' heading and inject marker.
    Returns updated content.
    """
    # Match either emoji variant used in day headings
    pattern = re.compile(
        rf"(### [^\n]+ Day {day}\b[^\n]*)",
        re.UNICODE,
    )
    match = pattern.search(content)
    if not match:
        print(f"  ⚠️  Could not find 'Day {day}' heading in README.")
        return content

    heading = match.group(1).rstrip()
    new_heading = heading + TODAY_HEADING_SUFFIX + "\n" + TODAY_BLOCKQUOTE
    content = content[: match.start()] + new_heading + content[match.end() :]
    return content


def update_week_readme(week: int, day: int) -> None:
    path = week_readme_path(week)
    if not os.path.exists(path):
        print(f"  ❌  {path} not found — skipping.")
        return

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    content = clear_today_markers(content)
    content = add_today_marker(content, day)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  ✅  Updated {path} → Day {day} highlighted.")


def clear_previous_week(week: int) -> None:
    """Clear any lingering TODAY markers from the previous week's README."""
    if week <= 1:
        return
    prev_path = week_readme_path(week - 1)
    if not os.path.exists(prev_path):
        return
    with open(prev_path, "r", encoding="utf-8") as f:
        content = f.read()
    if TODAY_HEADING_SUFFIX not in content and TODAY_BLOCKQUOTE not in content:
        return  # Nothing to clean
    content = clear_today_markers(content)
    with open(prev_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  🧹  Cleared old markers from Week-{week-1:02d}/README.md")


def main() -> None:
    week, day = compute_today()
    print(f"📅  Today → Week {week:02d}, Day {day}  (started {START_DATE})")

    if week > TOTAL_WEEKS:
        print("🏁  Challenge complete — no update needed.")
        return

    clear_previous_week(week)
    update_week_readme(week, day)


if __name__ == "__main__":
    main()
