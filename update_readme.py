import os
from pathlib import Path
from datetime import datetime


def get_problem_files(month_folder):
    """Get all .py files from a month folder"""
    problems = []
    if os.path.exists(month_folder):
        for file in Path(month_folder).rglob("*.py"):
            # Extract filename without extension
            problem_name = file.stem
            problems.append(problem_name)
    return problems


def update_readme():
    """Update README.md with current progress"""

    # Base folder structure (adjust if needed)
    base_path = "2026"

    # Get only available months from the 2026 folder
    available_months = []
    if os.path.exists(base_path):
        for item in sorted(os.listdir(base_path)):
            item_path = os.path.join(base_path, item)
            if os.path.isdir(item_path):
                available_months.append(item)

    # Collect data for available months only
    monthly_data = {}
    total_problems = 0

    for month in available_months:
        month_path = os.path.join(base_path, month)
        problems = get_problem_files(month_path)
        monthly_data[month] = problems
        total_problems += len(problems)

    # Generate README content
    readme_content = """# My Coding Discipline

Daily DSA practice in Python | Building consistency and mastering problem-solving patterns

## 2026 Progress

"""

    # Add each month's section
    for month in available_months:
        problems = monthly_data[month]
        count = len(problems)
        problems_str = ", ".join(problems) if problems else ""

        readme_content += f"""### {month}
**Total Problems: {count}**

Problems: {problems_str}

"""

    # Add footer
    current_date = datetime.now().strftime("%Y-%m-%d")
    readme_content += f"""
---

**Total Problems Solved in 2026: {total_problems}**

*Last Updated: {current_date}*"""

    # Write to README.md
    with open("README.md", "w") as f:
        f.write(readme_content)

    print(f"✓ README.md updated successfully!")
    print(f"✓ Total problems tracked: {total_problems}")
    print(f"✓ Active months: {sum(1 for p in monthly_data.values() if p)}")


if __name__ == "__main__":
    update_readme()