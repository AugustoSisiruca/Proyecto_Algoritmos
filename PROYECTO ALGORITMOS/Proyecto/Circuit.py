class Circuit():
    def __init__(self, circuitId, name, country, locality, lat, long): #Funcion constructora para definir los atributos
        self.circuitId = circuitId
        self.name = name
        self.country = country
        self.locality = locality
        self.lat = lat
        self.long = long
        
    def showCircuit(self): #Funcion para mostrar los atributos de forma ordenada y estetica
        print(f'''
        CIRCUITO
        ID: {self.circuitId}
        Nombre: {self.name}
        Ubicacion:
        -Pais: {self.country}
        -Localidad: {self.locality}
        -Latitud: {self.lat}
        -Longitud: {self.long}
        ''')