### [nparray](nparray.md).linspace (function)


```py

def linspace(start, stop, num, endpoint=True, unit=None)

```



This is an nparray wrapper around the numpy function.  The
numpy documentation is included below.  Currently most kwargs
should be accepted with the exception of 'dtype'.  The returned
object should act exactly like the numpy array itself, but with
several extra helpful methods and attributes.  Call help on the
resulting object for more information.

If you have astropy installed, units are supported by passing unit=astropy.unit
to the instantiation functions or by multiplying an array with a unit object.


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


===============================================================

** numpy documentation for underlying function: **


    Return evenly spaced numbers over a specified interval.

    Returns `num` evenly spaced samples, calculated over the
    interval [`start`, `stop`].

    The endpoint of the interval can optionally be excluded.

    .. versionchanged:: 1.16.0
        Non-scalar `start` and `stop` are now supported.

    Parameters
    ----------
    start : array_like
        The starting value of the sequence.
    stop : array_like
        The end value of the sequence, unless `endpoint` is set to False.
        In that case, the sequence consists of all but the last of ``num + 1``
        evenly spaced samples, so that `stop` is excluded.  Note that the step
        size changes when `endpoint` is False.
    num : int, optional
        Number of samples to generate. Default is 50. Must be non-negative.
    endpoint : bool, optional
        If True, `stop` is the last sample. Otherwise, it is not included.
        Default is True.
    retstep : bool, optional
        If True, return (`samples`, `step`), where `step` is the spacing
        between samples.
    dtype : dtype, optional
        The type of the output array.  If `dtype` is not given, infer the data
        type from the other input arguments.

        .. versionadded:: 1.9.0

    axis : int, optional
        The axis in the result to store the samples.  Relevant only if start
        or stop are array-like.  By default (0), the samples will be along a
        new axis inserted at the beginning. Use -1 to get an axis at the end.

        .. versionadded:: 1.16.0

    Returns
    -------
    samples : ndarray
        There are `num` equally spaced samples in the closed interval
        ``[start, stop]`` or the half-open interval ``[start, stop)``
        (depending on whether `endpoint` is True or False).
    step : float, optional
        Only returned if `retstep` is True

        Size of spacing between samples.


    See Also
    --------
    arange : Similar to `linspace`, but uses a step size (instead of the
             number of samples).
    geomspace : Similar to `linspace`, but with numbers spaced evenly on a log
                scale (a geometric progression).
    logspace : Similar to `geomspace`, but with the end points specified as
               logarithms.

    Examples
    --------
    &gt;&gt;&gt; np.linspace(2.0, 3.0, num=5)
    array([2.  , 2.25, 2.5 , 2.75, 3.  ])
    &gt;&gt;&gt; np.linspace(2.0, 3.0, num=5, endpoint=False)
    array([2. ,  2.2,  2.4,  2.6,  2.8])
    &gt;&gt;&gt; np.linspace(2.0, 3.0, num=5, retstep=True)
    (array([2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)

    Graphical illustration:

    &gt;&gt;&gt; import matplotlib.pyplot as plt
    &gt;&gt;&gt; N = 8
    &gt;&gt;&gt; y = np.zeros(N)
    &gt;&gt;&gt; x1 = np.linspace(0, 10, N, endpoint=True)
    &gt;&gt;&gt; x2 = np.linspace(0, 10, N, endpoint=False)
    &gt;&gt;&gt; plt.plot(x1, y, 'o')
    [&lt;matplotlib.lines.Line2D object at 0x...&gt;]
    &gt;&gt;&gt; plt.plot(x2, y + 0.5, 'o')
    [&lt;matplotlib.lines.Line2D object at 0x...&gt;]
    &gt;&gt;&gt; plt.ylim([-0.5, 1])
    (-0.5, 1)
    &gt;&gt;&gt; plt.show()

    

