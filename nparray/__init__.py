import nparray as _wrappers

def arange(start, stop, step):
    """
    """
    return _wrappers.Arange(start, stop, step)

def linspace(start, stop, num, endpoint=True):
    """
    """
    return _wrappers.Linspace(start, stop, num, endpoint)

def logspace(start, stop, num, endpoint=True, base=10.0):
    """
    """
    return _wrappers.Logspace(start, stop, num, endpoint, base)

def geomspace(start, stop, num, endpoint=True):
    """
    """
    return _wrappers.Geomspace(start, stop, num, endpoint)

def full(shape, fill_value):
    """
    """
    return _wrappers.Full(shape, fill_value)

def zeros(shape):
    """
    """
    return _wrappers.Zeros(shape)

def ones(shape):
    """
    """
    return _wrappers.Ones(shape)
