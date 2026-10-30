list = []
item = ""
entry1 = 0
final = 0
entry2 = 1

while True:
    try:
        item = input("Enter item price (Q to quit): ")
        if item.lower() == "q":
            break
        else:
            item = float(item)
            if item > -1:
                list.append(item)
            else:
                print("Invalid price.")
    except ValueError:
        print("Invalid price!")
    finally:
        print("Entry processed.")
    final += item
    entry1 += 1

print(f"Items purchased: {entry1}")
print(f"Total: {final}")
for items in list:
    print(f"Purchase {entry2}: {items}")
    entry2 += 1