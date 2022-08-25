# Demo of assignment operator
a = 2
b = 10
c = 0
c = a + b
print("Value of c is ", c)
c += a
print("Value of c += a (add-assign) is ", c)
c *= a
print("Value of c *= a (multiply-assign) is ", c)
c /= a
print("Value of c /= a (divide-assign) is ", c)
c **= a
print("Value of c **= a (exponential assign) is ", c)
c //= a
print("Value of c //= a (floor division assign) is ", c)
c %= a
print("Value of c %= a (remainder-assign) is ", c)
