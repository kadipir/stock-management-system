#!/usr/bin/python3
from models.base_model import BaseModel
"""
class that enables creation of an instance of the stock
"""

class Stock(BaseModel):
    def __init__(self):
        self.inventory = {}


    def product(self, name, quantity):
        """creates and updates product quantity records"""
        if name in self.inventory:
            self.inventory[name] += quantity
        else:
            self.inventory[name] = {
                    'name' : name,
                    'quantity' : quantity}

    def __str__(self):
        return str(self.inventory)       

if __name__ == "__main__":
    my_stock = Stock()
    my_stock.product()
    print(my_stock)
