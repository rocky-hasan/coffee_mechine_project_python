from coffee_maker import Coffee_Maker
from menu_item import MenuItem,MenuBar
from money_process import MoneyMechine


coffee_mechine=Coffee_Maker()
money_mechine=MoneyMechine()
item_menu=MenuBar()

def report():
    coffee_mechine.reports()
    money_mechine.reports()

# user_report=input('If you want to report, type report')
mechine_ON=True
while mechine_ON:
    customer_choice=input(f'type REPORT to see if ingredients are enough.or\n type (OFF) to turn off :' 
                          + f"\nwhat would you like {item_menu.get_item()}:\n").lower()
    if customer_choice=='report':
        report()
    elif customer_choice=='off':
        mechine_ON=False
    else:
        drink= item_menu.search_drink(customer_choice)
        if coffee_mechine.is_resource_sufficients(drink):
            money_mechine.make_payment(drink.Cost)
            coffee_mechine.make_coffee(drink)
        else:
            break    
        