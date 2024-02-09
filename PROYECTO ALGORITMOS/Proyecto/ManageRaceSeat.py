from numpy import size
class ManageRaceSeat():
    def __init__(self):
        self.countSeatsGeneral = 0
        self.countSeatsVIP = 0


        
    def checkSeatTicketGeneral(self, listSeatsGeneral, checkCarRace, listTicketGeneral): # Funcion que rellena los asientos Generales comrpados por carrera
        count = 0
        for ticket in listTicketGeneral:
            if ticket.validateCarRace == checkCarRace:
                for i in range(len(listSeatsGeneral)):
                    for j in range(len(listSeatsGeneral[i])):
                        if listSeatsGeneral[i][j] == ticket.generalRaceSeat:
                            listSeatsGeneral[i][j] += 'X'
                            count += 1
        if size(listSeatsGeneral) == count:
            print('\nNo existen asientos disponibles!\n') 
            return False
        
        self.showSeats(listSeatsGeneral)
        return listSeatsGeneral

    def checkSeatTicketVIP(self, listSeatsVIP, checkCarRace, listTicketVIP): # Funcion que rellena los asientos VIP comprados por carrera
        count = 0
        for ticket in listTicketVIP:
            if ticket.validateCarRace == checkCarRace:
                for i in range(len(listSeatsVIP)):
                    for j in range(len(listSeatsVIP[i])):
                        if listSeatsVIP[i][j] == ticket.VIPRaceSeat:
                            listSeatsVIP[i][j] += 'X'
                            count += 1
                            
        if size(listSeatsVIP) == count:
            print('\nNo existen asientos disponibles!\n') 
            return False
        
        self.showSeats(listSeatsVIP)
        return listSeatsVIP                      
     
     
                        
    def validateSeatGeneral(self, listSeatsGeneral, checkCarRace, listTicketGeneral): # Funcion que valida y asigna si el asiento general no esta ocupado
        listSeatsGeneral = self.checkSeatTicketGeneral(listSeatsGeneral, checkCarRace, listTicketGeneral)
        if listSeatsGeneral == False:
            return False
        
        while True:
            reserveSeat = input('\nIngrese el asiento que desea comprar: ').upper()
            seatAvailable = False
            
            for i in range(len(listSeatsGeneral)):
                for j in range(len(listSeatsGeneral[i])):
                    if (listSeatsGeneral[i][j])[:-1] == reserveSeat and (listSeatsGeneral[i][j])[-1]=='X':
                            print("\nEl asiento ya esta ocupado, seleccione otro!\n")
                            seatAvailable = True
                            
                            
                    elif listSeatsGeneral[i][j] == reserveSeat:
                            listSeatsGeneral[i][j] += 'X'
                            seatAvailable = True
                            print('\nAsiento escogido: \n')
                            self.showSeats(listSeatsGeneral)
                            return listSeatsGeneral[i][j]
                    
            if seatAvailable == False:
                print('El asiento seleccionado no existe!')

    def validateSeatVIP(self, listSeatsVIP, checkCarRace, listTicketVIP): # Funcion que valida y asigna si el asiento VIP no esta ocupado
        listSeatsVIP = self.checkSeatTicketVIP(listSeatsVIP, checkCarRace, listTicketVIP)
        if listSeatsVIP == False:
            return False
        
        while True:
            reserveSeat = input('\nIngrese el asiento que desea comprar: ').upper()
            seatAvailable = False
            
            for i in range(len(listSeatsVIP)):
                for j in range(len(listSeatsVIP[i])):
                    if (listSeatsVIP[i][j])[:-1] == reserveSeat and (listSeatsVIP[i][j])[-1]=='X':
                            print("\nEl asiento ya esta ocupado, seleccione otro!\n")
                            seatAvailable = True
                            
                            
                    elif listSeatsVIP[i][j] == reserveSeat:
                            listSeatsVIP[i][j] += 'X'
                            print('\nAsiento escogido: \n')
                            self.showSeats(listSeatsVIP)
                            
                            return listSeatsVIP[i][j]
                    
            if seatAvailable == False:
                print('El asiento seleccionado no existe!')
                
                
                
    def CreateMapGeneral(self, listCarRaces, checkCarRace): #Funcion para verificar y crear los asientos generales por filas columnas
        for carRace in listCarRaces:
            if checkCarRace == carRace.name:
                listSeatsGeneral = []
                rowSeats = ['A','B','C','D','E','F','G','H','I','J','K']
                for i in range(carRace.mapGeneral[1]):
                    row = []
                    for j in range(carRace.mapGeneral[0]):
                        row.append(rowSeats[i]+str(j+1))
                    listSeatsGeneral.append(row)
                return listSeatsGeneral

    def CreateMapVIP(self, listCarRaces, checkCarRace): #Funcion para verificar y crear los asientos VIP por filas columnas
        for carRace in listCarRaces:
            if checkCarRace == carRace.name:
                listSeatsVIP = []
                rowSeats = ['A','B','C','D','E','F','G','H','I','J','K']
                for i in range(carRace.mapVIP[1]):
                    row = []
                    for j in range(carRace.mapVIP[0]):
                        row.append(rowSeats[i]+str(j+1))
                    listSeatsVIP.append(row)
                return listSeatsVIP
  
  
  
    def showSeats(self, listSeats): #Funcion que imprime el mapa de los asientos seleccionados
        for i in range(len(listSeats)):
            for j in range(len(listSeats[i])):
                print(listSeats[i][j], end = "\t")
            print()
            
            
  
