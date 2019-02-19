### [nparray](nparray.md).ones_like (function)


```py

def ones_like(a, unit=None)

```



This is an nparray wrapper around the numpy function.  The
numpy documentation is included below.  Currently most kwargs
should be accepted with the exception of 'dtype'.  The returned
object should act exactly like the numpy array itself, but with
several extra helpful methods and attributes.  Call help on the
resulting object for more information.

If you have astropy installed, units are supported by passing unit=astropy.unit
to the instantiation functions or by multiplying an array with a unit object.


Note: unlike in the numpy version, the data-type of `a` is not currently
guaranteed to be maintained.

See also:

* [nparray.ones](nparray.ones.md)

Arguments
------------
* `a` (list or array): The shape of `a` define these same attributes of the
returned array.
* `unit` (astropy unit or string, optional, default=None): unit
corresponding to the passed values.

Returns
-----------
* [Ones](Ones.md)


===============================================================

** numpy documentation for underlying function: **


    Return an array of ones with the same shape and type as a given array.

    Parameters
    ----------
    a : array_like
        The shape and data-type of `a` define these same attributes of
        the returned array.
    dtype : data-type, optional
        Overrides the data type of the result.

        .. versionadded:: 1.6.0
    order : {'C', 'F', 'A', or 'K'}, optional
        Overrides the memory layout of the result. 'C' means C-order,
        'F' means F-order, 'A' means 'F' if `a` is Fortran contiguous,
        'C' otherwise. 'K' means match the layout of `a` as closely
        as possible.

        .. versionadded:: 1.6.0
    subok : bool, optional.
        If True, then the newly created array will use the sub-class
        type of 'a', otherwise it will be a base-class array. Defaults
        to True.

    Returns
    -------
    out : ndarray
        Array of ones with the same shape and type as `a`.

    See Also
    --------
    zeros_like : Return an array of zeros with shape and type of input.
    empty_like : Return an empty array with shape and type of input.
    zeros : Return a new array setting values to zero.
    ones : Return a new array setting values to one.
    empty : Return a new uninitialized array.

    Examples
    --------
    &gt;&gt;&gt; x = np.arange(6)
    &gt;&gt;&gt; x = x.reshape((2, 3))
    &gt;&gt;&gt; x
    array([[0, 1, 2],
           [3, 4, 5]])
    &gt;&gt;&gt; np.ones_like(x)
    array([[1, 1, 1],
           [1, 1, 1]])

    &gt;&gt;&gt; y = np.arange(3, dtype=float)
    &gt;&gt;&gt; y
    array([ 0.,  1.,  2.])
    &gt;&gt;&gt; np.ones_like(y)
    array([ 1.,  1.,  1.])

    

