import numpy

x = int(input("Enter number x: "))
y = int(input("Enter number y: "))

squared = x**y
log = numpy.log2(x)

print("x**y = " + str(squared))
print("log(x) = " + str(log))