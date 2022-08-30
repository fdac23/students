
from contextlib import contextmanager
import yaml
from pathlib import Path

def load(file: Path, default = {}):
    with file.open('r') as f:
        data = yaml.safe_load(f)
    if data is None:
        data = default
    return data

def save(file: Path, data):
    with file.open('w') as f:
        yaml.dump(data, f)

@contextmanager
def open(file: Path, readonly = False):
    try:
        if not file.exists() and not readonly:
            file.touch()
        data = load(file)
        yield data
    finally:
        if not readonly:
            save(file, data)
