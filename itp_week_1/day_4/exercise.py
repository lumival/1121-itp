# ITP Week 1 Day 4 Exercise


# Dictionary Loop

inventory = {
    "soda_cans": 45,
    "chips": 12,
    "sandwiches": 34,
    "candy": 1
}

# SCENARIO: A person came in and bought one of everything!

for item, value in inventory.items():
    # decrement item by using an assignment operator (Day 2 Lecture line #130)
    inventory.update({item: value - 1})
    # NOTE: recall that item represents the key of the key:value pair
print(inventory)
# SCENARIO: REMOVE ANY 0 ITEMS

for item in inventory:
    # use an if statement to check if the value is 0 and then remove it
    if inventory.values() == 0:
        inventory.pop(item)
        
print(inventory)