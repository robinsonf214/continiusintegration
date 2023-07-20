class DiningExperienceManager:
    def __init__(self):
        self.menu = {
            'Burger': {'price': 5, 'category': 'Regular'},
            'Pizza': {'price': 5, 'category': 'Regular'},
            'Sushi': {'price': 7, 'category': 'Regular'},
            'Steak': {'price': 10, 'category': 'Regular'},
            'Ice Cream': {'price': 3, 'category': 'Dessert'},
            'Cheesecake': {'price': 4, 'category': 'Dessert'},
            'Coffee': {'price': 2, 'category': 'Beverage'},
            'Tea': {'price': 2, 'category': 'Beverage'},
            'caviar': {'price': 12, 'category': 'Special'},
        }
    
    def display_menu(self):
        print("Menu:")
        for item, details in self.menu.items():
            print(f"{item} - ${details['price']}")
    
    def validate_quantity(self, quantity):
        try:
            quantity = int(quantity)
            if quantity > 0:
                return True
            else:
                print("Cantidad no válida. Introduzca un número entero positivo mayor que cero.")
        except ValueError:
            print("Cantidad no válida. Introduzca un número entero positivo mayor que cero.")
        return False
    
    def calculate_total_cost(self, order):
        total_cost = 0
        quantity_sum = sum(order.values())
        
        for item, quantity in order.items():
            if item in self.menu:
                price = self.menu[item]['price']
                total_cost += price * quantity
            else:
                return -1  # Invalid input, item not available in the menu
        
        if quantity_sum > 5:
            total_cost *= 0.9  # Apply 10% discount if quantity is more than 5
        if quantity_sum > 10:
            total_cost *= 0.8  # Apply 20% discount if quantity is more than 10
        
        special_category_items = [item for item in order if self.menu[item]['category'] == 'Special']
        if special_category_items:
            total_cost *= 1.05  # Apply 5% surcharge to special category items
        
        if total_cost > 50:
            total_cost -= 10  # Apply $10 discount if total cost is more than $50
        if total_cost > 100:
            total_cost -= 25  # Apply $25 discount if total cost is more than $100
        
        return total_cost
    #Cambio
    #print()
    def validate_order(self, order):
        for item, quantity in order.items():
            if item not in self.menu:
                print(f"Pedido no válido. '{item}' no está disponible en el menu.")
                return False
            if not self.validate_quantity(quantity):
                return False
        return True
    
    def place_order(self):
        print("Welcome to the Dining Experience Manager!")
        self.display_menu()
        
        order = {}
        while True:
            item = input("Ingrese el nombre de la comida a ordenar (o 'done' para terminar): ")
            if item == 'done':
                break
            
            quantity = input("Introduzca la cantidad:")
            if not self.validate_quantity(quantity):
                continue
            
            order[item] = int(quantity)
        
        if self.validate_order(order):
            total_cost = self.calculate_total_cost(order)
            if total_cost == -1:
                print("Pedido no válido. Verifique sus selecciones.")
            else:
                print("Order confirmed!")
                print("Selected meals:")
                for item, quantity in order.items():
                    print(f"{item} - Cantidad: {quantity}")
                print(f"Costo Total: ${total_cost}")
        else:
            print("Orden cancelada. Vuelva a introducir sus selecciones.")


def main():
    dem = DiningExperienceManager()
    dem.place_order()


if __name__ == '__main__':
    main()

