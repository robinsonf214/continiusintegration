import unittest
from unittest.mock import patch
from io import StringIO
from diningEM import DiningExperienceManager

class TestDiningExperienceManager(unittest.TestCase):
    def setUp(self):
        self.dem = DiningExperienceManager()
    
    def test_display_menu(self):
        expected_output = "Menu:\nBurger - $5\nPizza - $5\nSushi - $7\nSteak - $10\nIce Cream - $3\nCheesecake - $4\nCoffee - $2\nTea - $2\n"
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.dem.display_menu()
            self.assertEqual(mock_stdout.getvalue(), expected_output)
    
    def test_validate_quantity(self):
        self.assertTrue(self.dem.validate_quantity('5'))
        self.assertFalse(self.dem.validate_quantity('0'))
        self.assertFalse(self.dem.validate_quantity('-2'))
        self.assertFalse(self.dem.validate_quantity('abc'))
    
    def test_calculate_total_cost(self):
        order = {'Burger': 2, 'Sushi': 3, 'Ice Cream': 1}
        expected_cost = (2 * 5) + (3 * 7) + (1 * 3)
        self.assertEqual(self.dem.calculate_total_cost(order), expected_cost)
    
    def test_validate_order(self):
        valid_order = {'Burger': 2, 'Sushi': 3}
        self.assertTrue(self.dem.validate_order(valid_order))
        
        invalid_order = {'Burger': 0, 'Sushi': -1}
        self.assertFalse(self.dem.validate_order(invalid_order))
        
        invalid_item_order = {'Burger': 2, 'Salad': 1}
        self.assertFalse(self.dem.validate_order(invalid_item_order))
    
    @patch('builtins.input', side_effect=['Burger', '2', 'Sushi', '3', 'done'])
    def test_place_order_valid(self, mock_input):
        expected_output = "Order confirmed!\nSelected meals:\nBurger - Cantidad: 2\nSushi - Cantidad: 3\nCosto Total: $31\n"
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.dem.place_order()
            self.assertEqual(mock_stdout.getvalue(), expected_output)
    
    @patch('builtins.input', side_effect=['Burger', '0', 'Sushi', 'abc', 'done'])
    def test_place_order_invalid(self, mock_input):
        expected_output = "Orden cancelada. Vuelva a introducir sus selecciones.\n"
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.dem.place_order()
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
