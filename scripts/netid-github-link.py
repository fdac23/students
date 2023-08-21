
import re
import os
from pathlib import Path

from . import roboyml
from github import Github
from .settings import *
from .gh_settings import *

merged_pulls = list(filter(lambda pull: pull.merged, class_repo.get_pulls(state="closed")))

with roboyml.open(studentfile) as students:
  for pull in merged_pulls:
    gh_user = pull.user
    files_changed = list(pull.get_files())
    if len(files_changed) != 1:
      print(f"ERROR: PR {pull.number} by {gh_user.login} changed more than one file.")
      continue
    filename = files_changed[0].filename
    print(f"PR {pull.number}: {gh_user.login} changed {filename}")
    netid = Path(filename).stem.lower()
    if netid not in students:
      students[netid] = {}
    if "github" not in students[netid]:
      students[netid]["github"] = gh_user.login

print(f"Ratelimit: {gh.rate_limiting}")
