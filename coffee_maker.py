class Coffee_Maker:
    def __init__(self):
        self.ingredients={
            'Water': 300,
            'Coffee': 200,
            'Milk': 200,
            'Sugar': 100,
        }
    def reports(self):
        """Prints the reports for every Person"""
        print(f"Water : {self.ingredients['Water']}ml")
        print(f"Coffee Powder : {self.ingredients['Coffee']}g")
        print(f"Milk : {self.ingredients['Milk']}g")
        print(f"Sugar : {self.ingredients['Sugar']}g")
        
        """check product sufficients or not"""
    def is_resource_sufficients(self,drink):
        can_make=True
        for item in drink.product:
            if drink.product[item]>self.ingredients[item]:
                print(f"Sorry there is not enough {item}")
                can_make=False
        return can_make
    def make_coffee(self,order):
        for item in order.product:
            self.ingredients[item] -=order.product[item]
        print(f"Here is your {order.Name }")

    