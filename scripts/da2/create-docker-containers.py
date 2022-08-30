
import re
import os
from pathlib import Path

import docker

import roboyml
from settings import *

client = docker.from_env()

# reference start:
# docker run -i -d --name $n -p $p:22  -v /data:/local -v /home/$n:/home/$n -v /data/shared:/data -w /home/$n audris/jupyter-r:latest /bin/startsvc.sh $n

container_name_fmt = "fdac22_{0}"

running_containers = client.containers.list(all=True)

with roboyml.open(studentfile) as students:
  for netid, student in students.items():
    container_name = container_name_fmt.format(netid)
    if "port" not in student:
      print(f"### ERROR: {netid} has no port assigned, will not create a container for them.")
      continue
    if "container" not in student:
      student["container"] = {}
    if container_name not in [c.name for c in running_containers]:
      print(f"Container {container_name} not found... creating...")
      container = client.containers.run(
          'audris/jupyter-r:latest',
          f"/bin/startsvc.sh {netid}",
          detach=True,
          labels={"io.github.robobenklein.autocreated_name": container_name}, # for later identification
          name=container_name,
          oom_kill_disable=False,
          oom_score_adj=500, # prefer to kill the container instead of something on the host (-1000 to 1000)
          ports={ 22: student["port"] }, # container : host
          stdin_open=True, # the '-i' argument to docker run
          volumes=[
            "/data:/local",
            "/data/shared:/data",
            f"/home/{netid}:/home/{netid}",
          ],
          working_dir=f"/home/{netid}",
      )
    else:
      container = client.containers.get(container_name)

    # container checks:
    if container.status != "running":
      print(f"### WARN: Container {container_name} is not running! It's currently {container.status}.")

    student["container"]["name"] = container_name
    student["container"]["status"] = container.status

