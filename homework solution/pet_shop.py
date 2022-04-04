#1
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

#2
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

#3 and 4
def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

#5
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

#6
def increase_pets_sold(pet_shop, num_pets_sold):
    pet_shop["admin"]["pets_sold"] += num_pets_sold

#7
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

#8 and 9
def get_pets_by_breed(pet_shop, breed):
    found_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            found_pets.append(pet)

    return found_pets

#10 and 11
def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

#12 
def remove_pet_by_name(pet_shop, name):
    pet_to_delete = find_pet_by_name(pet_shop, name)
    pet_shop["pets"].remove(pet_to_delete)

#13
def add_pet_to_stock(pet_shop, pet):
    pet_shop["pets"].append(pet)

#14
def get_customer_cash(customer):
    return customer["cash"]

#15
def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

#16
def get_customer_pet_count(customer):
    return len(customer["pets"])

#17
def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

# optional 1 and 2
def customer_can_afford_pet(customer, pet):
    return customer["cash"] >= pet["price"]

# intergration
def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None and customer_can_afford_pet(customer, pet):
        remove_pet_by_name(pet_shop, pet["name"])
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        increase_pets_sold(pet_shop, 1)
