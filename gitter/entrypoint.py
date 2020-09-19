import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', help='Version')
    args = parser.parse_args()

    print('starter')
    print(args)


if __name__ == '__main__':
    main()
