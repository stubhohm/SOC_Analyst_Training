"""
The project is a version of python written in vs code. I have manually imported copys of allow_list.txt to this file
The goal of the python program is to take a list of addresses, and modify it to remove any banned addresses from the list
The updated list is stored in a new location so you can see that the function does what it is intended to do and can be repeated.
"""
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
file_path = "Python_Scripts//allow_list.txt"
after_file_path = "Python_Scripts//updated_allow_list.txt"

# open the file in the desinaged file path
with open(file_path, "r") as file:
    # read and split the file
    ip_addresses = file.read().split()

# iterate through the ip_address list and check for any in the remove_list
for element in ip_addresses:
    if element in remove_list:
        ip_addresses.remove(element)

# Return list to a string to rewrite to a new file
ip_addresses = "\n".join(ip_addresses)

with open(after_file_path, "w") as file:
    file.write(ip_addresses)