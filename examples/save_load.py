import nparray
import numpy as np
import json

a = nparray.linspace(0,1,10)

print a


##### DICTIONARY #####
d = a.to_dict()

print d

b = nparray.from_dict(d)

print b
print np.all(b==a)


##### JSON #####
j = a.to_json()

print j

c = nparray.from_json(j)

print c
print np.all(a==c)


##### FILE #####
f = a.to_file('save_load.json')

print f

d = nparray.from_file(f)

print d
print np.all(a==d)
