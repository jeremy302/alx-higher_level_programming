from sys import stderr


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as err:
        print('Exception: {:s}'.format(str(err)), file=stderr)
        return None