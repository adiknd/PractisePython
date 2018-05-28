values = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#even_values = []

#for value in values:
#    if value % 2 == 0:
#        even_values.append(value)

even_values = [value for value in values if value % 2 ==0]

print(even_values)