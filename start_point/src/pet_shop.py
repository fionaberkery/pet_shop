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

#8
def get_pets_by_breed(shop, breed_of_animal):
    number_of_breed = 0
    for pet in shop["pets"]:
        if pet["breed"] == breed_of_animal:
           number_of_breed += 1 
    return number_of_breed
        
#9


#10
def find_pet_by_name(shop, pets_name):
    for pet in shop["pets"]:
        if pet["name"] == pets_name:
            return pet 





