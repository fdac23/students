
import re
import os
import shutil
import subprocess
from pathlib import Path

from . import roboyml
from .settings import *

chown_group = "da"

if os.getuid() != 0:
  raise RuntimeError(f"This script needs to be run as root to create user directories.")

with roboyml.open(studentfile, readonly=True) as students:
  for netid, student in students.items():
    def set_file_owner_to_student(path, group=chown_group):
      shutil.chown(path, user=netid, group=group)
    da_home_dir = Path(f"/home/{netid}")
    print(f"Working on {da_home_dir} ...")
    (da_home_dir / ".ssh").mkdir(mode=0o755, parents=True, exist_ok=True)
    set_file_owner_to_student(da_home_dir)
    set_file_owner_to_student(da_home_dir / ".ssh", group=netid)
    (da_home_dir / ".ssh").chmod(0o700)

    # NOTE: unsupported depending on home NFS mount type since move to ishia + tighter security controls
    # set selinux context for their dir:
    #subprocess.check_output(
    #    f"chcon -u system_u -t user_home_t '{da_home_dir}'",
    #    stderr=subprocess.STDOUT,
    #    shell=True
    #)
    #subprocess.check_output(
    #    f"chcon -u system_u -t ssh_home_t '{da_home_dir / '.ssh'}'",
    #    stderr=subprocess.STDOUT,
    #    shell=True
    #)

    # derp: it's readonly since running as root
    # student["homedir"] = da_home_dir

    ssh_authorized_keys = da_home_dir / ".ssh" / "authorized_keys"
    if not len(student["keys"]):
      print(f"### WARN: {netid} has no keys to add, skipping.")
      continue

    if ssh_authorized_keys.exists():
      sak_text = ssh_authorized_keys.read_text()
    else:
      sak_text = "\n"
    keys_to_add = []
    for k in student["keys"]:
      if k not in sak_text:
        keys_to_add.append(k)
    # only write/touch file if we need to modify it:
    if keys_to_add:
      print(f"Need to add {len(keys_to_add)} keys ...")
      # open in append mode:
      with ssh_authorized_keys.open("a+") as sak_file:
        if not sak_text.endswith('\n'):
          sak_file.write("\n")
        sak_file.write(
          f"# Added by robobenklein's class scripts on {datetime.now().strftime('%Y-%m-%d')}:\n"
        )
        for k in keys_to_add:
          sak_file.write(f"{k} # from github account {student['github']}\n")
      set_file_owner_to_student(ssh_authorized_keys, group=netid)
      ssh_authorized_keys.chmod(0o700)
