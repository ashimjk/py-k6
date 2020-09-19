import shlex
import subprocess
from pprint import pprint


def run_k6():
    print(shlex.split('k6 run src/script.js'))

    process = subprocess.Popen(['k6', 'run', 'src/script.js'],
                               stdout=subprocess.PIPE,
                               universal_newlines=True)

    while True:
        output = process.stdout.readline()
        print(output.strip())

        return_code = process.poll()
        if return_code is not None:
            for output in process.stdout.readlines():
                print(output.strip())
            break


def start_process():
    process = subprocess.Popen(['ping', '-c 4', 'python.org'],
                               stdout=subprocess.PIPE,
                               universal_newlines=True)

    while True:
        output = process.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output
            for output in process.stdout.readlines():
                print(output.strip())
            break


john_data = {
    'name': 'John Q. Public',
    'street': '123 Main St.',
    'city': 'Anytown',
    'state': 'FL',
    'zip': 99999,
    'relationships': {
        'siblings': ['Michael R. Public', 'Suzy Q. Public'],
        'parents': ['John Q. Public Sr.', 'Mary S. Public'],
    }
}

if __name__ == '__main__':
    pprint(john_data)
    # print(john_data)
    # run_k6()
