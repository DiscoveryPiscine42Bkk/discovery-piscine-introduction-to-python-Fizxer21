original = [2, 8, 9, 48, 8, 22, -12, 2]

filtered = [x for x in original if x > 5]

new_array = [x + 2 for x in filtered]

no_duplicates = []
for x in new_array:
    if x not in no_duplicates:
        no_duplicates.append(x)

print(original)
print(no_duplicates)
