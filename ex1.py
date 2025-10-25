# Write a program that takes your name as input and prints a personalized greeting along with a calculation of your birth year.
# input

name = input("Enter your name: ")
birth_year = int(input("Birth year: "))
age = int(2025 - birth_year)

print(f"Servus {name}, {age}.")