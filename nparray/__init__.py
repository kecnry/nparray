import nparray as _wrappers

def linspace(start, stop, num):
    """
    """
    return _wrappers.Linspace(start, stop, num)

def arange(start, stop, step):
    """
    """
    return _wrappers.Arange(start, stop, step)

def zeros(shape):
    """
    """
    return _wrappers.Zeros(shape)

def ones(shape):
    """
    """
    return _wrappers.Ones(shape)
