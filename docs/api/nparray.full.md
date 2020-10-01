### [nparray](nparray.md).full (function)


```py

def full(shape, fill_value, unit=None)

```



This is an nparray wrapper around the numpy function.  The
numpy documentation is included below.  Currently most kwargs
should be accepted with the exception of 'dtype'.  The returned
object should act exactly like the numpy array itself, but with
several extra helpful methods and attributes.  Call help on the
resulting object for more information.

If you have astropy installed, units are supported by passing unit=astropy.unit
to the instantiation functions or by multiplying an array with a unit object.


See also:

* [nparray.full_like](nparray.full_like.md)

Arguments
------------
* `shape` (int or sequence of ints): Shape of the new array, e.g.,
``(2, 3)`` or ``2``.
* `fill_value` (int or float): Value to fill each element in the array.
* `unit` (astropy unit or string, optional, default=None): unit
corresponding to the passed values.

Returns
-----------
* [Full](Full.md)


===============================================================

** numpy documentation for underlying function: **


    Return a new array of given shape and type, filled with `fill_value`.

    Parameters
    ----------
    shape : int or sequence of ints
        Shape of the new array, e.g., ``(2, 3)`` or ``2``.
    fill_value : scalar
        Fill value.
    dtype : data-type, optional
        The desired data-type for the array  The default, `None`, means
         `np.array(fill_value).dtype`.
    order : {'C', 'F'}, optional
        Whether to store multidimensional data in C- or Fortran-contiguous
        (row- or column-wise) order in memory.

    Returns
    -------
    out : ndarray
        Array of `fill_value` with the given shape, dtype, and order.

    See Also
    --------
    full_like : Return a new array with shape of input filled with value.
    empty : Return a new uninitialized array.
    ones : Return a new array setting values to one.
    zeros : Return a new array setting values to zero.

    Examples
    --------
    &gt;&gt;&gt; np.full((2, 2), np.inf)
    array([[inf, inf],
           [inf, inf]])
    &gt;&gt;&gt; np.full((2, 2), 10)
    array([[10, 10],
           [10, 10]])

    

