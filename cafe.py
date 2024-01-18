menu = ['chicken', 'toast', 'coleslaw', 'sandwich'] # list holds menu items

stock = {'chicken': 200,   # stock dictionary which can be access by the items in the menu list
         'toast': 120,
         'coleslaw': 80,
         'sandwich': 110}

price = {'chicken': 5,   # price dictionary which can be access by the items in the menu list
         'toast': 4,
         'coleslaw': 2,
         'sandwich': 3}

for count, item in enumerate(menu, 1):
    total_per_item = stock[item] * price[item]
    print(f"{count}: {item} {stock[item]} {price[item]} = £{total_per_item}")

total_stock = 0
num = 0

print("*" * 90)
for item in menu: #loop through the menu list 
    total_per_item = stock[item] * price[item] #access the values from the stock and price by the keys in menu items and calculate
    num += 1
    print(f"{num}. {item.upper()} --- Stocks: {stock[item]}pcs --- Price/piece: {price[item]}£ --- Total {item.upper()} amount: {total_per_item}£")
    total_stock += total_per_item
print()
print(f"TOTAL STOCK WORTH: {total_stock}")
print("*" * 90)