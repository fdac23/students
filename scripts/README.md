# Ordering for populating students.yml

```bash
python scripts/netid-github-link.py # makes calls to github api, sets 'github' and creates netids in students.yml
python scripts/student-names-from-bios.py # reads bio markdown files to get 'firstname' 'lastname'
python scripts/assign-docker-ports.py # assigns ports to students for their docker containers
```

# ports.md

Updating the markdown file with data from the yml:

```bash
python scripts/make-ports-md.py > ports.md
```

# SSH keys

Pulls SSH keys from the github api for each student and puts the keys in the students.yml:

```bash
python scripts/get-ssh-keys.py
```
