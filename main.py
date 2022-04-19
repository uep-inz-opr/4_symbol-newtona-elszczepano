import math

elements = input().split( " " )

n = int(elements[0])
k = int(elements[1])

def newton(n,k):
    print(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

newton(n,k)