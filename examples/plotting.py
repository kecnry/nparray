import nparray
import matplotlib.pyplot as plt

x = nparray.linspace(0,10,101)
y = nparray.logspace(1,100,101,base=2)

plt.plot(x,y)
plt.show()
