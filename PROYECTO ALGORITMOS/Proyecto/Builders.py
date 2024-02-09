class Builders():
    def __init__(self, name, id, nationality, referencePilots, pointCarRace = 0): #Funcion constructora para definir los atributos
        self.name = name
        self.id = id
        self.nationality = nationality
        self.referencePilots = referencePilots
        self.pointCarRace = pointCarRace
        
    def showBuilders(self):
        print(f''' 
        CONSTRUCTOR
        Equipo: {self.name}
        ID Del Equipo: {self.id}
        Nacionalidad: {self.nationality}
        Referencia del piloto: {str(self.referencePilots)[1:-1]}
        Puntos obtenidos por equipo: {self.pointCarRace}
        ''')
    