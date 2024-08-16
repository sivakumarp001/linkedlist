stack = []
prices = []
total = 0

while True:
    print("\nSupermarket Basket Application")
    print("1. Add item")
    print("2. Remove item")
    print("3. View basket")
    print("4. Checkout")
   
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item = input("Enter the name of the item to add: ")
        price = float(input(f"Enter the price of {item}: Rs "))
        stack.append(item)
        prices.append(price)
        print(f"{item} added to the basket at Rs {price}.")

    elif choice == '2':
        if len(stack) == 0:
            print("The basket is empty. No item to remove.")
        else:
            removed_item = stack.pop()
            removed_price = prices.pop()
            print(f"{removed_item} removed from the basket (Rs {removed_price}).")

    elif choice == '3':
        if len(stack) == 0:
            print("The basket is empty.")
        else:
            print("Items in the basket:")
            for item in reversed(stack):
                print(item)

    elif choice == '4':
        if len(stack) == 0:
            print("The basket is empty. Nothing to checkout.")
        else:
            print("Checking out items in the basket:")
            total = 0
            while len(stack) > 0:
                item = stack.pop()
                price = prices.pop()
                total += price
                print(f"Checked out {item} at Rs {price}.")
            print(f"All items checked out. Your total is: Rs {total}")


    else:
        print("Invalid choice. Please try again.")