
import re
import os
from pathlib import Path

from . import roboyml
from .settings import *

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("github_login")
parser.add_argument("file_changed")
args = parser.parse_args()

with roboyml.open(studentfile) as students:
    netid = Path(args.file_changed).stem.lower()
    if netid not in students:
        students[netid] = {}
    if "github" not in students[netid]:
        students[netid]["github"] = args.github_login

