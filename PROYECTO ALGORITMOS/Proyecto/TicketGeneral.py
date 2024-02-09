from Ticket import Ticket

class TicketGeneral(Ticket):
    def __init__(self, name, dni, age, validateCarRace, generalRaceSeat = 'GEN-', price = 150, restaurant = False, ticketId = 'GEN', usedTicket = False, spentMoney = 0): #Funcion constructora para definir los atributos heredados de la clase hija TicketVIP
        super().__init__(name, dni, age, validateCarRace)
        self.generalRaceSeat = generalRaceSeat
        self.price = price
        self.restaurant = restaurant
        self.ticketId = ticketId
        self.usedTicket = usedTicket
        self.spentMoney = spentMoney
        
    def showTicketGeneral(self): #Funcion para mostrar los atributos de la clase hija TicketGeneral en forma ordenada y estetica
        return f'''
                TIPO DE ENTRADA: ENTRADA GENERAL
                {super().showTicket()}
                Precio de la entrada: {self.price}$'''
                
    def showEntranceTicket(self): #Funcion para mostrar los atributos del boleto de entrada General
        return f'''
                ---------------------------------
                    BOLETO DE ENTRADA GENERAL
                ---------------------------------
                {super().showTicket()}
                Restaurante: No Aplica
                Asiento: {self.generalRaceSeat}
                Ticket ID: {self.ticketId}
                Ticket Usado: {self.usedTicket}
                ---------------------------------
                '''