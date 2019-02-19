### [Logspace](Logspace.md).__init__ (method)


```py

def __init__(self, start, stop, num, endpoint=True, base=10.0, unit=None)

```



This is available as a top-level convenience function as [nparray.logspace](nparray.logspace.md).

Arguments
------------
* `start` (int or float): ``base ** start`` is the starting value of the sequence.
* `stop` (int or float): ``base ** stop`` is the final value of the sequence,
    unless `endpoint` is False.  In that case, ``num + 1`` values are spaced
    over the interval in log-space, of which all but the last (a sequence of
    length `num`) are returned.
* `num` (int): number of samples to generate.
* `endpoint` (bool, optional, default=True): If True, `stop` is the last
    sample. Otherwise, it is not included.
* `base` (float, optional, default=10.0): The base of the log space. The
    step size between the elements in ``ln(samples) / ln(base)``
    (or ``log_base(samples)``) is uniform.
* `unit` (astropy unit or string, optional, default=None): unit
  corresponding to the passed values.

Returns
-----------
* [Logspace](Logspace.md)

