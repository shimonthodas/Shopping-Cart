def shopping_cart():

    # Create empty lists to store the names and prices of items
    item_names = []
    item_prices = []

    while True:
        # Display the menu options
        print("Welcome to the Shopping Cart Program!")
        print("Please select one of the following:")
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")

        # Get the user's choice
        choice = input("Please enter an action: ")

        # Add a new item to the cart
        if choice == "1":
            name = input("What item would you like to add? ")
            price = input(f"What is the price of '{name}'? ")
            item_names.append(name)
            item_prices.append(price)
            print(f"'{name}' has been added to the cart.")

        # Display the contents of the cart
        elif choice == "2":
            print("The contents of the shopping cart are:")
            for i in range(len(item_names)):
                print(f"{i + 1}. {item_names[i]} - ${item_prices[i]}")

        # Remove an item from the cart
        elif choice == "3":
            index = input("Which item would you like to remove? ")
            try:
                index = int(index) - 1
                if index < 0 or index >= len(item_names):
                    raise ValueError("Invalid item number")
                item_names.pop(index)
                item_prices.pop(index)
                print("Item removed.")
            except ValueError as e:
                print(f"Sorry, {e}.")

        # Compute the total price of the items in the cart
        elif choice == "4":
            total = sum([float(price) for price in item_prices])
            print(f"The total price of the items in the shopping cart is ${total:.2f}")

        # Quit the program
        elif choice == "5":
            print("Thank you for using the Shopping Cart Program!")
            break

        # Invalid choice
        else:
            print("Invalid choice. Please try again.")
