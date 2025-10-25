
# Comparison of Logical Operators in Python

# Logical AND
a = True
b = False
print("a and b:", a and b)  # Returns True if both are True, else False

# Logical OR
print("a or b:", a or b)  # Returns True if at least one is True

# Logical NOT
print("not a:", not a)  # Returns the opposite of the boolean value
print("not b:", not b)

# Combining logical operators
x = 10
y = 20
z = 30

# Example: Logical AND and OR
result = (x < y) and (y < z)  # True and True -> True
print("Result of (x < y) and (y < z):", result)

result = (x > y) or (y < z)  # False or True -> True
print("Result of (x > y) or (y < z):", result)

# Example: Logical NOT
result = not (x > y)  # not False -> True
print("Result of not (x > y):", result)

# ...