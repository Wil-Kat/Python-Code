# functions for florist_control

import os
import csv

# get florist list for selection
def get_flor_list(file_name='florist_list.csv'):
    with open(file_name, 'r', newline='') as file:
        reader = list(csv.reader(file))
        return reader[1:]

# make selection of florists to append
def select_flor(florist):
    print('\nFlorists: ')
    for index, row in enumerate(florist):
        print(f'{index + 1}) {row[0]}')
    try:
        choice = int(input('Select florist by entering the number: '))
        if 1 <= choice <= len(florist):
            return florist[choice - 1]
        else:
            print('Your choice was invalid')
            return select_flor()
    except ValueError:
        print('Your choice was invalid')
        return select_flor()
    
def delete_flor(file_name='florist_list.csv'):
    with open(file_name, 'r', newline='') as file:
        reader = list(csv.reader(file))
        headers = reader[0]
        florists = reader[1:]
    
    if not florists:
        print('There are no floral shops to delete.')
        return
    
    print('\nFlorists: ')
    for index, row in enumerate(florists):
        print(f'{index + 1}) {row[0]} - {row[1]} - {row[2]} Delivers: {row[3]}')

    while True:
            try:
                selection = int(input('Select the number for the shop to delete: ').strip())
                if 1 <= selection <= len(florists):
                    deleted = florists.pop(selection - 1)
                    print(f"Deleted florist: {deleted[0]}")
                    break
                else:
                    print('Your selection was invalid. Try again.')
            except ValueError:
                print('Invalid input. Please enter a number.')

    with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(florists)
    
# create file names for sale items for each florist
def get_sale_filename(florist_name):
    return f'{florist_name.replace(' ', '_').lower()}_sale.csv'

# delete a sale list for a floral shop
def delete_sale_list():
    florists = get_flor_list()
    selected = select_flor(florists)

    if selected:
        florist_name = selected[0]
        sale_file = get_sale_filename(florist_name)

        if os.path.exists(sale_file):
            confirm = input(f"Are you sure you want to delete the sale list '{sale_file}'? (y/n): ").lower()
            if confirm == 'y':
                os.remove(sale_file)
                print(f"Sale list '{sale_file}' has been deleted.")
            else:
                print("Sale list not deleted.")
        else:
            print(f"No sale list found for '{florist_name}'.")

# create file names for sale items for each florist
def get_sale_filename(florist_name):
    return f'{florist_name.replace(' ', '_').lower()}_sale.csv'

# add sale items to the selected floral shop
def add_sale_item(sale_file):
    item = input("Enter item name: ")
    desc = input("Enter description: ")
    price = input("Enter price: ")
    with open(sale_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([item, desc, price])
        print(f"Item '{item}' added to {sale_file}.")

# delete a sale item from a sale list
def delete_sale_item():
    florists = get_flor_list()
    selected = select_flor(florists)

    if selected:
        florist_name = selected[0]
        sale_file = get_sale_filename(florist_name)

        if not os.path.exists(sale_file):
            print(f"No sale list found for '{florist_name}'.")
            return

        with open(sale_file, 'r', newline='') as file:
            reader = list(csv.reader(file))
            headers = reader[0]
            items = reader[1:]

        if not items:
            print("No items in the sale list to delete.")
            return

        print(f"\nItems in {florist_name}'s sale list:")
        for index, row in enumerate(items):
            print(f"{index + 1}) {row[0]} - {row[1]} - ${row[2]}")

        try:
            selection = int(input("Select the number of the item to delete: "))
            if 1 <= selection <= len(items):
                deleted = items.pop(selection - 1)
                print(f"Deleted item: {deleted[0]}")
            else:
                print("Invalid selection.")
                return
        except ValueError:
            print("Invalid input.")
            return

        with open(sale_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(items)
        print("Sale list updated.")

# amend items in the sales file for select florist
def amend_sale_item(sale_file):
    if not os.path.exists(sale_file):
        print("Sale file does not exist.")
        return amend_sale_item()

    with open(sale_file, 'r', newline='') as file:
        reader = list(csv.reader(file))
        headers = reader[0]
        items = reader[1:]

    if not items:
        print("No items in the menu to amend.")
        return

    print("\nMenu Items:")
    for index, row in enumerate(items):
        print(f"{index + 1}) {row[0]} - {row[1]} - ${row[2]}")

    try:
        selection = int(input("Select an item to amend by number: "))
        if 1 <= selection <= len(items):
            print("Fields: 1) Item Name  2) Description  3) Price")
            field = input("Which field do you want to amend (1-3)? ")
            if field in ['1', '2', '3']:
                new_value = input("Enter new value: ")
                items[selection - 1][int(field) - 1] = new_value
                print("Item updated.")
            else:
                print("Invalid field selection.")
                return amend_sale_item()
        else:
            print("Invalid item selection.")
            return amend_sale_item()
    except ValueError:
        print("Invalid input.")

    with open(sale_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(items)
