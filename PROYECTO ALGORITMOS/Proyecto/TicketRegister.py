from TicketGeneral import TicketGeneral
from TicketVIP import TicketVIP
from ManageRaceSeat import ManageRaceSeat
from BuyTicket import BuyTicket

class TicketRegister():
    def __init__(self):
        pass


    def WavyNumber(self, ticket):  #Funcion que devuelve un booleano True/False depedendiendo si el numero es ondulado
        dni = ticket.dni 
        if int(dni) < 100:
            return True
        
        if len(dni) % 2 != 0:
            for i in range(len(dni)):
                if i % 2 == 0:
                    if dni[i] == dni[0]:
                        pass
                    else:
                        return False
                    
                elif i % 2 != 0:
                    if dni[i] == dni[1]:
                        pass
                    
                    else:
                        return False
            return True
        
        elif len(dni) % 2 == 0:
            for i in range(len(dni)):
                if i % 2 == 0:
                    if dni[i] == dni[-2]:
                        pass
                    else:
                        return False
                    
                elif i % 2 != 0:
                    if dni[i] == dni[-1]:
                        pass
                    
                    else:
                        return False
            return True  
      
    def onlyID(self, listTicket):  #funcion que verificar que no se repita la cedula en las compras
        value = True
        dni = input('\nIngrese su cedula para la verificacion, sin puntos ni otro simbolo no numerico: ')
        while not dni.isdigit() or not int(dni) > 0:
            dni = input('Error! Ingrese su cedula correctamente: ')

        while True: 
                    
            for ticket in listTicket:
                if ticket.dni == dni:
                    value = False
                    
            if value == False:
                print('\nError! Cedula ya registrada!\n ')
                
            elif value == True:
                return dni  
               
            dni = input('Ingrese otra cedula: ')
            while not dni.isdigit() or not int(dni) > 0:
                dni = input('Error! Ingrese su cedula correctamente: ')
            value = True

           
    def buyTicketGeneral(self, ticketGeneral): #Funcion que imprime la factura del ticket general y retorna los valores del ticket comprado
        validateNumber = TicketRegister().WavyNumber(ticketGeneral)
        ticketPrice = 150
        if validateNumber == True:
            print('\nSe le apelicara un descuento del 50% para su compra porque su cedula es un numero ondulado!\n')
            discount = ticketPrice * 0.50 
            subtotalPrice = ticketPrice - discount
        else:
            discount = 'No aplica'              
            subtotalPrice = ticketPrice
            
        vatTax = subtotalPrice * 0.16
        totalPrice = subtotalPrice + vatTax
        
        
        buyTicketGeneral = BuyTicket(ticketGeneral, discount, subtotalPrice, vatTax, totalPrice)
        buyTicketGeneral.showBillGeneral()
        while True:    
            buyConfirm = input('''Desea proceder con su compra:
                                    1.Si
                                    2.No
                                    Opcion: ''')
            if buyConfirm == '1':
                print('\nPago Exitoso!\nGracias por su compra! Vuelva pronto!\n')
                ticketGeneral.spentMoney += totalPrice   
                return ticketGeneral, []
                
                    
            elif buyConfirm == '2':
                print('\nGracias por su vista!\n')
                return [], []
                    
            else:
                print('\nError! Opcion incorrecta, vuelve a intentarlo.\n')            
                           
    def buyTicketVIP(self, ticketVIP): # funcion que imprime la factura del ticket VIP y retorna los valores del ticket comprado
        validateNumber = TicketRegister().WavyNumber(ticketVIP)
        ticketPrice = 340
        
        if validateNumber == True:
            print('\nSe le apelicara un descuento del 50% para su compra porque su cedula es un numero ondulado!\n')
            discount = ticketPrice * 0.50 
            subtotalPrice = ticketPrice - discount
        else:
            discount = 'No aplica'              
            subtotalPrice = ticketPrice
            
        vatTax = subtotalPrice * 0.16
        totalPrice = subtotalPrice + vatTax
        

        buyTicketVIP = BuyTicket(ticketVIP, discount, subtotalPrice, vatTax, totalPrice)
        buyTicketVIP.showBillVIP()   
        
        while True:    
            buyConfirm = input('''Desea proceder con su compra:
                            1.Si
                            2.No
                            Opcion: ''')
            
            if buyConfirm == '1':
                print('\nPago Exitoso!\nGracias por su compra! Vuelva pronto!\n')
                ticketVIP.spentMoney += totalPrice
                return [], ticketVIP
                
            
            elif buyConfirm == '2':
                print('\nGracias por su vista!\n')
                return [], []
                
            else:
                print('\nError! Opcion incorrecta, vuelve a intentarlo.\n')            
                      
    def createTicket(self, checkCarRace, listTicket, listTicketGeneral, listTicketVIP, listCarRaces): #Funcion que registra el ticket y retorna el objeto
        print('\nREGISTRO DE DATOS:')
        firstName = input('\nIngrese su primer nombre: ').lower()
        while not firstName.isalpha():
            firstName = input('\nError! El nombre no puede llevar caracteres especiales ni espacios ni numeros: ').lower()
        lastName = input('\nIngrese su apellido: ').lower()
        while not lastName.isalpha():
            lastName = input('\nError! El apellido no puede llevar caracteres especiales ni espacios ni numeros: ').lower()
        name = firstName.title() + " " + lastName.title()
        dni = self.onlyID(listTicket)
        age = input('\nIngrese su edad sin puntos ni otro simbolo no numerico: ')
        while not age.isdigit() or not int(age) > 0:
            age = input('\nError! Ingrese su edad correctamente: ')
        
        while True:
            typeTicket = input('''
            Ingrese cual de los tipos de entrada desea comprar:
                
                1. Entrada General (Precio: 150$)
                2. Entrada VIP (Precio: 340$ e incluye acceso al restaurante!)
                
                Opcion: ''')
            
            if typeTicket == '1':
                print('\nSeleccione su asiento General de los que estan disponibles: \n')
                listSeatsGeneral = ManageRaceSeat().CreateMapGeneral(listCarRaces, checkCarRace)
                generalRaceSeats = ManageRaceSeat().validateSeatGeneral(listSeatsGeneral, checkCarRace, listTicketGeneral)
                if generalRaceSeats == False:
                    print('\nNo se puede realizar la compra por falta de asientos! Intente comprar en otro momento!\n')
                    return [], []
                generalRaceSeats = generalRaceSeats[:-1]
  
                ticketGeneral = TicketGeneral(name, dni, age, checkCarRace, generalRaceSeats)
                objectTicketGeneral, objectTicketVIP = self.buyTicketGeneral(ticketGeneral)
                return objectTicketGeneral, objectTicketVIP

                
            elif typeTicket == '2':
                print('\nSeleccione su asiento VIP de los que estan disponibles:\n ')
                listSeatsVIP = ManageRaceSeat().CreateMapVIP(listCarRaces, checkCarRace)
                VIPRaceSeats = ManageRaceSeat().validateSeatVIP(listSeatsVIP, checkCarRace, listTicketVIP)
                if VIPRaceSeats == False:
                    print('\nNo se puede realizar la compra por falata de asientos! Intente comprar en otro momento!\n')
                    return [], []
                VIPRaceSeats = VIPRaceSeats[:-1]
                
                ticketVIP = TicketVIP(name, dni, age, checkCarRace, VIPRaceSeats)
                objectTicketGeneral, objectTicketVIP = self.buyTicketVIP(ticketVIP)
                return objectTicketGeneral, objectTicketVIP
            
            else:
                print('\nError! Opcion incorrecta, vuelve a intentarlo.\n')
                