from dest.actions import add_destinations, print_destinations
from storage.loadsave import load,save
from icecream import ic

my_destinations = []

def menu():
    load()
    ic(my_destinations)
    while True:
        ic("1 - Add")
        ic("2 - List")
        ic("3 - Exit")
        selection = input("Your choice: ")
        if selection == '1':
            add_destinations(my_destinations)
        elif selection == '2':
            print_destinations(my_destinations)
        elif selection == '3':
            save()
            exit()
        else:
            print("Invalid choice, please select 1, 2, or 3.")

menu()