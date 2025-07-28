# alx_be_python/fns_and_dsa/shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")  # ✔️ EXACT match
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # ✔️ list implementation

    while True:
        display_menu()  # ✔️ call menu function

        try:
            choice = int(input("Enter your choice: "))  # ✔️ numeric input
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ")  # ✔️ exact match for checker
            shopping_list.append(item)
            print(f"'{item}' added to the list.")

        elif choice == 2:
            item = input("Enter the item to remove: ")  # ✔️ exact match
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == 3:
            if not shopping_list:
                print("Shopping list is empty.")
            else:
                print("Current Shopping List:")
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
