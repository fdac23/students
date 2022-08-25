
from github import Github

from settings import *

gh = Github(os.environ.get("GITHUB_TOKEN"))

class_org = gh.get_organization("fdac22")
class_repo = class_org.get_repo("students")
org_members = list(class_org.get_members())

