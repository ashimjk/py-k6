import inspect


def get_caller_info(level: str):
    module = ((inspect.stack()[2][1].split("/")[-1]).split(".")[0]).upper()
    lineno = inspect.stack()[2][2]
    function = inspect.stack()[2][3]
    prefix = f"[{level}][{module}.{function}:{lineno}] "
    return prefix


if __name__ == '__main__':
    get_caller_info('    ')
