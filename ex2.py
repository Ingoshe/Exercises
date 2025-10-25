# Demonstrate the floating-point precision issue by calculating 0.1 + 0.2 and explaining why the result isn't exactly 0.3
result = 0.1 + 0.2
print("The result of 0.1 + 0.2 is:", result)
print("The result is not exactly 0.3 because floating-point numbers are stored in binary format, and some decimal fractions, like 0.1 and 0.2, cannot be represented precisely in binary. This leads to small rounding errors.")
# This happens because floating-point numbers are represented in a way that cannot exactly capture all decimal fractions. In binary, some numbers that are simple in decimal become repeating fractions, leading to small precision errors