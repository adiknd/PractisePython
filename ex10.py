import random

a = random.sample(range(15), 10)
b = random.sample(range(15), 10)
common_elements = []
common_elements = [elem for elem in set(a) if elem in b and elem not in common_elements]
print(a)
print(b)
print(common_elements)
