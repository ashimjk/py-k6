import os
from dataclasses import dataclass
from typing import Optional

import yaml
from dataclasses_json import dataclass_json
from marshmallow import pprint


@dataclass_json
@dataclass
class GitlabCI:
    MAVEN_TEST_SKIP: str = ""
    MAVEN_EXTRA_ARGS: str = ""
    MAVEN_DEPLOY_SKIP: str = ""
    DIR_DOCKER: str = ""
    DIR_CHART: str = ""
    DIR_STACK: str = ""
    DIR_SCAN: str = ""
    DIR_ARTIFACTS: str = ""
    ARTIFACTS_BASH: str = ""
    LOGGING_ARGS: str = ""
    TEMPLATE: str = ""


def user_home(filepath: str) -> str:
    home = os.path.expanduser(filepath)
    return home


# -----------------------------------------------
def load_gitlabci() -> Optional[GitlabCI]:
    filename = '../.gitlab-ci.yml'
    try:
        with open(user_home(filename)) as file:
            data = yaml.safe_load(file)
            proj_dict = data['variables']
            gitlab_ci = GitlabCI.from_dict(proj_dict)
            # for key in proj_dict:
            #     os.environ[key] = proj_dict[key]
            return gitlab_ci
    except Exception as e:
        print(str(e))
        return None


##################################################
if __name__ == "__main__":
    pprint(load_gitlabci().to_dict())
