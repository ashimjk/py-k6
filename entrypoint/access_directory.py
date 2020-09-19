import os
from pathlib import Path


def read_file():
    with open('../package.json', 'r') as f:
        data = f.readlines()
        print(data)


def read_directory():
    entries = os.listdir('../py-k6')
    for entry in entries:
        print(entry)


def read_directory1():
    with os.scandir('../py-k6') as entries:
        for entry in entries:
            print(entry.name)


def read_directory2():
    entries = Path('../py-k6')
    for entry in entries.iterdir():
        print(entry.name)


def read_directory3():
    for root, directories, files in os.walk('../src', topdown=False):
        for name in directories:
            print(os.path.join(root, name))
        for name in files:
            print(os.path.join(root, name))


def search_js_file():
    for root, dirs, files in os.walk('../src', topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            if filename.endswith('.js'):
                print(filename)


if __name__ == '__main__':
    # read_file()
    # read_directory()
    # read_directory1()
    # read_directory2()
    # read_directory3()
    search_js_file()
