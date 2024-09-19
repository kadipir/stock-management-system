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
            name = input("Enter item name: ")
            quantity = input("Enter quantity: ")
            self.inventory[name] = {
                    'name' : name,
                    'quantity' : quantity
                    }


    def __str__(self):
        return str(self.inventory)       
