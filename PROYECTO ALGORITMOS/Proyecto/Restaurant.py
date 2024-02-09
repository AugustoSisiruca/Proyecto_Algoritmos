from Product import Product

class Restaurant():
    def __init__(self, circuitId, restaurantName, productRestaurant):
        self.circuitId = circuitId
        self.restaurantName = restaurantName
        self.productRestaurant = productRestaurant
        
        
    
    def showRestaurant(self): #Funcion para mostrar los atributos de forma ordenada y estetica
        print(f'''
        Carrera ID: {self.circuitId}
        Nombre del restaurante: {self.restaurantName}
        ''')
        

    