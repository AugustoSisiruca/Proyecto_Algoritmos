class Pilot():
    def __init__(self, firstName, lastName, dateOfBirth, nationality, permanentNumber, pilotId, pointCarRace = 0):
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        self.nationality = nationality
        self.permanentNumber = permanentNumber
        self.pilotId = pilotId
        self.pointCarRace = pointCarRace
    
    def showPilot(self): #Funcion para mostrar los atributos de forma ordenada y estetica
        print(f'''
        PILOTO
        ID: {self.pilotId}
        Nombre: {self.firstName}
        Apellido: {self.lastName}
        Fecha de Nacimiento: {self.dateOfBirth}
        Nacionalidad: {self.nationality}
        Numero del Piloto: {self.permanentNumber}
        Puntos obtenidos: {self.pointCarRace}
    
        ''')