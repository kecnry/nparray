### [Arange](Arange.md).__init__ (method)


```py

def __init__(self, start, stop, step, unit=None)

```



This is available as a top-level convenience function as [nparray.arange](nparray.arange.md).

Arguments
------------
* `start` (int or float): the starting point of the sequence.
* `stop` (int or float): the ending point of the sequence.  The interval
    does not include this value, except in some cases where `step` is not an
    integer and floating point round-off affects the length of the array.
* `step` (int or float): the stepsize between each item in the sequence.
* `unit` (astropy unit or string, optional, default=None): unit
  corresponding to the passed values.

Returns
-----------
* [Arange](Arange.md)

