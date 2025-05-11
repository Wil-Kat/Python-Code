# allow user to delete floral shops, sale lists, or list items

import os
import csv
import Florist_Functions

print('Welcome to the florist delete menu please select you action: ')

# user selection 
user_choice = str(input(' 1) Delete a floral shop\n 2) Delete a sale list\n 3) Delete an item in a sale list \n 4) No actions, exit the program \n'))

if user_choice == '1':
    response = input("You want to remove a floral shop from the list, is that correct? (y/n): ").lower()
    if response == 'y':
        Florist_Functions.delete_flor()
    else:
        print('No floral shops were deleted.')

elif user_choice == '2':
    response = input("You want to remove a sake list, is that correct? (y/n): ").lower()
    if response == 'y':
        Florist_Functions.delete_sale_list()
    else:
        print('No sale lists were deleted.')

elif user_choice == '3':
    response = input("You want to remove an itemfrom a sale list, is that correct? (y/n): ").lower()
    if response == 'y':
        Florist_Functions.delete_sale_item()
    else:
        print('No sale lists were deleted.')
else:
    print('No actions were selected. Good bye.')
    exit()