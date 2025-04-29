class Inventory: 

    def __init__(self): 
        self.items = {} 

    def add_item(self, item_name, quantity): 
        if quantity <= 0: 
            raise ValueError("Quantity must be positive.") 
        if item_name in self.items: 
            self.items[item_name] += quantity 
        else: 
            self.items[item_name] = quantity 

    def remove_item(self, item_name, quantity): 
        if item_name not in self.items: 
            raise ValueError("Item not found in inventory.") 
        if quantity <= 0: 
            raise ValueError("Quantity must be positive.") 
        if quantity > self.items[item_name]: 
            raise ValueError("Not enough quantity to remove.") 
        self.items[item_name] -= quantity 
        if self.items[item_name] == 0: 
            del self.items[item_name] 

    def get_quantity(self, item_name): 
        return self.items.get(item_name, 0) 
