Quick copy-paste in order: (assuming your `python` is 3.6+)

```bash
# Requires GITHUB_TOKEN to be set:
python -m scripts.github-org-team-membership
python -m scripts.get-ssh-keys
# on da2: (remember to commit/push/pull this repo with new changes)
sudo python3 scripts/da2/create-user-home-dirs.py
python3 scripts/da2/create-docker-containers.py
```

# Setup

Generate a token on github that has permissions to manage orgs, repos, etc.

Place this token in the environment or `.env` file as `GITHUB_TOKEN=xxx`

Run `python -m scripts.gh_settings` to verify the token has more than 60 ratelimit. (Should be a few thousand for a user token)

# Ports.md

This is normally done automatically, but can be run manually:

```bash
python -m scripts.make-ports-md > Ports.md
```

# SSH keys

Pulls SSH keys from the github api for each student and puts the keys in the students.yml:

```bash
python -m scripts.get-ssh-keys
```

# da2 admin actions

Create user dirs and import ssh keys from the yml:

```bash
# REQUIRES ROOT, ONLY RUN ON DA2:
# Ensure you are in the repository directory!
sudo python3 scripts/da2/create-user-home-dirs.py
```

Starting the docker containers should NOT be run with root privs:

```bash
python3 scripts/da2/create-docker-containers.py
```

# Github actions automation

These scripts are now run automatically by github actions, make sure the repo's settings give permissions for the actions runner token.

```bash
# Replace the values with `github_name` and `netid.md` if you want to run this manually:
python -m scripts.pr_actions_handler ${{ github.event.pull_request.user.login }} ${{ steps.changed-files.outputs.netids_all_changed_and_modified_files }}
python -m scripts.student-names-from-bios
python -m scripts.assign-docker-ports && python -m scripts.make-ports-md > Ports.md
```
