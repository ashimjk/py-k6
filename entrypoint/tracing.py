def tracing(func):
    def executor():
        print('Tracing started')
        func()
        print('Tracing ended')

    return executor


@tracing
def starter():
    print('Start')


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)

    return inner


@smart_divide
def divide(a, b):
    print(a / b)


def star(func):
    def inner(*args, **kwargs):
        print(f'args:{args}')
        print(f'kwargs:{kwargs}')
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)

    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)

    return inner


@star
@percent
def printer(msg):
    print(msg)


@star
def printer2(msg, msg1, msg2):
    print(msg, msg1, msg2)


if __name__ == '__main__':
    # tracing(starter)()
    # starter()
    # divide(2, 5)
    # divide(2, 0)
    # printer('Hello')
    printer2(msg='Hello', msg2='Ashim', msg1='Here')
