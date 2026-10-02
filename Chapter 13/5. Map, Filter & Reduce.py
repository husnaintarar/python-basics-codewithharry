#Map Example
a = [1, 2, 3, 4, 5]
square = list(map(lambda x: x ** 2, a)) 
print(square)

#Filter Example
b = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, b))
print(even)

#Reduce Example
from functools import reduce    
c = [1, 2, 3, 4, 5] 
sum = reduce(lambda x, y: x + y, c)
print(sum)