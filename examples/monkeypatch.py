import nparray
import numpy as np

print "BEFORE MONKEYPATCH"
print np.arange(0,1,0.1)

nparray.monkeypatch()

print "AFTER MONKEYPATCH"
print np.arange(0,1,0.1)
