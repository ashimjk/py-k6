import os
from dataclasses import dataclass


@dataclass
class Env:
    auth_url: str
    auth_username: str
    auth_password: str
    api_gateway_url: str


@dataclass
class K6Config:
    report_output_file: str
    page_no: int
    size: int
    file_name: str


def load_env_variable():
    print(os.getenv(f'JAVA_HOME'))
    print(os.getenv('JAVA_HOME'))


if __name__ == '__main__':
    load_env_variable()
