### [Eye](Eye.md).__init__ (function)


```py

def __init__(self, M, N=None, k=0, unit=None)

```



This is available as a top-level convenience function as [nparray.eye](nparray.eye.md).

Arguments
------------
* `M` (int): Number of rows in the output.
* `N` (int or None, optional, default=None): Number of columns in the output.
    If None, defaults to `N`.
* `k` (int, optional, default=1): Index of the diagonal: 0 (the default)
    refers to the main diagonal, a positive value refers to an upper
    diagonal, and a negative value to a lower diagonal.
* `unit` (astropy unit or string, optional, default=None): unit
  corresponding to the passed values.

Returns
-----------
* [Eye](Eye.md)

