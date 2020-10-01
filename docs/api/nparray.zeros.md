### [nparray](nparray.md).zeros (function)


```py

def zeros(shape, unit=None)

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

* [nparray.zeros_like](nparray.zeros_like.md)

Arguments
------------
* `shape` (int or sequence of ints): Shape of the new array, e.g.,
``(2, 3)`` or ``2``.
* `unit` (astropy unit or string, optional, default=None): unit
corresponding to the passed values.

Returns
-----------
* [Zeros](Zeros.md)


===============================================================

** numpy documentation for underlying function: **

zeros(shape, dtype=float, order='C')

    Return a new array of given shape and type, filled with zeros.

    Parameters
    ----------
    shape : int or tuple of ints
        Shape of the new array, e.g., ``(2, 3)`` or ``2``.
    dtype : data-type, optional
        The desired data-type for the array, e.g., `numpy.int8`.  Default is
        `numpy.float64`.
    order : {'C', 'F'}, optional, default: 'C'
        Whether to store multi-dimensional data in row-major
        (C-style) or column-major (Fortran-style) order in
        memory.

    Returns
    -------
    out : ndarray
        Array of zeros with the given shape, dtype, and order.

    See Also
    --------
    zeros_like : Return an array of zeros with shape and type of input.
    empty : Return a new uninitialized array.
    ones : Return a new array setting values to one.
    full : Return a new array of given shape filled with value.

    Examples
    --------
    &gt;&gt;&gt; np.zeros(5)
    array([ 0.,  0.,  0.,  0.,  0.])

    &gt;&gt;&gt; np.zeros((5,), dtype=int)
    array([0, 0, 0, 0, 0])

    &gt;&gt;&gt; np.zeros((2, 1))
    array([[ 0.],
           [ 0.]])

    &gt;&gt;&gt; s = (2,2)
    &gt;&gt;&gt; np.zeros(s)
    array([[ 0.,  0.],
           [ 0.,  0.]])

    &gt;&gt;&gt; np.zeros((2,), dtype=[('x', 'i4'), ('y', 'i4')]) # custom dtype
    array([(0, 0), (0, 0)],
          dtype=[('x', '&lt;i4'), ('y', '&lt;i4')])

