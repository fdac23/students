
import re
import os
from pathlib import Path

import roboyml
from github import Github
from settings import *
from gh_settings import *

project_team_prefix = "project_"

org_members = list(class_org.get_members())
students_team = class_org.get_team_by_slug("students")
gh_teams = list(class_org.get_teams())
project_teams = {t.name: t for t in filter(lambda t: t.slug.startswith(project_team_prefix), gh_teams)}
org_repos = list(class_org.get_repos())

print(f"Start with {len(project_teams)} project teams...")

with roboyml.open(studentfile) as students, roboyml.open(teamfile) as teams:
  for teamname, team in teams.items():
    if f"{project_team_prefix}{teamname}" not in project_teams:
      print(f"Creating team for {teamname} ...")
      new_team = class_org.create_team(f"{project_team_prefix}{teamname}", privacy="closed")
      project_teams[new_team.name] = new_team
    gh_team = project_teams[f"{project_team_prefix}{teamname}"]
    gh_members = list(gh_team.get_members())
    for netid in team["members"]:
      gh_username = students[netid]["github"]
      if gh_username not in [m.login for m in gh_members]:
        print(f"Adding {gh_username} to {gh_team}")
        gh_team.add_membership(gh.get_user(gh_username), role="maintainer")
    
    # repo creation
    if teamname not in [r.name for r in org_repos]:
      repo = class_org.create_repo(
          teamname,
          description=f"Project repo for team {teamname}",
          private=True,
          has_issues=True,
          has_wiki=True,
          team_id=gh_team.id,
          auto_init=True,
      )
      print(f"Created repo {repo}")
    else:
      repo = next(r for r in org_repos if r.name == teamname)
    gh_team.update_team_repository(repo, "maintain")

print(f"Ratelimit: {gh.rate_limiting}")
