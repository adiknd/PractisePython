prime_numbers = []
happy_numbers = []
common_numbers = []

with open('primenumbers.txt', 'r') as open_prime_numbers:
    line = open_prime_numbers.readline()
    while line:
        prime_numbers.append(line.strip())
        line = open_prime_numbers.readline()

with open('happynumbers.txt', 'r') as open_happy_numbers:
    line = open_happy_numbers.readline()
    while line:
        happy_numbers.append(line.strip())
        line = open_happy_numbers.readline()

for i in prime_numbers:
    if i in happy_numbers:
        common_numbers.append(i)

print(common_numbers)



