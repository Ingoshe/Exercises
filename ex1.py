# Write a program that takes your name as input and prints a personalized greeting along with a calculation of your birth year.
# input

name = input("Enter your name: ")
birth_year = int(input("Birth year: "))
current_year = 2025
age = int(current_year - birth_year)

print(f"Servus {name}, {age}.")
