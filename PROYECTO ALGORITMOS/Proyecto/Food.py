from Restaurant import Restaurant

class Food(Restaurant):
    def __init__(self, circuitId, restaurantName, productRestaurant, foodType, nameItem, price = 0, amount = 0, inventory = 100):
        super().__init__(circuitId, restaurantName, productRestaurant)
        self.foodType = foodType
        self.nameItem = nameItem
        self.price = price
        self.amount = amount
        self.inventory = inventory
        
        
    def showFood(self): #Funcion para mostrar los atributos de forma ordenada y estetica
        print(f'''   
        COMIDA   
        Carrera ID: {self.circuitId}
        Restaurante: {self.restaurantName}
        Tipo de servicio: {self.foodType}
        Nombre de la comida: {self.nameItem}
        Precio Sin IVA: {self.price}$
        ''')
        
