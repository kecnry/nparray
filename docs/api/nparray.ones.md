### [nparray](nparray.md).ones (function)


```py

def ones(shape, unit=None)

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

* [nparray.ones_like](nparray.ones_like.md)

Arguments
------------
* `shape` (int or sequence of ints): Shape of the new array, e.g.,
``(2, 3)`` or ``2``.
* `unit` (astropy unit or string, optional, default=None): unit
corresponding to the passed values.

Returns
-----------
* [Ones](Ones.md)


===============================================================

** numpy documentation for underlying function: **


    Return a new array of given shape and type, filled with ones.

    Parameters
    ----------
    shape : int or sequence of ints
        Shape of the new array, e.g., ``(2, 3)`` or ``2``.
    dtype : data-type, optional
        The desired data-type for the array, e.g., `numpy.int8`.  Default is
        `numpy.float64`.
    order : {'C', 'F'}, optional
        Whether to store multidimensional data in C- or Fortran-contiguous
        (row- or column-wise) order in memory.

    Returns
    -------
    out : ndarray
        Array of ones with the given shape, dtype, and order.

    See Also
    --------
    zeros, ones_like

    Examples
    --------
    &gt;&gt;&gt; np.ones(5)
    array([ 1.,  1.,  1.,  1.,  1.])

    &gt;&gt;&gt; np.ones((5,), dtype=int)
    array([1, 1, 1, 1, 1])

    &gt;&gt;&gt; np.ones((2, 1))
    array([[ 1.],
           [ 1.]])

    &gt;&gt;&gt; s = (2,2)
    &gt;&gt;&gt; np.ones(s)
    array([[ 1.,  1.],
           [ 1.,  1.]])

    

