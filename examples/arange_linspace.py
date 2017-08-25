import nparray as npa
import numpy as np

# we'll build the same arrays, both through numpy as nparray
np_a = np.arange(0, 1, 0.1)
npa_a = npa.arange(0, 1, 0.1)

# the numpy array is just... the array
print np_a

# whereas the nparray array holds the arguments used to make that array
print npa_a

# to access the array itself we can call .array
print npa_a.array

# but the object also acts exactly as an actual numpy array would.  So you
# don't need to go through .array
print np_a[0]
print npa_a[0]


print np_a.tolist()
print npa_a.tolist()

print len(np_a)
# print len(nparray_a)  # BUG: this doesn't work quite yet

# the only things you can't do (yet) are operations that actually change the
# underlying array
# np_a[1] = 2 would work, but
# nparray_a[1] = 2 raises an error

# but you can change any of the arguments
npa_a.stop=5
print npa_a
print npa_a.array

# and you can also convert between some supported types
print npa_a.to_linspace()
