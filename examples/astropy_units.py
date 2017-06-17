import nparray
import astropy.units as u

a = nparray.linspace(0,1,11)

q = a * u.m

print a
print q
print q.value
