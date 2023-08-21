
import re
import os
from pathlib import Path

from . import roboyml
from .settings import *

# https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
# only game server stuff runs between 7700-7830, so this range should be safe
min_start_port = 7700

with roboyml.open(studentfile) as students:
  next_free_port = lambda: max(students.values(), key=lambda s: s["port"] if "port" in s else min_start_port)["port"] + 1
  print(f"Start assigning ports from {next_free_port()}")
  for netid, student in students.items():
    if "port" not in student:
      new_port = next_free_port()
      student["port"] = new_port

