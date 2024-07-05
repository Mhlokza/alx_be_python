def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(item_name,shopping_list):
    shopping_list.append(item_name)

def remove_item(item_name,shopping_list):
    shopping_list.remove(item_name)

def display_shopping_list(shopping_list):
    return shopping_list
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            user_input = input("enter the item to add: ")
            add_item(item_name = user_input,shopping_list = shopping_list)

        elif choice == '2':
            # Prompt for and remove an item
            user_input = input("enter the item to be removed: ")
            remove_item(item_name=user_input,shopping_list=shopping_list)

        elif choice == '3':
            # Display the shopping list
            print(display_shopping_list(shopping_list))

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

