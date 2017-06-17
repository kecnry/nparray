import nparray as _wrappers

# allow isinstance(obj, nparray.ndarray) to be similar to numpy
ndarray = _wrappers.ArrayWrapper

def array(value):
    """
    """
    return _wrappers.Array(value)

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

def full_like(a, fill_value):
    """
    """
    return _wrappers.Full(a.shape, fill_value)

def zeros(shape):
    """
    """
    return _wrappers.Zeros(shape)

def zeros_like(a):
    """
    """
    return _wrappers.Zeros(a.shape)

def ones(shape):
    """
    """
    return _wrappers.Ones(shape)

def ones_like(a):
    """
    """
    return _wrappers.Ones(a.shape)

def eye(M, N=None, k=1):
    """
    """
    return _wrappers.Eye(M, N, k)
