# WRITE YOUR FUNCTIONS HERE

#1
def get_pet_shop_name(shop):
    return shop["name"]

#2    
def get_total_cash(shop):
    return shop["admin"]["total_cash"]

#3 and 4
def add_or_remove_cash(shop, amount):
    shop["admin"]["total_cash"] += amount

#5    
def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

#6
def increase_pets_sold(shop, number_of_pets):
    shop["admin"]["pets_sold"] += number_of_pets

#7
def get_stock_count(shop):
    stock = len(shop["pets"]) 
    return stock 

#8 and 9
def get_pets_by_breed(pet_shop, breed):
    pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            pets.append(pets)
    return pets 

#10 and 11
def find_pet_by_name(shop, pets_name):
    for pet in shop["pets"]:
        if pet["name"] == pets_name:
            return pet 

#12
def remove_pet_by_name(shop, pets_name):
    pet_to_delete = find_pet_by_name(shop, pets_name)
    shop["pets"].remove(pet_to_delete)
        
# 13
def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

#14
def get_customer_cash(customer):
    return customer["cash"]

#15
def remove_customer_cash(customer_no, cash_amount):
    customer_no["cash"] -= cash_amount

#16
def get_customer_pet_count(customer):
    return len(customer["pets"])

#17
def add_pet_to_customer(customer_name, new_pet):
   customer_name["pets"].append(new_pet) 

# optional 1 and 2 - (I did the first one, either work)
# def customer_can_afford_pet(customer_name, pet_to_buy):
#     if customer_name["cash"] >= 100:
#         return True 
#     else:
#         return False 
def customer_can_afford_pet(customer, pet):
    return customer["cash"] >= pet["price"]

# intergration 1
def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None and customer_can_afford_pet(customer, pet):
        remove_pet_by_name(pet_shop, pet["name"])
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        increase_pets_sold(pet_shop, 1)



   





    

    

    







