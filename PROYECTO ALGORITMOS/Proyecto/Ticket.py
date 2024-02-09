class Ticket():
    def __init__(self, name, dni, age, validateCarRace): #Funcion constructora para definir los atributos de la clase Ticket
        self.name = name
        self.dni = dni
        self.age = age
        self.validateCarRace= validateCarRace

        
    def showTicket(self): #Funcion para mostrar los atributos de forma ordenada y estetica
        return f'''
                Nombre: {self.name}
                Cedula: {self.dni}
                Edad: {self.age}
                Carrera: {self.validateCarRace}'''
        
    