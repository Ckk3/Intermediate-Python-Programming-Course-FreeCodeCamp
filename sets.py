# Its a unordered collection of unique elements

my_set = set([1,2,3,4,5,5])
print(my_set)
print(type(my_set))

another_set = {1,2,3,4,5,5}
print(another_set)
print(type(another_set))

# Add an element to the set
my_set.add(6)
print(my_set)

# remove an element from the set
my_set.remove(6)
print(my_set)

# Add a duplicate element to the set
my_set.add(5)
print(my_set)

# combine sets
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}
union = odds.union(evens)
print(union)

# Intersection, get all the elements that are common in both sets
intersection = odds.intersection(evens)
print(intersection)
intersection = odds.intersection(primes)
print(intersection)
intersection = evens.intersection(primes)
print(intersection)

# Difference, get all the elements that are not common in first set
set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}
difference = set_a.difference(set_b)
print(difference)
difference = set_b.difference(set_a)
print(difference)

# Symmetric Difference, same as difference but it returns the elements that are not common in both sets
symetric_difference = set_a.symmetric_difference(set_b)
print(symetric_difference)

# Is subset, check if all the elements of one set are present in another set
set_a = {1,2,3,4,5}
set_b = {4,5}
print(set_b.issubset(set_a))
print(set_b.issuperset(set_a))
print(set_a.issubset(set_b))
print(set_a.issuperset(set_b))

# To copy, use .copy() method
set_a = {1,2,3,4,5}
set_b = set_a.copy()
print(set_b)
print(set_a)
set_b = set_a
set_b.add(6)
print(set_b)
print(set_a)

# Create a immutable set 

my_set = frozenset([1,2,3,4,5])
print(my_set)
print(type(my_set))