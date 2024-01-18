"""
Fast Restaurant ordering program with tax

1.ask menu
2.how many meals
3.ask the drinks (lemonade with extra charge)
4.back to menu (yes or no) if yes, back to 1,2,3,4
5.ask extras
6.ask in or out
7.calculate
"""

mea1_1 = 10
meal_2 = 11
meal_3 = 12
meal_4 = 13
choice = True

while choice:
    print("Choose your favorite meal \n 1.) Sandwich Combo - 10£\n 2.) Hotdog Combo - 11£ \n 3.) Chicken Combo - 12£ \n "
          "4.) Beef Combo - 13£")
    meal = input("Enter your choice: ")
    if meal == "1" or meal == "2" or meal == "3" or meal == "4":
        num_meals = int(input("How many meals: "))
        drinks = input("Drinks Choices \n 1.) ")
    else:
        print("You Entered Wrong Choice, Please try again")
















