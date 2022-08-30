Quick copy-paste in order: (assuming your `python` is 3.6+)

```bash
python scripts/netid-github-link.py
python scripts/student-names-from-bios.py
python scripts/assign-docker-ports.py
python scripts/make-ports-md.py > Ports.md
python scripts/get-ssh-keys.py
# on da2: (remember to commit/push/pull this repo with new changes)
sudo python3 scripts/da2/create-user-home-dirs.py
python3 scripts/da2/create-docker-containers.py
```

# Ordering for populating students.yml

```bash
python scripts/netid-github-link.py # makes calls to github api, sets 'github' and creates netids in students.yml
python scripts/student-names-from-bios.py # reads bio markdown files to get 'firstname' 'lastname'
python scripts/assign-docker-ports.py # assigns ports to students for their docker containers
```

# Ports.md

Updating the markdown file with data from the yml:

```bash
python scripts/make-ports-md.py > Ports.md
```

# SSH keys

Pulls SSH keys from the github api for each student and puts the keys in the students.yml:

```bash
python scripts/get-ssh-keys.py
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

