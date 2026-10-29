list = []
try:
    item = int(input("Enter item price (Q to quit): "))
except ValueError:
    print("Invalid price!")
finally:
    print("Entry processed.")