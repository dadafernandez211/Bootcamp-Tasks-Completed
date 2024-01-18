# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"
# syntax error 1.)No double quotation marks, when declaring string to a variable it has to have double quotation marks enclosed to string

animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"
# logical error 1.) Variables inside this string is ignored, f-string will make the variables activated by putting "f" before the string
# logical error 2.) Wrong variable placement, variable named "number_of_teeth" must be on third place and var named "animal_type" in on 2nd

print(full_spec)
# syntax error 1.)Missing open & close parenthesis in print statement