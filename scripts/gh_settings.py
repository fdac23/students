
from github import Github
from dotenv import load_dotenv

from .settings import *

load_dotenv()

gh = Github(os.environ.get("GITHUB_TOKEN"))

class_org = gh.get_organization(os.environ.get("GITHUB_REPOSITORY_OWNER", "fdac23"))
class_repo = class_org.get_repo("students")

if __name__ == "__main__":
    print(f"org: {class_org}")
    print(f"repo: {class_repo}")
