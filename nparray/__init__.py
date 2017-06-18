import nparray as _wrappers
import json
import os

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

def from_dict(d):
    """
    """
    if not isinstance(d, dict):
        raise TypeError("argument must be of type dict")
    if 'nparray' not in d.keys():
        raise ValueError("input dictionary missing 'nparray' entry")

    classname = d.pop('nparray').title()
    return getattr(_wrappers, classname)(**d)

def from_json(j):
    """
    """
    if not (isinstance(j, str) or isinstance(j, unicode)):
        raise TypeError("argument must be of type str")

    return from_dict(json.loads(j))

def from_file(filename):
    """
    """
    f = open(filename, 'r')
    j = json.load(f)
    f.close()

    return from_dict(j)
