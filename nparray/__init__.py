import nparray as _wrappers
import numpy as np
import json
import os

# allow isinstance(obj, nparray.ndarray) to be similar to numpy
ndarray = _wrappers.ArrayWrapper

__docprefix__ = """
This is an nparray wrapper around the numpy function.  The
numpy documentation is included below.  Currently most kwargs
should be accepted with the exception of 'dtype'.  The returned
object should act exactly like the numpy array itself, but with
several extra helpful methods and attributes.  Call help on the
resulting object for more information.

===============================================================


"""

def array(value):
    return _wrappers.Array(value)

array.__doc__ = __docprefix__ + np.array.__doc__

def arange(start, stop, step):
    return _wrappers.Arange(start, stop, step)

arange.__doc__ = __docprefix__ + np.arange.__doc__

def linspace(start, stop, num, endpoint=True):
    return _wrappers.Linspace(start, stop, num, endpoint)

linspace.__doc__ = __docprefix__ + np.linspace.__doc__

def logspace(start, stop, num, endpoint=True, base=10.0):
    return _wrappers.Logspace(start, stop, num, endpoint, base)

logspace.__doc__ = __docprefix__ + np.logspace.__doc__

def geomspace(start, stop, num, endpoint=True):
    return _wrappers.Geomspace(start, stop, num, endpoint)

geomspace.__doc__ = __docprefix__ + np.geomspace.__doc__

def full(shape, fill_value):
    return _wrappers.Full(shape, fill_value)

full.__doc__ = __docprefix__ + np.full.__doc__

def full_like(a, fill_value):
    return _wrappers.Full(a.shape, fill_value)

full_like.__doc__ = __docprefix__ + np.full_like.__doc__

def zeros(shape):
    return _wrappers.Zeros(shape)

zeros.__doc__ = __docprefix__ + np.zeros.__doc__

def zeros_like(a):
    return _wrappers.Zeros(a.shape)

zeros_like.__doc__ = __docprefix__ + np.zeros_like.__doc__

def ones(shape):
    return _wrappers.Ones(shape)

ones.__doc__ = __docprefix__ + np.ones.__doc__

def ones_like(a):
    return _wrappers.Ones(a.shape)

ones_like.__doc__ = __docprefix__ + np.ones_like.__doc__

def eye(M, N=None, k=1):
    return _wrappers.Eye(M, N, k)

eye.__doc__ = __docprefix__ + np.eye.__doc__

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

def monkeypatch():
    np.array = array
    np.arange = arange
    np.linspace = linspace
    np.logspace = logspace
    np.geomspace = geomspace
    np.full = full
    np.full_like = full_like
    np.zeros = zeros
    np.zeros_like = zeros_like
    np.ones = ones
    np.ones_like = ones_like
    np.eye = eye
