import nparray as npa
import astropy.units as u

a = npa.linspace(0,1,11)

q = a * u.m

print a
print q
print q.value
