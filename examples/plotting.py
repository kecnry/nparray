import nparray as npa
import matplotlib.pyplot as plt

x = npa.linspace(0,10,101)
y = npa.logspace(1,100,101,base=2)

plt.plot(x,y)
plt.show()
