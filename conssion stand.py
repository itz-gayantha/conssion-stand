menu ={"popcorn": 1200,
       "soda":600,
       "bites":450,
       "water":70,
       "candy":12,
       "potato_cips":300}
total = 0
cart = []
print("------------MENU------------")
items = menu.items()
for key,value in items:
    print(f"{key:15}:Rs.{value:.2f}")
while True:
    s_item =input("select item you want (Q to quit): ").upper()
    if s_item == "Q":
        break
    elif menu.get(s_item.lower()) is not None:
        cart.append(s_item.lower())
        total += menu.get(s_item.lower())
    else:
        print("invalid item")
    
print("------------------------------------------")
print("                YOUR CART                 ")
for item in cart:
    print(item,end=", ")
print()  
print(f"total cost is Rs.{total:.2f}")
print("------------------------------------------")