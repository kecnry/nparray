from nose.tools import assert_raises

import nparray as npa
import numpy as np
import astropy.units as u

def test_create():
    np_a = np.linspace(0,1,11) * u.solRad
    npa_a = npa.linspace(0,1,11) * u.solRad
    npa_b = npa.linspace(0, 1, 11, unit=u.solRad)

    assert(npa_a.unit==npa_b.unit)

    assert(np.alltrue(np_a==npa_a.quantity))
    assert(np_a.value.tolist()==npa_a.array.tolist())


def test_conversions():
    npa_a = npa.linspace(0,1,11) * u.solRad

    npa_b = npa_a.to_arange()
    assert(np.alltrue(npa_a.array == npa_b.array))

def test_copy():
    npa_a = npa.linspace(0,1,11) * u.solRad
    npa_b = npa_a.copy()

    assert(np.alltrue(npa_a.quantity == npa_b.quantity))

def test_to():
    npa_solRad = npa.linspace(0,1,11) * u.solRad
    npa_km = npa_solRad.to(u.km)

    assert(npa_km[-1]==(1.0*u.solRad).to(u.km).value)

if __name__ == '__main__':
    test_create()
    test_conversions()
