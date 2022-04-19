import math

n = int(input())
k = int(input())

def newton(n,k):
    print(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

newton(n,k)