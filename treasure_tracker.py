# Using dictionaries help organize everything because you can keep track of everything cause it's all put into the same place but spreaded out
# The big Challenge was figuring out why my code wasn't working.. Turns out I put [] for the inventory and not {}. So both treasures and inventory had []
# A good way to expand this assignment is to add certain items you can add to your treasure instead of being able to input anything into the thing and it gives you that whatever you typed

# This creates an empty list for discovered treasures.
# This creates an empty dictionary to track each item’s quantity and value.
treasures = []
inventory = {}

# This has a loop to continuously ask the user for input until they decide to quit.
while True:
    print("\nChoose an option")
    print("1. Add a treasure")
    print("2. Update inventory")
    print("3. Display inventory")
    print("4. Quit")
    choice = input("Enter your choice: ")

    # This Asks the user for the name of the treasure, its quantity, and value.
    # This Appends(or adds) the treasure to the list and update the dictionary
    if choice == "1":
        name = input("Enter the name of the treasure: ")
        quantity = int(input("Enter the quantity: "))
        value = int(input("Enter the value per unit: "))
        treasures.append(name)
        inventory[name] = {"quantity": quantity, "value_per_unit": value}
        print(f"{name} added to your inventory.")
        
    # This allows users to update the quantity or value of existing items
    elif choice == "2":
        name = input("Enter the name of the treasure to update: ")
        if name in inventory:
            new_quantity = int(input("Enter the new quantity: "))
            new_value = int(input("Enter the new value per unit: "))
            inventory[name]["quantity"] = new_quantity
            inventory[name]["value_per_unit"] = new_value
            print(f"{name} updated in your inventory")
        else:
            print("Treasure not found in your inventory")

    # Display Inventory: This prints out all items in the dictionary in a readable format.
    elif choice == "3":
        for item, details in inventory.items():
            print(f"Name: {item}, Quantity: {details['quantity']} per Unit: {details['value_per_unit']}")

    # Exiting: Allow the user to quit the loop when they’re done
    elif choice == "4":
        print("Good luck on your quest!")
        break
    else:
        print("Invalid choice. Please try again")

