from nose.tools import assert_raises

import nparray as npa
import numpy as np

def test_create():
    np_a = np.arange(0,1,0.1)
    npa_a = npa.arange(0,1,0.1)

    assert(np.alltrue(np_a==npa_a.array))
    assert(np_a.tolist()==npa_a.tolist())

def test_create_errors():
    # passing string
    assert_raises(ValueError, npa.arange, 0, "1", 1)

    # not enough args
    assert_raises(TypeError, npa.arange, 0, 1)

    # too many args
    assert_raises(TypeError, npa.arange, 0, 1, 1, True, None, 1)

def test_conversions():
    npa_a = npa.arange(0,1,0.1)

    npa_b = npa_a.to_linspace()
    assert(np.alltrue(npa_a.array == npa_b.array))

def test_math():
    npa_a = npa.arange(0,1,0.1)

    npa_a+1
    npa_a*5



if __name__ == '__main__':
    test_create()
    test_create_errors()
    test_conversions()
    test_math()
