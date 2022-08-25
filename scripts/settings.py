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

