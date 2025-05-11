# Take a user through creating florist lists and sales menus

import os
import csv
import Florist_Functions

# create florist list if not exist
try:
    with open('florist_list.csv', 'x') as file:
        pass
    print('File "florist_list.csv" has been created.')
except FileExistsError:
    print('File named "florist_list.csv" already exists')

# add headers to the florist list if don't already exit
headers = ['Florist Name','Address', 'Phone Number', 'Delivers']
with open('florist_list.csv', 'r', newline='') as file:
    if not file.readline():
        with open('florist_list.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
        print('Headers have been added to the file.')
    else:
        print("Headers are already present.")

# allow user to add new florist to the list
response = input("Do you want to add a new floral shop? (y/n): ").lower()
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

# allow user to create a sale list for each florist
response = input("Do you want to creat a sale list for a floral shop? (y/n): ").lower()
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

# allow a user to add a menu item or modify a menu item
response = input("Do you want to add to or amend a sale list? (y/n): ").lower()
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