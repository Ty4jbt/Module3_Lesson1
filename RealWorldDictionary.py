# Task 1
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Adds the "Beverages" key to the dictionary with a dictionary as its value
restaurant_menu["Beverages"] = {"Soda": 2.50, "Juice": 3.00}

# Finds the "Steak" key on the "Main Course" dictionary and changes its value to 17.99
restaurant_menu["Main Course"]["Steak"] = 17.99

# Deletes the "Bruschetta" key from the "Starters" dictionary
del restaurant_menu["Starters"]["Bruschetta"]

print(restaurant_menu)
