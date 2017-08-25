import nparray as npa
import numpy as np

print "BEFORE MONKEYPATCH"
print np.arange(0,1,0.1)

npa.monkeypatch()

print "AFTER MONKEYPATCH"
print np.arange(0,1,0.1)
