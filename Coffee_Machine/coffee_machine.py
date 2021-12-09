from menu import MENU, resources

# ==== Initial variable ====
switch_on = True
account = 0
coffee = resources['coffee']
milk = resources['milk']
water = resources['water']

# ==== MENU BLOCK ====
# --- Ingredients of the menu ---
def ingredients(menu_name):
    ''' Menu ingredients list '''
    ingredients = {
        'water' : MENU[menu_name]['ingredients']['water'],
        'milk'  : MENU[menu_name]['ingredients']['milk'],
        'coffee': MENU[menu_name]['ingredients']['coffee']
    }
    return ingredients
# ==== MENU BLOCK END ====

# ==== INVENTORY BLOCKS ====
# --- Inventory ---
def inventory(water, milk, coffee):
    '''Make dictionary based on how much resources left '''
    inventory = {
        'water' : water,
        'milk'  : milk,
        'coffee': coffee,        
    }
    return inventory

# --- Checking Inventory ---
def check_inventory(menu_name, inventory):
    ''' Check if inventory sufficient to make an order '''
    menu_ingredient = ingredients(menu_name)
    inventory_stock = inventory
    for item in menu_ingredient:
        if menu_ingredient[item] > inventory_stock[item]:
            return False
    return True

# ---- Inventory update ----
def resource_used(coffee, milk, water, menu_name): 
    ''' Reduce resources with ingredients '''
    menu_ingredient = ingredients(menu_name)
    coffee -= menu_ingredient['coffee']           
    milk -= menu_ingredient['milk']               
    water -= menu_ingredient['water']             
    return coffee, milk, water

def resources_not_enough(inventory, cash):
    ''' When the resources in inventory is not enough'''
    print("The resources is not enough. The machine must be refilled before use.")
    reporting = input("Would you like to prin the report? yes or no?  > ").lower()
    if reporting == 'yes' or reporting == 'y':
        report(inventory, cash)
    else:
        print("Machine off.")
# ==== INVENTORY BLOCKS END ====

# ==== REPORT AND PAYMENT BLOCKS ====
# --- Report ---
def report(inventory, cash):
    ''' Return inventory report '''
    print("Inventory list:")                  
    print(f"Coffee: {inventory['coffee']} g")   
    print(f"Milk: {inventory['milk']} mL")       
    print(f"Water: {inventory['water']} mL")     
    print(f"Profit: $ {cash}")                  

# --- Menu price ---
def pricing(menu):
    ''' Pricing menu '''
    price = MENU[menu]['cost']
    return price

# ---Accept payment ---
def payment(cost, profit):
    '''Counting exchange'''
    while True:
        print(f"The price is $ {cost}.")
        money = float(input("Please enter your payment: > $ ")) 
        money -= cost  
        profit += cost 
        if money > 0:
            print(f"Your exchange is $ {money}.")   
            break
        elif money == 0:
            print("Payment accepted.")    
            break
        else:
            print("Your money is not enough.")
            continue
    return profit    
# ==== REPORT AND PAYMENT BLOCKS END ====

    
# ==== MACHINE BLOCK =====
while switch_on:
    # ---- Greetings and show options ----
    print("Welcome. To using the machine, please choose one of these numbers:") 
    print("1. Espresso\n2. Latte\n3. Cappuccino\n4. REPORT MODE\n5. OFF MODE\n") 
    numbers = input(">  ") 

    # ---- Checking user input ----
    # ---- If input is in options ----
    if numbers in ['1', '2', '3', '4', '5']: 
        if numbers == '1':
            if check_inventory('espresso', inventory(water, milk, coffee)):
                account = payment(pricing('espresso'), account) 
                coffee, milk, water = resource_used(coffee, milk, water, 'espresso') 
                print("Here is your coffee.\n")   
            else:
                print("Sorry, not enough resource. We will give your money back.")
                account -= pricing('espresso')
                resources_not_enough(inventory(water, milk, coffee), account)
                switch_on = False
                break
        elif numbers == '2':
            if check_inventory('latte', inventory(water, milk, coffee)):
                account = payment(pricing('latte'), account) 
                coffee, milk, water = resource_used(coffee, milk, water, 'latte')
                print("Here is your coffee.\n")                
            else:
                print("Sorry, not enough resource. We will give your money back.")
                account -= pricing('latte')
                resources_not_enough(inventory(water, milk, coffee), account)            
                switch_on = False
                break
        elif numbers == '3':
            if check_inventory('cappuccino', inventory(water, milk, coffee)):
                account = payment(pricing('cappuccino'), account) 
                coffee, milk, water = resource_used(coffee, milk, water, 'cappuccino')
                print("Here is your coffee.\n")                
            else:
                print("Sorry, not enough resource. We will give your money back.")
                account -= pricing('cappuccino')
                resources_not_enough(inventory(water, milk, coffee), account)
                switch_on = False
                break
        elif numbers == '4':
            # ---- Show latest inventory and profit ----
            report(inventory(water, milk, coffee), account) 
        elif numbers == '5':
            # ---- Kill the machine ----
            print('Machine off.') 
            switch_on = False 
            break

    # ---- If input is NOT in options ----
    else:
        print("Please choose one of the numbers.") 
        continue
    
    # ---- Continue or no ----
    while True:
        new_order = input("Would you like to continue? yes or no?  > ").lower()
        if new_order == 'y' or new_order == 'yes':
            break
        if new_order == 'n' or new_order == 'no':
            report(inventory(water, milk, coffee), account)
            print('Machine off.')
            switch_on = False
            break
        else:
            print("Please enter only 'yes' or 'no'.")
# ==== MACHINE BLOCK END ====
