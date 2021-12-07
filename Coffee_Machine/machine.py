from menu import MENU, resources

# --- Machine Stocks ---
water_stock, milk_stock, coffee_stock = resources.values()

# --- First cash position ---
account = 0

# --- Default condition ---
machine_on = True
  

# --- Menu data ---
def menu_list(menu):
    '''Take data from dictionary into usable data'''
    the_menu = MENU[menu]
    ingredients = the_menu['ingredients']
    water, milk, coffee = ingredients.values()
    price = the_menu['cost']
    return water, coffee, milk, price

# --- The menu ---
espresso = menu_list('espresso')
latte = menu_list('latte')
cappuccino = menu_list('cappuccino')

# --- inventory and cashflow checking ---
def stock_control_price( water, milk, coffee, cash, menu):
    '''Inventory and cash checking'''
    menu_water, menu_coffee, menu_milk, menu_price = menu
    water -= menu_water
    coffee -= menu_coffee
    milk -= menu_milk
    cash += menu_price
    return water, coffee, milk, cash 

# --- Machine shutdown message ---
def shutdown(water, coffee, milk, cash):
    print("Inventory list:")
    print(f"Water: {water}")
    print(f"Coffee: {coffee}")
    print(f"Milk: {milk}")
    print(f"Cash: $ {cash}")
    print('-' * 20)

# --- Machine workflow ---
while machine_on:
    
    # --- Check if the EVERY stock exist ---
    # --- Stop if ANY of the stock is 0 or below ---
    if water_stock > 0 and milk_stock > 0 and coffee_stock > 0:
        print(f"Inventory:\nWater: {water_stock}\nMilk: {milk_stock}\nCoffee: {coffee_stock}\n")
        start = input("Would you like to order? Press 'y' to start or any other keys to stop:  > ").lower()
        if start == 'y':
            print('-' * 20)
            print("Welcome!")
            print("Choose one of the menu:\n1. Espresso.\n2. Latte\n3. Cappuccino.")
            print('-' * 20)
        
            # --- Check if the order correct ---
            checking = True
            
            while checking:
                order = (input("Enter your order:  > "))
                if order in ['1', '2', '3']:
                    print('-' * 20)
                    print("Payment accepted. Order processed.")
                    checking = False                    
                else:
                    print("Please choose only '1', '2', or '3' to access the menu.\n")
                    continue 

            # --- Process the order ---
            # --- For espresso ---
            if order == '1':                
                water_stock, coffee_stock, milk_stock, account = stock_control_price( water_stock, coffee_stock, milk_stock, account, espresso)
                print("Espresso ready!\n")
                print(f"Inventory:\nWater: {water_stock}\nMilk: {milk_stock}\nCoffee: {coffee_stock}\n")
                
            # --- For latte ---
            elif order == '2':
                water_stock, coffee_stock, milk_stock, account = stock_control_price( water_stock, coffee_stock, milk_stock, account, latte)
                print("Latte ready!\n")
                print(f"Inventory:\nWater: {water_stock}\nMilk: {milk_stock}\nCoffee: {coffee_stock}\n")
                
            # --- For Cappuccino ---
            else:                
                water_stock, coffee_stock, milk_stock, account = stock_control_price( water_stock, coffee_stock, milk_stock, account, cappuccino)
                print("Cappuccino ready!\n")
                print(f"Inventory:\nWater: {water_stock}\nMilk: {milk_stock}\nCoffee: {coffee_stock}\n")
                
            # --- Asking if user will order again or not ---
            start_over = input("Any order? yes / no :   > ").lower()
            if start_over == 'yes' or start_over == 'y':
                print('-' * 20)
                continue
            elif start_over == 'no' or start_over == 'n':
                print("Thank you for using us.")
                shutdown(water_stock, coffee_stock, milk_stock, account)                
                machine_on = False
            else:
                print("Machine don't understand.\nMachine off.")
                shutdown(water_stock, coffee_stock, milk_stock, account)                
                machine_on = False            
        else:
            print("Machine off.")
            shutdown(water_stock, coffee_stock, milk_stock, account)            
            machine_on = False
    else:
        # --- If ANY of the stock is 0 ---
        print("Machine needs to restocked")
        shutdown(water_stock, coffee_stock, milk_stock, account)
        machine_on = False
       
# --- Program finished ---
print("Program terminated!")
print('-' * 20)
    
