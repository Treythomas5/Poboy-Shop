item_menu = {
    print("1." "catfish poboy $14.95"),
    print("2." "roast beef poboy $13.95"),
    print("3." "sausge poboy $12.95"),
    print("4." "gumbo $4.95"),
}
user_order = {
    "2. roast beef poboy"
}
user_order = input("What would you like to order? Type the appropriate number of the menu item:")
if(user_order == "2"):
    print("roast beef poboy $13.95")
else:
    print("Sorry you can only order one item")
sales_tax = 0.0945
tax = 13.95 * 0.0945
final_cost = 13.95 + tax
if(user_order == "2"):
    print(f'final cost is ${final_cost:.2f}')

