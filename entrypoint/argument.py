import argparse
import os
import sys


def print_all_arg():
    print(f"Name of the script      : {sys.argv[0]=}")
    print(f"Arguments of the script : {sys.argv[1:]=}")


def rev_arg():
    arg = sys.argv[1]
    print(arg[::-1])


def arg_parse():
    text = 'This is a test program.'
    parser = argparse.ArgumentParser(description=text)
    parser.add_argument('-v', '--version', help='show program version', action='store_true')
    parser.add_argument('-w', '--width', help='set output width')
    parser.add_argument("square", type=int, help="display a square of a given number")
    parser.add_argument("--verbose", type=int, choices=[0, 1, 2], help="increase output verbosity")

    args = parser.parse_args()

    if args.version:
        print('Version is 1.0')
    if args.width:
        print(f'Width is {args.width}')

    answer = args.square ** 2
    if args.verbose == 2:
        print("the square of {} equals {}".format(args.square, answer))
    elif args.verbose == 1:
        print("{}^2 == {}".format(args.square, answer))
    else:
        print(answer)


def verbosity():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int, help="display a square of a given number")
    parser.add_argument("-v", "--verbosity", action="count", default=0, help="increase output verbosity")
    args = parser.parse_args()
    answer = args.square ** 2
    if args.verbosity >= 2:
        print("the square of {} equals {}".format(args.square, answer))
    elif args.verbosity >= 1:
        print("{}^2 == {}".format(args.square, answer))
    else:
        print(answer)


def positional_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    parser.add_argument("-z", type=int, help="the exponent", required=True)
    parser.add_argument("-v", "--verbosity", action="count", default=0)

    args = parser.parse_args()
    answer = args.x ** args.y
    print(f'x: {args.x}, y: {args.y}, z: {args.z}')

    if args.verbosity >= 2:
        print("{} to the power {} equals {}".format(args.x, args.y, answer))
    elif args.verbosity >= 1:
        print("{}^{} == {}".format(args.x, args.y, answer))
    else:
        print(answer)


def mutually_exclusive():
    parser = argparse.ArgumentParser(description="calculate X to the power of Y")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    args = parser.parse_args()
    answer = args.x ** args.y

    if args.quiet:
        print(answer)
    elif args.verbose:
        print("{} to the power {} equals {}".format(args.x, args.y, answer))
    else:
        print("{}^{} == {}".format(args.x, args.y, answer))


def sub_parser():
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('--foo', action='store_true', help='foo help')
    subparsers = parser.add_subparsers(title='a', description='a desc', help='sub-command help')

    # create the parser for the "a" command
    parser_a = subparsers.add_parser('a', help='a help')
    parser_a.add_argument('bar', type=int, help='bar help')

    # create the parser for the "b" command
    parser_b = subparsers.add_parser('b', help='b help')
    parser_b.add_argument('--baz', choices='XYZ', help='baz help')

    args = parser.parse_args()
    print(args)


def default_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('--api', help="Api URL", default=os.getenv(f'JAVA_HOME'))

    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    # print_all_arg()
    # rev_arg()
    # arg_parse()
    # verbosity()
    # positional_arg()
    # mutually_exclusive()
    # sub_parser()
    default_arg()
