# Allow user to select functions such as add a shop or add an item

import os
import csv
import Florist_Functions

print('Welcome to the florist addition menu please select you action: ')

# user selection 
user_choice = str(input(' 1) Add a new floral shop\n 2) Add a new sale list\n 3) Add to or modify a sale list \n 4) No actions, exit the program \n'))

if user_choice == '1':
    response = input("You want to add a new floral shop, is that correct? (y/n): ").lower()
    if response == 'y':
        name = input("Enter florist name: ")
        address = input("Enter address: ")
        phone = input("Enter phone number: ")
        deliver = input("Does the shop offer delivery? (Yes/No): ")

        with open ('florist_list.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, address, phone, deliver])

    else:
        print('No floral shops added.')

elif user_choice == '2':
    # allow user to create a sale list for each florist
    response = input("You want to creat a sale list for a floral shop, is that correct? (y/n): ").lower()
    if response == 'y':
        florist = Florist_Functions.get_flor_list()
        selected = Florist_Functions.select_flor(florist)

        if selected:
            selected_name = selected[0]
            sale_filename = Florist_Functions.get_sale_filename(selected_name)

            if os.path.exists(sale_filename):
                print(f"Sale list already exists: '{sale_filename}'")
            else:
                with open(sale_filename, 'w', newline='') as sale_file:
                    writer = csv.writer(sale_file)
                    writer.writerow(['Item Name', 'Description', 'Price'])
                print(f"Sale file '{sale_filename}' created.")
    else:
        print("No sale list was created.")

elif user_choice == '3':
# allow a user to add a menu item or modify a menu item
    response = input("You want to add to or amend a sale list, is that correct? (y/n): ").lower()
    if response == 'y':
        action = input("Type 'add' to add a sale item or 'amend' to modify one: ").lower()
        florist_list = Florist_Functions.get_flor_list()
        selected = Florist_Functions.select_flor(florist_list)

        if selected:
            florist_name = selected[0]
            sale_file = Florist_Functions.get_sale_filename(florist_name)

            if not os.path.exists(sale_file):
                print(f"Sale list does not exist for '{florist_name}'. Creating one now.")
                with open(sale_file, 'x', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Item Name', 'Description', 'Price'])

            if action == 'add':
                while True:
                    Florist_Functions.add_sale_item(sale_file)
                    again = input("Add another item? (y/n): ").lower()
                    if again != 'y':
                        print("Finished adding items.")
                        break  
            elif action == 'amend':
                Florist_Functions.amend_sale_item(sale_file)
            else:
                print("Unknown action. Please type 'add' or 'amend'.")
    else:
        print("No sale changes made.")

else:
    print('Have a nice day.')
    exit()