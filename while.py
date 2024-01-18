num = float(input("Enter a number: "))

"""float is being used for the instance that user entered a float 
then no error will occur
"""

count = 0     # this variable stores how many times the user entered a number
total = 0     # this variable will collect the sum of the numbers entered
average = 0   # this will store the formulated average of "total" divided by "count"

"""
Variable "total" collects or add all the numbers being entered and serves as
the dividend.
While user enter a number greater than -1, variable "count" keeps on adding 1,
and serves as a divisor to get the average 
"""

while num >= -1:
    count += 1
    total += num
    num = float(input("Enter a number: "))
    if num < 0:
        average = total / count
        print("-" * 30)
        print(f"Average is {average}")
        break  # break is to stop the while loop

