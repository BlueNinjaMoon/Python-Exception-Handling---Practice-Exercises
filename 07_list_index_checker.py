animals = ["Dog", "Cat", "Rabbit", "Duck", "Horse"]
try:
    index = int(input("Enter an index(0-4): "))
    print(animals[index])
except ValueError:
    print("Has to be a number.")
except IndexError:
    print("Index out of range.")