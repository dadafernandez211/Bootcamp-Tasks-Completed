import math

# 2 selection of calculator, either investment or bond
# capitalization matters, use OR operator (investment or bond)
# investment create variables ff
# deposit, interest rate, num of years
# then ask user simple or compound, store in var "interest"
# then execute the formula given on each calculation choices

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan \n")
calculation = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

'''program must recognize the word(investment/bond) even though the letters are in different cases as soon as it has 
correct spelling as stated in the choices'''

if calculation.upper() == "investment" or calculation.lower() == "investment":
    calculation = "Investment"
    deposit = int(input("Enter deposit amount                :  "))
    int_rate = float(input("Enter interest rate                 :  ")) # float is used cause rates could be with decimals
    int_rate = int_rate / 100       # this formula will make the interest rate convert percentage value with decimal
    years = int(input("Enter number of years               :  "))
    interest = input("Interest type 'simple' or 'compound': ")

    if interest.upper() == "simple" or interest.lower() == "simple":
        amount_earn = deposit * (1 + int_rate * years)
        interest = "Simple Interest"
        print("-" * 50)
        print(f"CALCULATION TYPE          :   {calculation}")
        print(f"TYPE OF INTEREST RATE     :   {interest}")
        print(f"DEPOSIT AMOUNT            :   {deposit}")
        print(f"INTEREST RATE             :   {int(int_rate * 100)}%")
        print(f"YEARS OF INVESTING        :   {years}")
        print(f"AMOUNT TO EARN            :   {int(amount_earn)}")
        print("-" * 50)
    elif interest.upper() == "compound" or interest.lower() == "compound":
        amount_earn = deposit * math.pow((1 + int_rate), years)
        interest = "Compound Interest"
        print("-" * 50)
        print(f"CALCULATION TYPE          :   {calculation}")
        print(f"TYPE OF INTEREST RATE     :   {interest}")
        print(f"DEPOSIT AMOUNT            :   {deposit}")
        print(f"INTEREST RATE             :   {int(int_rate * 100)}%")
        print(f"YEARS OF INVESTING        :   {years}")
        print(f"AMOUNT TO EARN            :   {int(amount_earn)}")
        print("-" * 50)
    else:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("You type wrong choice or you misspelled ! Please try again")

# if user typed in bond, below block of code will be executed
elif calculation.upper() == "bond" or calculation.lower() == "bond":
    calculation = "Bond"
    house_value = int(input("Value of the house      : "))
    int_rate = float(input("Enter interest rate     : "))
    int_rate = int_rate / 100
    interest_rate = int_rate / 12
    num_months = int(input("Number of months to pay : "))
    repayment = (interest_rate * house_value) / (1 - (1 + interest_rate) ** (- num_months))
    print("-" * 50)
    print(f"CALCULATION TYPE           :   {calculation}")
    print(f"HOUSE VALUE                :   {house_value}")
    print(f"INTEREST RATE              :   {int(int_rate * 100)}%")
    print(f"NUMBER OF MONTHS TO REPAY  :   {num_months}")
    print(f"MONTHLY PAYMENT            :   {int(repayment)}")
    print("-" * 50)
else:
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("You type wrong choice or you misspelled ! Please try again")
