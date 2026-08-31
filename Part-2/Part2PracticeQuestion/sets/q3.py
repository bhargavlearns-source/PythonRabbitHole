
# Create a list with some missing numbers from 1-20
available = [1, 2, 4, 5, 7, 9, 10, 12, 14, 15, 16, 18, 19, 20]

print(f"Available numbers: {available}")
print(f"Expected range: 1 to 20")

# Find missing numbers using sets
all_numbers = set(range(1, 21))  # Set of all numbers 1-20
available_set = set(available)
missing = all_numbers - available_set

print(f"\nMissing numbers: {sorted(missing)}")
print(f"Count of missing: {len(missing)}")
