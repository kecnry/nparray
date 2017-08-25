import nparray as npa

a = npa.linspace(0,1,10,False)
b = npa.arange(0,1,0.1)

print a, a.array
print b, b.array
print a.array==b.array, a==b
print a==a.array
print 0 in a.array, 0 in a
