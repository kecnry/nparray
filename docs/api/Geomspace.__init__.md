### [Geomspace](Geomspace.md).__init__ (method)


```py

def __init__(self, start, stop, num, endpoint=True, unit=None)

```



This is available as a top-level convenience function as [nparray.geomspace](nparray.geomspace.md).

Arguments
------------
* `start` (int or float): the starting point of the sequence.
* `stop` (int or float): the final value of the sequence, unless `endpoint`
    is False.  In that case, ``num + 1`` values are spaced over the
    interval in log-space, of which all but the last (a sequence of
    length `num`) are returned.
* `num` (int): number of samples to generate.
* `endpoint` (bool, optional, default=True): If True, `stop` is the last
    sample. Otherwise, it is not included.
* `unit` (astropy unit or string, optional, default=None): unit
  corresponding to the passed values.

Returns
-----------
* [Geomspace](Geomspace.md)

