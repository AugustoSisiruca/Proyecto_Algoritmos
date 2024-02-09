class CarRace():
    def __init__(self, name, round, date, circuitId, mapGeneral, mapVIP, podium = '', asistence = 0): #Funcion constructora para definir los atributos
        self.name = name
        self.round = round
        self.date = date
        self.circuitId = circuitId
        self.mapGeneral = mapGeneral
        self.mapVIP = mapVIP
        self.podium = podium
        self.seatGeneral = self.mapGeneral[0] * self.mapGeneral[1]
        self.seatVIP = self.mapVIP[0] * mapVIP[1]
        self.asistence = asistence

        
    def showCarRace(self): #Funcion para mostrar los atributos de forma ordenada y estetica
        print(f'''
        CARRERA
        Nombre: {self.name}
        Ronda: {self.round}
        Fecha: {self.date}
        ID del Circuito: {self.circuitId}
        Asientos generales: {self.seatGeneral}
        Asientos VIP: {self.seatVIP}
        Podium: {self.podium}
        ''')