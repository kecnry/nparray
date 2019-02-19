### [nparray](nparray.md).full_like (function)


```py

def full_like(a, fill_value, unit=None)

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

* [nparray.full](nparray.full.md)

Arguments
------------
* `a` (list or array): The shape of `a` define these same attributes of the
returned array.
* `fill_value` (int or float): Value to fill each element in the array.
* `unit` (astropy unit or string, optional, default=None): unit
corresponding to the passed values.

Returns
-----------
* [Full](Full.md)


===============================================================

** numpy documentation for underlying function: **


    Return a full array with the same shape and type as a given array.

    Parameters
    ----------
    a : array_like
        The shape and data-type of `a` define these same attributes of
        the returned array.
    fill_value : scalar
        Fill value.
    dtype : data-type, optional
        Overrides the data type of the result.
    order : {'C', 'F', 'A', or 'K'}, optional
        Overrides the memory layout of the result. 'C' means C-order,
        'F' means F-order, 'A' means 'F' if `a` is Fortran contiguous,
        'C' otherwise. 'K' means match the layout of `a` as closely
        as possible.
    subok : bool, optional.
        If True, then the newly created array will use the sub-class
        type of 'a', otherwise it will be a base-class array. Defaults
        to True.

    Returns
    -------
    out : ndarray
        Array of `fill_value` with the same shape and type as `a`.

    See Also
    --------
    zeros_like : Return an array of zeros with shape and type of input.
    ones_like : Return an array of ones with shape and type of input.
    empty_like : Return an empty array with shape and type of input.
    zeros : Return a new array setting values to zero.
    ones : Return a new array setting values to one.
    empty : Return a new uninitialized array.
    full : Fill a new array.

    Examples
    --------
    &gt;&gt;&gt; x = np.arange(6, dtype=int)
    &gt;&gt;&gt; np.full_like(x, 1)
    array([1, 1, 1, 1, 1, 1])
    &gt;&gt;&gt; np.full_like(x, 0.1)
    array([0, 0, 0, 0, 0, 0])
    &gt;&gt;&gt; np.full_like(x, 0.1, dtype=np.double)
    array([ 0.1,  0.1,  0.1,  0.1,  0.1,  0.1])
    &gt;&gt;&gt; np.full_like(x, np.nan, dtype=np.double)
    array([ nan,  nan,  nan,  nan,  nan,  nan])

    &gt;&gt;&gt; y = np.arange(6, dtype=np.double)
    &gt;&gt;&gt; np.full_like(y, 0.1)
    array([ 0.1,  0.1,  0.1,  0.1,  0.1,  0.1])

    

