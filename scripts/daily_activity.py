from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DAILY_DIR = PROJECT_ROOT / "daily"

today = datetime.now()
date_string = today.strftime("%Y-%m-%d")

daily_file = DAILY_DIR / f"{date_string}.md"

DAILY_DIR.mkdir(parents=True, exist_ok=True)

activities = [
    {
        "focus": "Python Automation",
        "challenge": "Create a Python script that automates a repetitive development task.",
        "technologies": "Python, Linux, Git",
        "goal": "Improve Python scripting and automation skills."
    },
    {
        "focus": "Git & GitHub",
        "challenge": "Practice branching, commits, merging, and repository management.",
        "technologies": "Git, GitHub",
        "goal": "Improve professional Git workflow skills."
    },
    {
        "focus": "JavaScript",
        "challenge": "Solve a small JavaScript programming problem.",
        "technologies": "JavaScript, Node.js",
        "goal": "Strengthen JavaScript programming fundamentals."
    },
    {
        "focus": "React",
        "challenge": "Build or improve a small React component.",
        "technologies": "React, JavaScript, Vite",
        "goal": "Improve modern frontend development skills."
    },
    {
        "focus": "Linux",
        "challenge": "Practice Linux commands, shell scripting, or system administration.",
        "technologies": "Linux, Bash",
        "goal": "Improve Linux administration and terminal skills."
    },
    {
        "focus": "Networking",
        "challenge": "Study or practice a networking concept such as DNS, DHCP, TCP/IP, or routing.",
        "technologies": "Linux, Networking",
        "goal": "Strengthen practical networking knowledge."
    },
    {
        "focus": "Project Development",
        "challenge": "Improve an existing project by adding a small feature or documentation.",
        "technologies": "Git, GitHub, Programming",
        "goal": "Make measurable progress on a real development project."
    }
]

# Select an activity based on the day of the year.
day_of_year = today.timetuple().tm_yday
activity = activities[day_of_year % len(activities)]

if daily_file.exists():
    print(f"Daily activity already exists: {daily_file}")
else:
    content = f"""# Daily Developer Activity

**Date:** {date_string}

## Focus

{activity["focus"]}

## Today's Challenge

{activity["challenge"]}

## Technologies

{activity["technologies"]}

## Learning Goal

{activity["goal"]}

## Progress

This daily developer activity was generated automatically
as part of my GitHub development journal.
"""

    daily_file.write_text(content, encoding="utf-8")

    print(f"Created: {daily_file}")
    print(f"Focus: {activity['focus']}")
