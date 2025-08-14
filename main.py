catalog = {
    "apple": 3.50,
    "banana": 2.00,
    "bread": 12.00,
    "milk": 9.50
}

cart = {}

# Discount rule: Buy 3 get 1 free for bananas
discount_item = "banana"
discount_buy = 3
discount_free = 1

while True:
    print("\n1. Show Catalog")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Update Quantity")
    print("5. Remove from Cart")
    print("6. Checkout")
    print("7. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("\n--- PRODUCT CATALOG ---")
        for item, price in catalog.items():
            print(f"{item} - GHS {price:.2f}")
        print(f"Special: Buy {discount_buy} get {discount_free} free on {discount_item}")

    elif choice == "2":
        item = input("Enter product name: ").lower()
        if item in catalog:
            qty = int(input("Enter quantity: "))
            if item in cart:
                cart[item] += qty
            else:
                cart[item] = qty
            print(f"{qty} x {item} added to cart.")
        else:
            print("Item not found in catalog.")

    elif choice == "3":
        if not cart:
            print("Cart is empty.")
        else:
            total = 0
            print("\n--- YOUR CART ---")
            for item, qty in cart.items():
                price = catalog[item] * qty

                # Apply discount
                if item == discount_item and qty >= discount_buy:
                    free_items = (qty // (discount_buy + discount_free)) * discount_free
                    price -= free_items * catalog[item]
                    print(f"{item} x {qty} (includes {free_items} free) = GHS {price:.2f}")
                else:
                    print(f"{item} x {qty} = GHS {price:.2f}")

                total += price
            print(f"Total: GHS {total:.2f}")

    elif choice == "4":
        item = input("Enter product name to update: ").lower()
        if item in cart:
            qty = int(input("Enter new quantity: "))
            if qty > 0:
                cart[item] = qty
                print(f"{item} quantity updated to {qty}.")
            else:
                del cart[item]
                print(f"{item} removed from cart.")
        else:
            print("Item not in cart.")

    elif choice == "5":
        item = input("Enter product name to remove: ").lower()
        if item in cart:
            del cart[item]
            print(f"{item} removed from cart.")
        else:
            print("Item not in cart.")

    elif choice == "6":
        if not cart:
            print("Cart is empty.")
        else:
            total = 0
            print("\n--- INVOICE ---")
            for item, qty in cart.items():
                price = catalog[item] * qty

                # Apply discount at checkout
                if item == discount_item and qty >= discount_buy:
                    free_items = (qty // (discount_buy + discount_free)) * discount_free
                    price -= free_items * catalog[item]
                    print(f"{item} x {qty} (includes {free_items} free) = GHS {price:.2f}")
                else:
                    print(f"{item} x {qty} = GHS {price:.2f}")

                total += price
            print(f"TOTAL: GHS {total:.2f}")
            print("Thank you for shopping!")
            cart.clear()
            break

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
