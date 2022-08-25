import os
from pathlib import Path
from datetime import timedelta, datetime
import pytz

from dotenv import load_dotenv
from dateutil.parser import parse as dt_parse

load_dotenv()

teamfile = Path("teams.yml")
studentfile = Path("students.yml")
repofile = Path("repos.yml")

class_timezone = pytz.timezone('America/New_York')
a_week = timedelta(days=7)

md_files = list(Path(".").glob("*.md"))
student_bio_files = list(filter(lambda m: m.stem not in ["FAQ", "ports", "README"], md_files))

if __name__ == "__main__":
    print(f"Bio files:")
    print(student_bio_files)
