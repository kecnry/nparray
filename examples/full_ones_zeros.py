import nparray
import numpy as np

a = nparray.full(10, np.inf)
print a
print a.to_linspace()

b = nparray.ones(10)
print b
print b.to_full()
print b.to_linspace()

c = nparray.zeros(10)
print c
print c.to_full()
print c.to_linspace()
