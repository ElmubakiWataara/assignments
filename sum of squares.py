"""Write a short Python function that takes a positive integer n and returns the sum of the
squares of all the positive integers smaller than n."""


def integer(n):
    if n < 0:
        print("Input a positive value")
        return None
    sum = 0
    for i in range(0,n):
        sum = i**2 + sum
    return sum
    
n = 12
results = integer(n)
print(results)

