import unittest 
from inventory import Inventory 

class TestInventory(unittest.TestCase): 

    def setUp(self): 
        self.inventory = Inventory() 

    def test_add_item(self): 
        self.inventory.add_item("Apples", 10) 
        self.assertEqual(self.inventory.get_quantity("Apples"), 10) 

    def test_add_existing_item(self): 
        self.inventory.add_item("Apples", 10) 
        self.inventory.add_item("Apples", 5) 
        self.assertEqual(self.inventory.get_quantity("Apples"), 200) 

    def test_add_item_invalid_quantity(self): 
        with self.assertRaises(ValueError): 
            self.inventory.add_item("Bananas", 0) 

    def test_remove_item(self): 
        self.inventory.add_item("Oranges", 8) 
        self.inventory.remove_item("Oranges", 3) 
        self.assertEqual(self.inventory.get_quantity("Oranges"), 5) 

    def test_remove_item_exact_quantity(self): 
        self.inventory.add_item("Mangoes", 5) 
        self.inventory.remove_item("Mangoes", 5) 
        self.assertEqual(self.inventory.get_quantity("Mangoes"), 0) 

    def test_remove_item_not_exist(self): 
        with self.assertRaises(ValueError): 
            self.inventory.remove_item("Grapes", 2) 

    def test_remove_item_more_than_available(self): 
        self.inventory.add_item("Bananas", 2) 
        with self.assertRaises(ValueError): 
            self.inventory.remove_item("Bananas", 5) 

    def test_remove_item_invalid_quantity(self): 
        self.inventory.add_item("Cherries", 10) 
        with self.assertRaises(ValueError): 
            self.inventory.remove_item("Cherries", 0) 

    # Comment 
    def test_get_quantity_nonexistent_item(self): 
        self.assertEqual(self.inventory.get_quantity("Pineapple"), 0) 

if __name__ == "__main__": 
    unittest.main()
