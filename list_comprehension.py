# List comprehension in Python is a concise way of creating lists from the ones that already exist.
# It offers a shorter syntax when creating a new list based on the values of an existing list.

#a simple list comprehension
squares = [x**2 for x in range(1, 15)]
print(squares)  


#list comprehension with a condition
evens = [x for x in range(1, 15) if x % 2 == 0]
print(evens)  


#Nested list comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)  


