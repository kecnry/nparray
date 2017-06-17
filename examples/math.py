import nparray

a = nparray.linspace(0,1,11)
b = nparray.linspace(5,10,11).to_arange()
c = nparray.zeros(11)

# when possible, math on nparrays will attempt to return a smart nparray.  Otherwise
# it will return an Array object which only stores the underlying array itself
print "a: ", a
print "b: ", b
print "c: ", c
print "a+5: ", a+5
print "a+b: ", a+b
print "a*5+b/2: ", a+5+b
print "c+3: ", c+3
