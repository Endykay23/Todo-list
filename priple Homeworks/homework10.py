import itertools

# Sample data
data = ['A', 'B', 'C']

# Permutations: All possible arrangements of the elements
print("Permutations:")
for perm in itertools.permutations(data):
    print(perm)

# Combinations: All possible combinations of two elements
print("\nCombinations (2 elements):")
for comb in itertools.combinations(data, 2):
    print(comb)

# Cartesian Product: All possible pairs (with repetition) of elements
print("\nCartesian Product (pairs):")
for prod in itertools.product(data, repeat=2):
    print(prod)

# Accumulate: Running totals of the elements
numbers = [1, 2, 3, 4, 5]
print("\nAccumulate (running totals):")
for total in itertools.accumulate(numbers):
    print(total)
