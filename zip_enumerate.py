inventory_names = ["Screws", "Wheels", "Metal parts", "Rubber bits", "Screwdrivers", "Woods"]
inventory_numbers = [43, 23, 88, 32, 5, 103]

for index, inventory_tuple in enumerate(zip(inventory_names, inventory_numbers)):
    print(f"{inventory_tuple[0]} id:[{index}] - inventory: {inventory_tuple[1]}")