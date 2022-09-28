
import re
import os
import argparse
from pathlib import Path

import roboyml
from settings import *

parser = argparse.ArgumentParser()
parser.add_argument('teams_dir', type=Path)
args = parser.parse_args()

if not args.teams_dir.is_dir():
    raise ValueError("need a dir of team markdown files")

team_files = list(filter(lambda x: x.name not in ["README.md"] and x.suffix == ".md", args.teams_dir.iterdir()))
team_contents = dict()
for f in team_files:
    with f.open() as file:
        team_contents[f] = file.read()

def teamfile_to_team_name(f: Path):
    return f.stem.replace(" ", "_")

def team_containing_string(s: str):
    r = rf"\b{s}\b"
    #rc = re.compile(r)
    #print(f"Debug regex: {r}")
    for f, c in team_contents.items():
        if re.search(r, c):
            return teamfile_to_team_name(f)
    return None


with roboyml.open(studentfile) as students, roboyml.open(teamfile) as teams:
    for netid, student in students.items():
        if "team" in student:
            del student["team"]
    for team in teams.values():
        team["members"] = set()
    def add_student_to_team(netid, team):
        student = students[netid]
        if type(teams[team]["members"]) != set:
            teams[team]["members"] = set(teams[team]["members"])
        if "team" in student:
            assert student["team"] == team, f"Student {netid}: {student['team']} did not match {team}! {student}"
        student["team"] = team
        teams[team]["members"].add(netid)

    for teamfile in team_files:
        known_team_files = list(map(lambda f: f["filename"] if f else None, teams.values()))
        if teamfile.name not in known_team_files:
            teams[teamfile_to_team_name(teamfile)] = {"filename": teamfile.name, "members": set()}
    for netid, student in students.items():
        # print(f"Finding team for {netid}: {student['firstname']} {student['lastname']} ...")
        if t := team_containing_string(netid):
            add_student_to_team(netid, t)
            continue
        elif t := team_containing_string(student["github"]):
            add_student_to_team(netid, t)
            continue
        elif t := team_containing_string(student["firstname"] + " " + student["lastname"]):
            add_student_to_team(netid, t)
            continue
        else:
            print(f"Did not find team for {netid}: {student['firstname']} {student['lastname']} ...")
