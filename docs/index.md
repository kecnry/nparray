# nparray

**High-level Wrappers for Building and Manipulating Numpy Arrays**

[![GitHub](https://img.shields.io/badge/github-kecnry%2Fnparray-blue.svg)](https://github.com/kecnry/nparray)
[![License](https://img.shields.io/badge/license-GPL3-blue.svg)](https://github.com/kecnry/nparray/blob/master/LICENSE)
[![travis build status](https://travis-ci.org/kecnry/nparray.svg?branch=master)](https://travis-ci.org/kecnry/nparray)
[![Documentation Status](https://readthedocs.org/projects/nparray/badge/?version=latest)](https://nparay.readthedocs.io/en/latest/?badge=latest)


Create numpy arrays (via arange, linspace, etc) and manipulate the creation arguments at any time.  The created object acts as a numpy array but only stores the input parameters until its value is accessed.

The following snippet should give you a better idea of the purpose of nparray.  Note that under-the-hood are *actual* numpy arrays, meaning passing directly to matplotlib works fine, but using isinstance or type will currently not recognize the numpy array (at least for now - see [this issue](https://github.com/kecnry/nparray/issues/6)).

```py
import nparray as npa

a = npa.arange(0,1,0.1)
print(a)
# <arange start=0 stop=1 step=0.1>
print(a[-1])
# 0.9
a.step=0.5
print(a)
# <arange start=0 stop=1 step=0.5>
print(a[-1])
# 0.5
b = a.to_linspace()
print(b)
# <linspace start=0 stop=0.5 num=2, endpoint=True>
print(b*3)
# <linspace start=0, stop=1.5, num=2, endpoint=True>
b[1] = 99
print(b)
# <array value=[0, 99]>
```

## Getting Started

### Dependencies

**nparray** requires the following dependencies:

  - python 2.7+ or 3.6+
  - numpy 1.10+
  - collections (should be standard python module)

and the following optional dependencies:

  - astropy 1.0+ (required for units support)


You can see the [Travis testing matrix](https://travis-ci.org/kecnry/nparray) for
details on what exact versions have been tested and ensured to work.  If you run
into any issues with dependencies, please [submit an issue](https://github.com/kecnry/nparray/issues/new).

### Installation

**nparray** is available via [pip](https://pypi.org/project/nparray/):

```sh
pip install nparray
```

Alternatively, to install from source, use the standard python setup.py commands.

To install globally:
```sh
python setup.py build
sudo python setup.py install
```

Or to install locally:
```sh
python setup.py build
python setup.py install --user
```

### Import

Now from within python we can import the `nparray` package:

```py
import nparray
```

## Supported Array Types

**nparray** currently supports the following with all arguments (except for dtype - see [open issue](https://github.com/kecnry/nparray/issues/8)):

* [array](api/nparray.array.md)
* [arange](api/nparray.arange.md)
    * [to_array](api/Arange.to_array.md)
    * [to_linspace](api/Arange.to_linspace.md)
* [linspace](api/nparray.linspace.md)
    * [to_array](api/Linspace.to_array.md)
    * [to_arange](api/Linspace.to_arange.md)
* [logspace](api/nparray.logspace.md)
    * [to_array](api/Logspace.to_array.md)
* [geomspace](api/nparray.geomspace.md)
    * [to_array](api/Geomspace.to_array.md)
* [full](api/nparray.full.md) or [full_like](api/nparray.full_like.md)
    * [to_array](api/Full.to_array.md)
* [zeros](api/nparray.zeros.md) or [zeros_like](api/nparray.zeros_like.md)
    * [to_array](api/Zeros.to_array.md)
    * [to_full](api/Zeros.to_full.md)
    * [to_linspace](api/Zeros.to_linspace.md)
* [ones](api/nparray.ones.md) or [ones_like](api/nparray.ones_like.md)
    * [to_array](api/Ones.to_array.md)
    * [to_full](api/Ones.to_full.md)
    * [to_linspace](api/Ones.to_linspace.md)
* [eye](api/nparray.eye.md)
    * [to_array](api/Eye.to_array.md)


## Math on Array Objects

Whenever possible, math on nparray objects will attempt to return another
nparray object of the same type.  When not possible, an [nparray.Array](api/Array.md)
object will be return which only stores the underlying array value itself.

## Comparing Array Objects

Comparison operators on nparray objects will act on the computed array object
itself.

```py
import nparray

a = nparray.linspace(0,1,10,False)
b = nparray.arange(0,1,0.1)
a==b
```

## Support for Units

**NOTE:** astropy is required for units support.

```py
import nparray
import astropy.units as u

a = nparray.linspace(0,1,11)

q = a * u.m

print(a)
print(q)
print(q.value)
```

## MonkeyPatching Numpy

Optionally, you can [monkeypatch](api/nparray.monkeypatch.md) numpy so that calling
any of the numpy versions (`np.array`, `np.linspace`, etc), will actually call
the nparray version instead.

```py
import nparray
import numpy

nparray.monkeypatch()
print(np.linspace(0,1,11))
```

## API Documentation

See the [API documentation](./api.md) for full details on each type of supported array.

## Contributors

[Kyle Conroy](https://github.com/kecnry)

Contributions are welcome!  Feel free to file an issue or fork and create a pull-request.
