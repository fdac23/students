import os
from pathlib import Path
from datetime import timedelta, datetime
import pytz

teamfile = Path("teams.yml")
studentfile = Path("students.yml")
repofile = Path("repos.yml")

class_timezone = pytz.timezone('America/New_York')
a_week = timedelta(days=7)

md_files = list(Path(".").glob("*.md"))
student_bio_files = list(filter(lambda m: m.stem and not m.stem[0].isupper(), md_files))

if __name__ == "__main__":
    print(f"Bio files:")
    print(student_bio_files)
