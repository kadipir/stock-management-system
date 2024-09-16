#!/usr/bin/python3
"""
class that enables creation of an instance of the stock
"""

class Stock:
    def __init__(self):
        self.inventory = {}


    def product(self, name, quantity):
        """creates and updates product quantity records"""
        if name in self.inventory:
            self.inventory[name]['quantity'] += quantity
        else:
            self.inventory[name] = {
                    'name' : name,
                    'quantity' : quantity,
                    }

