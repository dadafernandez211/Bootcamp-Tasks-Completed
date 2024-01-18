"""
*
**
***
****
*****
****
***
**
*
"""

for i in range(10):  # iteration for pattern's length
    if i <= 5:       # true on first 5 iteration
        print("*" * i)
        x = i        # copy the value of 5, and use it in else block
    else:
        x -= 1       # decrease by 1 every iteration
        print("*" * x)
