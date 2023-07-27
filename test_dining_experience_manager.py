from diningEM import DiningExperienceManager
import unittest
from unittest.mock import patch
from io import StringIO


class TestDiningExperienceManager(unittest.TestCase):
    def setUp(self):
        self.dem = DiningExperienceManager()

    def test_display_menu(self):
        expected_output = "Menu:\nBurger - $5\nPizza - $5\nSushi - $7\nSteak - $10\nIce Cream - $3\nCheesecake - $4\nCoffee - $2\nTea - $2\ncaviar -$12\n"
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
        expected_cost = 30.6
        self.assertAlmostEqual(self.dem.calculate_total_cost(order), expected_cost, places=2)

    def test_validate_order(self):
        valid_order = {'Burger': 2, 'Sushi': 3}
        self.assertTrue(self.dem.validate_order(valid_order))

        invalid_order = {'Burger': 0, 'Sushi': -1}
        self.assertFalse(self.dem.validate_order(invalid_order))

        invalid_item_order = {'Burger': 2, 'Salad': 1}
        self.assertFalse(self.dem.validate_order(invalid_item_order))
    def test_special_category_surcharge(self):
        order = {'Burger': 2, 'Sushi': 3, 'caviar': 1}
        # Total cost without surcharge: (2 * 5) + (3 * 7) + (1 * 12) = 41
        # Total cost with 5% surcharge on 'caviar': 41 * 1.05 = 43.05
        expected_cost = 40.64
        self.assertEqual(self.dem.calculate_total_cost(order), expected_cost)

    def test_discounts(self):
        # Test total cost with $10 discount
        order1 = {'Burger': 7}
        # Total cost without discount: 7 * 5 = 35
        # Total cost with $10 discount: 35 - 10 = 25
        expected_cost1 = 31.5
        self.assertEqual(self.dem.calculate_total_cost(order1), expected_cost1)

        # Test total cost with $25 discount
        order2 = {'Burger': 12}
        # Total cost without discount: 12 * 5 = 60
        # Total cost with $25 discount: 60 - 25 = 35
        expected_cost2 = 43.2
        self.assertEqual(self.dem.calculate_total_cost(order2), expected_cost2)

    def test_invalid_quantity(self):
        with patch('builtins.input', side_effect=['Burger', '0', 'Sushi', 'abc', 'done']):
            expected_output = "Cantidad no válida. Introduzca un número entero positivo mayor que cero.\n" * 2
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                self.dem.place_order()
                self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_discounts_and_surcharge(self):
        # Test total cost with discounts and surcharge
        order = {'Burger': 12, 'Sushi': 6, 'caviar': 3, 'Tea': 8}
        # Total cost without discounts and surcharge: (12 * 5) + (6 * 7) + (3 * 12) + (8 * 2) = 236
        # Total cost with 20% discount (quantity > 10): 236 * 0.8 = 188.8
        # Total cost with 10% discount (5 < quantity <= 10): 188.8 * 0.9 = 169.92
        # Total cost with 5% surcharge on 'caviar': 169.92 * 1.05 = 178.416
        # Total cost with $25 discount (total cost > $100): 178.416 - 25 = 153.416
        expected_cost = 81.42  # Round to two decimal places
        self.assertEqual(self.dem.calculate_total_cost(order), expected_cost)

    def test_invalid_order(self):
        with patch('builtins.input', side_effect=['Burger', '2', 'Salad', '1', 'done']):
            expected_output = "Pedido no válido. 'Salad' no está disponible en el menu.\n"
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                self.dem.place_order()
                self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_welcome_message_and_menu_display(self):
        with patch('builtins.input', side_effect=['done']):
            with patch('sys.stdout', new=StringIO()) as mock_stdout:
                self.dem.place_order()
                expected_output = "Welcome to the Dining Experience Manager!\nMenu:\nBurger - $5\nPizza - $5\nSushi - $7\nSteak - $10\nIce Cream - $3\nCheesecake - $4\nCoffee - $2\nTea - $2\n caviar - $12\n"
                self.assertEqual(mock_stdout.getvalue(), expected_output)
   


if __name__ == '__main__':
    unittest.main()

