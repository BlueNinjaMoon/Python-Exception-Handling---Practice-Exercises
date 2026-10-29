prices = {"pizza": 12, "burger": 8, "fries": 4, "soda": 2}
try:
    item = input("Enter a food item: ").lower().strip()
    print(f"The food item, {item}, costs ${prices[item]}.")
except KeyError:
    print("Sorry, that item is not on the menu.")