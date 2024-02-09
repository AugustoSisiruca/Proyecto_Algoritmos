from Restaurant import Restaurant

class Drink(Restaurant):
    def __init__(self, circuitId, restaurantName, productRestaurant, drinkType, nameItem, price = 0, amount = 0, inventory = 100):
        super().__init__(circuitId, restaurantName, productRestaurant)
        self.drinkType = drinkType
        self.nameItem = nameItem
        self.price = price
        self.amount = amount
        self.inventory = inventory
        
    def showDrink(self): #Funcion para mostrar los atributos de forma ordenada y estetica
        print(f'''   
        BEBIDA   
        Carrera ID: {self.circuitId}
        Restaurante: {self.restaurantName}
        Tipo de bebida: {self.drinkType}
        Nombre de la comida: {self.nameItem}
        Precio Sin IVA: {self.price}$
        ''')
        