array = [2, 8, 9, 48, 8, 22, -12, 2]

filtered = [x for x in array if x > 5]

transformed = [x + 2 for x in filtered]

print(array, end='$\n')
print(transformed, end='$\n')
