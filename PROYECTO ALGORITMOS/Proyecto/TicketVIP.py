from Ticket import Ticket

class TicketVIP(Ticket):
    def __init__(self, name, dni, age, validateCarRace,  VIPRaceSeat = 'VIP-', price = 340, restaurant = True, ticketId = 'VIP', usedTicket = False, spentMoney = 0): #Funcion constructora para definir los atributos heredados de la clase hija TicketVIP
        super().__init__(name, dni, age, validateCarRace)
        self.VIPRaceSeat = VIPRaceSeat
        self.price = price
        self.restaurant = restaurant
        self.ticketId = ticketId
        self.usedTicket = usedTicket
        self.spentMoney = spentMoney
        
    def showTicketVIP(self): #Funcion para mostrar los atributos de la clase hija TicketVIP en forma ordenada y estetica
        return f'''     
                TIPO DE ENTRADA: ENTRADA VIP
                {super().showTicket()}
                Precio de la Entrada: {self.price}$'''
                
    def showEntranceTicket(self): #Funcion para mostrar los atributos del boleto de entrada VIP
        return f'''
                --------------------------------
                    BOLETO DE ENTRADA VIP
                --------------------------------
                {super().showTicket()}
                Restaurante: Aplica
                Asiento: {self.VIPRaceSeat}
                Ticket ID: {self.ticketId}
                Ticket Usado: {self.usedTicket}
                --------------------------------
                '''
        
        
        
    
    
        