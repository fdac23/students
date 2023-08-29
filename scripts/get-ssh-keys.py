
import re
import os
from pathlib import Path

from . import roboyml
from github import Github
from .settings import *
from .gh_settings import *

with roboyml.open(studentfile) as students:
  for netid, student in students.items():
    gh_user = gh.get_user(student["github"])
    gh_keys = list(gh_user.get_keys())
    if "keys" not in student:
      student["keys"] = []
    for k in gh_keys:
      if k.key not in student["keys"]:
        student["keys"].append(k.key)
    for k in student["keys"]:
      if k not in [k.key for k in gh_keys]:
        print(f"### WARN: {netid} (gh {student['github']}) removed key: {k}")
        student["keys"].remove(k)
    if len(gh_keys) == 0:
      print(f"### WARN: {netid} (gh {student['github']}) has no SSH keys on github")

print(f"Ratelimit remains: {gh.rate_limiting}")
