#Code to impliment Inventry Checker(it can add,update and check the inventry)
inventory = {"apples": 50, "bananas": 30, "oranges": 20}

while True:
    action = input("Enter action (add/update/check/exit): ").lower()
    if action == "exit":
        break
    elif action == "add":
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity to add: "))
        inventory[item] = inventory.get(item, 0) + quantity
        print(f"{item} updated. Current quantity: {inventory[item]}")
    elif action == "update":
        item = input("Enter item name: ")
        quantity = int(input("Enter new quantity: "))
        inventory[item] = quantity
        print(f"{item} updated. Current quantity: {inventory[item]}")
    elif action == "check":
        item = input("Enter item name: ")
        print(f"{item}: {inventory.get(item, 'Not in inventory')}")
    else:
        print("Invalid action.")
