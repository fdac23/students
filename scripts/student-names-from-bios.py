
import re
import os
from pathlib import Path

from . import roboyml
from .settings import *

find_name_re = r"^ *((Hi|Hey)!?,? |Hello[\., ]?(there)?,? ?)?(I'm |I am |[Mm]y name is )(?P<firstname>(([A-Z]\w+)[ ]?)+?)[ ](?P<lastname>[A-Z][\w\-]+)"

with roboyml.open(studentfile) as students:
  for netid, student in students.items():
    bio = Path(f"{netid}.md")
    if not bio.exists():
      print(f"ERROR: {netid}.md does not exist")
      continue
    with bio.open('r') as f:
      bio_text = f.read()
    r_m = re.search(find_name_re, bio_text, flags=re.MULTILINE)
    if r_m is None:
        print(f"### ERROR: {netid}.md did not match")
        continue
    firstname = r_m.group('firstname')
    lastname = r_m.group('lastname')
    print(f"{netid}: {firstname} {lastname}")
    students[netid]["firstname"] = firstname
    students[netid]["lastname"] = lastname

