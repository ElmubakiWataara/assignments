"""Write a short Python function, minmax(data), that takes a sequence of one or more numbers,
and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use
the built-in functions min or max in implementing your solution."""


def minmax(numbers):
    if len(numbers)==0:
        return None
    
    smallest = float('inf')
    largest = float('-inf')
    
    for i in numbers:
        if i < smallest:
           smallest = i
        if i > largest:
           largest = i
    return (smallest,largest)
Numbers = [1,17,2,3,6]
results = minmax(Numbers)
print(results)
#print(minmax([1,17,2,3,6]))   #alternative calling
    
  