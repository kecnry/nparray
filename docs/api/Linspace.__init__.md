### [Linspace](Linspace.md).__init__ (method)


```py

def __init__(self, start, stop, num, endpoint=True, unit=None)

```



This is available as a top-level convenience function as [nparray.linspace](nparray.linspace.md).

Arguments
------------
* `start` (int or float): the starting point of the sequence.
* `stop` (int or float): the ending point of the sequence, unless `endpoint`
    is set to False.  In that case, the sequence consists of all but the
    last of ``num + 1`` evenly spaced samples, so that `stop` is excluded.
    Note that the step size changes when `endpoint` is False.
* `num` (int): number of samples to generate.
* `endpoint` (bool, optional, default=True): If True, `stop` is the last
    sample. Otherwise, it is not included.
* `unit` (astropy unit or string, optional, default=None): unit
    corresponding to the passed values.

Returns
-----------
* [Linspace](Linspace.md)

