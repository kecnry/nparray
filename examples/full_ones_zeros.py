import nparray as npa
import numpy as np

a = npa.full(10, np.inf)
print a
print a.to_linspace()

b = npa.ones(10)
print b
print b.to_full()
print b.to_linspace()

c = npa.zeros(10)
print c
print c.to_full()
print c.to_linspace()
