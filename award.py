print("=" * 44)
print("==" + "ENTER THE TIME FINISHED FOR THE 3 EVENTS==")

# 3 variables created to store 3 events value

swimming = int(input("Swimming: "))
cycling = int(input("Cycling: "))
running = int(input("Running: "))
total = swimming + cycling + running
print(" ")

if total <= 100:
    print(f"Your total time taken to complete the triathlon is {total} minutes.")
    print("::: You got Provincial Colours :::")
elif total <= 105:
    print(f"Your total time taken to complete the triathlon is {total} minutes.")
    print("::: You got Provincial Half Colours :::")
elif total <= 110:
    print(f"Your total time taken to complete the triathlon is {total} minutes.")
    print("::: You got Provincial Scroll :::")
else:
    print(f"Your total time taken to complete the triathlon is {total} minutes.")
    print("::: No award :::")
print("=" * 44)
