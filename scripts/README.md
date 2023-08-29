Quick copy-paste in order: (assuming your `python` is 3.6+)

```bash
python -m scripts.netid-github-link
python -m scripts.student-names-from-bios
python -m scripts.assign-docker-ports
python -m scripts.make-ports-md > Ports.md
python -m scripts.get-ssh-keys
# on da2: (remember to commit/push/pull this repo with new changes)
sudo python3 scripts/da2/create-user-home-dirs.py
python3 scripts/da2/create-docker-containers.py
```

# Setup

Generate a token on github that has permissions to manage orgs, repos, etc.

Place this token in the environment or `.env` file as `GITHUB_TOKEN=xxx`

Run `python -m scripts.gh_settings` to verify the token has more than 60 ratelimit. (Should be a few thousand for a user token)

# Ordering for populating students.yml

```bash
python -m scripts.netid-github-link # makes calls to github api, sets 'github' and creates netids in students.yml
python -m scripts.student-names-from-bios # reads bio markdown files to get 'firstname' 'lastname'
python -m scripts.assign-docker-ports # assigns ports to students for their docker containers
```

# Ports.md

Updating the markdown file with data from the yml:

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

