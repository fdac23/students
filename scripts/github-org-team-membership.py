
import re
import os
from pathlib import Path

import roboyml
from github import Github
from settings import *
from gh_settings import *

org_members = list(class_org.get_members())
students_team = class_org.get_team_by_slug("students")

with roboyml.open(studentfile) as students:
  for netid, student in students.items():
    gh_user = gh.get_user(student["github"])
    if gh_user not in org_members:
      print(f"Inviting {gh_user} to the students team...")
      class_org.invite_user(user=gh_user, teams=[students_team,])

print(f"Ratelimit: {gh.rate_limiting}")
