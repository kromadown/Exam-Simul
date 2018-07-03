import math

def f(n):
    return (-1)**n*x**(2*n+1)/math.factorial(2*n+1)

x = math.pi/3
n = 10
s = 0

for i in range(n+1):
    s += f(i)

exact = math.sin(x)
est = exact - s

print (est)
print (exact)
