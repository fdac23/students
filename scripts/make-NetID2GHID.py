
import re
import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

import roboyml
from settings import *

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

template = env.get_template("NetID2GHID.md")

with roboyml.open(studentfile) as students:
  print(template.render(students={
    k: v for k, v in sorted(students.items(), key=lambda t: t[1]["port"])
  }))
