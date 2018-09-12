from nose.tools import assert_raises

import nparray as npa
import numpy as np

def test_create():
    for endpoint in [True, False]:
        np_a = np.linspace(0,1,11, endpoint=endpoint)
        npa_a = npa.linspace(0,1,11, endpoint=endpoint)

        assert(np.alltrue(np_a==npa_a.array))
        assert(np_a.tolist()==npa_a.tolist())

def test_create_errors():
    # passing string
    assert_raises(ValueError, npa.linspace, 0, "1", 11)

    # not enough args
    assert_raises(TypeError, npa.linspace, 0, 1)

    # test type of optional endpoint
    assert_raises(ValueError, npa.linspace, 0, 1, 1, 5)

    # too many args
    assert_raises(TypeError, npa.linspace, 0, 1, 1, True, None, 1)

def test_conversions():
    npa_a = npa.linspace(0,1,11)

    npa_b = npa_a.to_arange()
    assert(np.alltrue(npa_a.array == npa_b.array))

def test_math():
    npa_a = npa.linspace(0,1,11)

    npa_a+1
    npa_a*5



if __name__ == '__main__':
    test_create()
    test_create_errors()
    test_conversions()
    test_math()
