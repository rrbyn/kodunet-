import random

x = 0
numbers = []
output = []

while x < 5:
    numbers.append(random.randint(1, 100))
    x = x + 1
    
print (numbers)
output.insert(0,(numbers[0]))
output.insert(1,(numbers[-1]))
print (output)
