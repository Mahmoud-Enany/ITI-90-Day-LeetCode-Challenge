#!/usr/bin/env python3
"""
Auto-update Leaderboard in README.md
Scans all Week-XX folders and counts solutions per contributor.
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent))
from solution_extensions import VALID_EXTENSIONS

BADGES = {
    1:   "🌱 Beginner",
    5:   "⚡ Week Warrior",
    15:  "🔥 On Fire",
    30:  "🧠 Big Brain",
    50:  "🎯 Sharp Shooter",
    90:  "👑 ITI Legend",
}

def get_badge(count):
    badge = "🌱 Beginner"
    for threshold, b in sorted(BADGES.items()):
        if count >= threshold:
            badge = b
    return badge

def extract_author(filepath):
    """Try to extract author from filename: ProblemName_AuthorName.ext"""
    stem = Path(filepath).stem  # e.g. TwoSum_Ahmed
    parts = stem.split('_')
    if len(parts) >= 2:
        return parts[-1]  # Last part after last underscore
    return None

def count_solutions():
    repo_root = Path(__file__).parent.parent
    scores = defaultdict(int)
    problems_solved = defaultdict(set)
    
    for week_dir in sorted(repo_root.glob("Week-*")):
        if not week_dir.is_dir():
            continue
        week_num = week_dir.name
        
        for f in week_dir.iterdir():
            if f.is_file() and f.suffix in VALID_EXTENSIONS and f.name != '.gitkeep':
                author = extract_author(f)
                if author:
                    scores[author] += 1
                    problems_solved[author].add(f"{week_num}/{f.stem.split('_')[0]}")
    
    return scores, problems_solved

def generate_leaderboard_table(scores, problems_solved):
    if not scores:
        return """| Rank | Contributor | Solutions | Badge |
|------|-------------|-----------|-------|
| — | *No solutions yet!* | — | — |

*Be the first to submit a solution!* 🚀"""
    
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    rank_emoji = {1: "🥇", 2: "🥈", 3: "🥉"}
    
    rows = ["| Rank | Contributor | Solutions | Badge |",
            "|------|-------------|-----------|-------|"]
    
    for i, (author, count) in enumerate(sorted_scores[:20], 1):
        rank = rank_emoji.get(i, str(i))
        badge = get_badge(count)
        rows.append(f"| {rank} | {author} | {count} | {badge} |")
    
    if len(sorted_scores) > 20:
        rows.append(f"| ... | *and {len(sorted_scores)-20} more!* | — | — |")
    
    rows.append("")
    rows.append(f"*Total contributors: {len(scores)} | Total solutions: {sum(scores.values())}*")
    
    return "\n".join(rows)

def update_readme(leaderboard_table):
    readme_path = Path(__file__).parent.parent / "README.md"
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace leaderboard section
    pattern = r'(## 🏆 Leaderboard.*?>\s*Updated automatically.*?\n\n).*?(\n---)'
    replacement = f'\\1{leaderboard_table}\n\n\\2'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    if new_content == content:
        print("⚠️  Could not find leaderboard section to update. Check README format.")
    else:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("✅ Leaderboard updated in README.md")

def main():
    print("🔍 Scanning solutions...")
    scores, problems = count_solutions()
    
    print(f"📊 Found {len(scores)} contributors with {sum(scores.values())} total solutions")
    
    for author, count in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        print(f"  {author}: {count} solutions | {get_badge(count)}")
    
    table = generate_leaderboard_table(scores, problems)
    update_readme(table)
    print("🏆 Done!")

if __name__ == "__main__":
    main()
