# sub-command functions
import argparse
import sys


def foo(args):
    print(args.x * args.y)


def bar(args):
    print('((%s))' % args.z)


def subcmd():
    # create the top-level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # create the parser for the "foo" command
    parser_foo = subparsers.add_parser('foo')
    parser_foo.add_argument('-x', type=int, default=1)
    parser_foo.add_argument('y', type=float)
    parser_foo.set_defaults(func=foo)

    # create the parser for the "bar" command
    parser_bar = subparsers.add_parser('bar')
    parser_bar.add_argument('z')
    parser_bar.set_defaults(func=bar)

    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    else:
        args.func(args)


if __name__ == '__main__':
    subcmd()
