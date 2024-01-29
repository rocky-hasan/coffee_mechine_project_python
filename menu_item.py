class MenuItem:
    def __init__(self,Name,Water,Milk,Coffee,Sugar,Cost):
        self.Name=Name
        self.Cost=Cost
        self.product={
            'Water':Water,
            'Coffee':Coffee,
            'Milk':Milk,
            'Sugar':Sugar,
        }
class MenuBar:
    def __init__(self):
        self.menu=[
            MenuItem(Name='cappechino',Water=100,Coffee=25,Milk=20,Sugar=10,Cost=50),
            MenuItem(Name='cold_coffee',Water=50,Coffee=12,Milk=10,Sugar=5,Cost=30),
            MenuItem(Name='espresso',Water=25,Coffee=20,Milk=15,Sugar=7,Cost=25),
            MenuItem(Name='regular',Water=15,Coffee=10,Milk=5,Sugar=5,Cost=20),
        ]
    def get_item(self):
        option=""
        for item in self.menu:
            option +=f"{item.Name}/"
        return option
    
    def search_drink(self,order_name):
        for item in self.menu:
            if item.Name==order_name:
                return item
        print("Sorry item is not available this time")