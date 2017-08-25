import nparray as npa
import numpy as np
import json

a = npa.linspace(0,1,10)

print a


##### DICTIONARY #####
d = a.to_dict()

print d

b = npa.from_dict(d)

print b
print np.all(b==a)


##### JSON #####
j = a.to_json()

print j

c = npa.from_json(j)

print c
print np.all(a==c)


##### FILE #####
f = a.to_file('save_load.json')

print f

d = npa.from_file(f)

print d
print np.all(a==d)
