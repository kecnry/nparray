# nparray

Create numpy arrays (via arange, linspace, etc) and manipulate the creation arguments at any time.  The created object acts as a numpy array but only stores the input parameters.

The following snippet should give you a better idea of the purpose of nparray.  Note that under-the-hood are *actual* numpy arrays, but using isinstance or type will currently not recognize the numpy array.

**NOTE**: this is a work-in-progress and currently only supports arange and linspace, but support for more are coming.

```
import nparray

a = nparray.arange(0,1,0.1)
print a
# <arange start=0 stop=1 step=0.1>
print a[-1]
# 0.9
a.step=0.5
print a
# <arange start=0 stop=1 step=0.5>
print a[-1]
# 0.5
b = a.to_linspace()
print b
# <linspace start=0 stop=0.5 num=2>
```

## Dependencies

* [numpy](https://github.com/numpy/numpy)
* collections (should be standard python module)

nparray is currently only tested on Python 2.7 with numpy 1.12.1

## Installation

Installation is done using the standard python setup.py commands.

To install globally:

```
python setup.py build
sudo python setup.py install
```

Or to install locally:

```
python setup.py build
python setup.py install --user
```

## Basic Usage

See the snippet above or the examples in the examples directory.

## Contributing

Contributions are welcome! Feel free to file an issue or fork and create a pull-request.
