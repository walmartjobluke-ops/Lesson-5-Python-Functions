#Objective: The aim of this assignment is to create a program that helps users make a shopping list.

#Task 1: Write a function that lets the user add items to a list.

#Task 2: Include a function to remove items from the list.

#Task 3: Add a function that prints out the entire list in a formatted way.

#Note: The goal of this is to be a program. The recommendation is to use a while loop that will allow the user to continue to add, remove, and print off their shopping list until they decide to "quit", also known as breaking the loop.

shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(f'Added: {item}')

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'Removed: {item}')
    else:
        print(f'Item not found: {item}')

def print_list():
    print("Shopping List:")
    for item in shopping_list:
        print(f'- {item}')

def main():
    while True:
        action = input("Enter 'add', 'remove', 'print', or 'quit': ").strip().lower()
        if action == 'add':
            item = input("Enter the item to add: ")
            add_item(item)
        elif action == 'remove':
            item = input("Enter the item to remove: ")
            remove_item(item)
        elif action == 'print':
            print_list()
        elif action == 'quit':
            print("Exiting the program.")
            break
        else:
            print("Invalid action. Please try again.")
if __name__ == "__main__":
    main()