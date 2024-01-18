# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")
# syntax error 1.)Missing open & close parenthesis in strings
print("\n")
# syntax error 1.)Missing open & close parenthesis

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old"
# runtime error 1.)Using double equal sign is used only during conditional statement or looping, single equal sign is used on assigning value to a variable
# syntax error 1.) Indention is not necessary
age = 24
# runtime error 1.)Wrong casting from str to int, variable "age_Str" contains character so its not possible to convert to integer, instead, we can just simply assign a value of integer
# syntax error 1.) Indention is not necessary
print("I'm " + str(age) + " years old.")
# runtime error 1.)Wrong concatenation, when printing with integer value, it has to be cast to str.
# 2.)White space has to be added in and out "age" variable
# syntax error 1.) Indention is not necessary

# Variables declaring additional years and printing the total years of age
years_from_now = 3
#runtime error 1.)Assigning a number with double quotation marks reads as string, so any computation occurs with this variable will be an error
# syntax error 1.) Indention is not necessary
total_years = age + years_from_now
# syntax error 1.) Indention is not necessary

print("The total number of years: " + str(total_years))
# syntax error 1.) Missing open & close parenthesis in strings.
# runtime error 2.)Variable named "total_years" has to be cast to str when printing.
# 3.)White space has to be added before "total_years" variable

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (age * 12) + 42
# logical error 1.)Wrong formula to compute total months of 27 years and 6 months old. To compute correctly, current age (24years old) multiply to 12 months, then add 42 months which is equivalent to 3 years and 6 months)

print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")
# syntax error 1.)Missing open & close parenthesis.
# runtime error 2.)When printing, variable with int value has to be casted to str)

# HINT, 330 months is the correct answer