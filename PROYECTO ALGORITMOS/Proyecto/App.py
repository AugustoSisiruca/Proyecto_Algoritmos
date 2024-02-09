import random 
import statistics
import json
from RestaurantManage import RestaurantManage
from Restaurant import Restaurant
from Drink import Drink
from Food import Food
from TicketRegister import TicketRegister
from TicketGeneral import TicketGeneral
from TicketVIP import TicketVIP
from Builders import Builders
from CarRace import CarRace
from Circuit import Circuit
from Pilot import Pilot
from Product import Product
from BuyProduct import BuyProduct



class App():
    def __init__(self):
        self.listTicket = []
        self.listTicketVIP = []
        self.listTicketGeneral = []
        self.listRestaurant = []
        self.listDrink = []
        self.listFood = []
        self.listWinnerRaceCar = False
        self.validate = True
        self.countcarRaceBestSellers = []
        self.listRestaurantProducts = []
        self.safe = False

        
    def getData(self):  # funcion para obtener datos de tickets, el restaurante, la comida y la bebida   
        openTxt = open('ticketGeneral.txt', 'r')
        data = openTxt.readlines()
        for line in data:
            ticketData = line.split(',')
            newTicketGeneral = TicketGeneral(ticketData[0], ticketData[1], ticketData[2], ticketData[3], ticketData[4], int(ticketData[5]), eval(ticketData[6]), ticketData[7], eval(ticketData[8]), float(ticketData[9]))
            self.listTicketGeneral.append(newTicketGeneral)
        openTxt.close()
        
        openTxt = open('ticketVIP.txt', 'r')
        data = openTxt.readlines()
        for line in data:
            ticketData = line.split(',')
            newTicketVIP = TicketVIP(ticketData[0], ticketData[1], ticketData[2], ticketData[3], ticketData[4], int(ticketData[5]), eval(ticketData[6]), ticketData[7], eval(ticketData[8]), float(ticketData[9]))
            self.listTicketVIP.append(newTicketVIP)
        openTxt.close()

        openTxt = open('listFood.txt', 'r')
        data = openTxt.readlines()
        for line in data:
            foodData = line.split('?')
            newFood = BuyProduct(foodData[0], foodData[1], foodData[2], (str(foodData[3])[2:-2]), foodData[4], float(foodData[5]), float(foodData[6]), float(foodData[7]))
            self.listFood.append(newFood)
        openTxt.close()

        openTxt = open('listDrink.txt', 'r')
        data = openTxt.readlines()
        for line in data:
            drinkData = line.split('?')
            newDrink = BuyProduct(drinkData[0], drinkData[1], drinkData[2], (str(drinkData[3])[2:-2]), drinkData[4], float(drinkData[5]), float(drinkData[6]), float(drinkData[7]))
            self.listDrink.append(newDrink)
        openTxt.close()        
    
    def saveData(self, listTicketGeneral, listTicketVIP): #funcion para guardar los datos de tickets y el restaurante.
        openTxt = open('ticketGeneral.txt', 'w')

        ticketDataGeneral = []
        
        for item in listTicketGeneral:
            ticketString = f'{item.name},{item.dni},{item.age},{item.validateCarRace},{item.generalRaceSeat},{item.price},{item.restaurant},{item.ticketId},{item.usedTicket},{item.spentMoney}\n'
            ticketDataGeneral.append(ticketString)
        openTxt.writelines(ticketDataGeneral)
        openTxt.close()
            
        openTxt = open('ticketVIP.txt', 'w')
        ticketDataVIP = []
        
        for item in listTicketVIP:
            ticketString = f'{item.name},{item.dni},{item.age},{item.validateCarRace},{item.VIPRaceSeat},{item.price},{item.restaurant},{item.ticketId},{item.usedTicket},{item.spentMoney}\n'
            ticketDataVIP.append(ticketString)
        openTxt.writelines(ticketDataVIP)
        openTxt.close()           
        
        openTxt = open('listFood.txt', 'w')
        foodData = []
        for item in self.listFood:
            foodString = f'{item.name}?{item.dni}?{item.age}?{item.listBuyProduct}?{item.discount}?{item.subtotalPrice}?{item.priceIVA}?{item.totalPrice}\n'
            foodData.append(foodString)
        openTxt.writelines(foodData)
        openTxt.close()

        openTxt = open('listDrink.txt', 'w')
        drinkData = []
        for item in self.listDrink:
            drinkString = f'{item.name}?{item.dni}?{item.age}?{item.listBuyProduct}?{item.discount}?{item.subtotalPrice}?{item.priceIVA}?{item.totalPrice}\n'
            drinkData.append(drinkString)
        openTxt.writelines(drinkData)
        openTxt.close()
            
            
                 
    def requestPilots(self): #Funcion para solicitar el codigo de la Api para pilotos  y convertirlo en un diccionario
        with open("pilot.json", "r") as j:
            pilots = json.load(j)
        return pilots
        
    def requestBuilders(self): #Funcion para solicitar el codigo de la Api para los constructores  y convertirlo en un diccionario
        with open("builder.json", "r") as j:
            builders = json.load(j)
        return builders
    
    def requestCarRaces(self): #Funcion para solicitar el codigo de la Api para la carrera y convertirlo en un diccionario
        with open("carRace.json", "r") as j:
            carRaces = json.load(j)
        return carRaces
     
       
      
            
    def TransformListPilots(self, dictionaryPilots): #funcion para convertir el diccionario de la Api de pilotos en lista
        listPilots = []
        for item in dictionaryPilots:
            pilot = Pilot(item['firstName'], item['lastName'], item['dateOfBirth'], item['nationality'], item['permanentNumber'], item['id'])
            listPilots.append(pilot)
        return listPilots
            
    def TransformListBuilders(self, dictionaryBuilders, dictionaryPilots): #funcion para convertir el diccionario de la Api de constructores en lista
        listBuilders = []
        listItems = []
        listUserBuilders = []
        listItemCount = []
        for team in dictionaryBuilders:
            for pilots in dictionaryPilots:
                if team['id'] == pilots['team']:
                    user = {pilots['team']: pilots['id']}
                    listItems.append(user)

        count = 0
        for item in listItems:
            for value in item.values():
                listItemCount.append(value)
                count += 1
                
                if count == 2:
                    listUserBuilders.append(listItemCount)
                    listItemCount = []
                    count = 0
                    
        for builder, pilots in zip(dictionaryBuilders, listUserBuilders):
            builder = Builders(builder['name'], builder['id'], builder['nationality'], pilots)
            listBuilders.append(builder)           
        return listBuilders
    
    def TransformListCarRaces(self, dictionaryCarRaces): #funcion para convertir el diccionario de la Api de carrera en lista
        listCarRaces = []
        for item in dictionaryCarRaces:
            carRace = CarRace(item['name'], item['round'], item['date'], item['circuit']['circuitId'], item['map']['general'], item['map']['vip'], podium = 'No establecido')
            listCarRaces.append(carRace)
        return listCarRaces  
                    
    def TransformListCircuit(self, dictionaryCarRaces): #funcion para convertir el diccionario de la Api de carrera en lista para el circuito
        listCircuit = []
        for item in dictionaryCarRaces:
            circuit = Circuit(item['circuit']['circuitId'], item['circuit']['name'], item['circuit']['location']['country'], item['circuit']['location']['locality'], item['circuit']['location']['lat'], item['circuit']['location']['long'])
            listCircuit.append(circuit)
    
        return listCircuit  

    def TransformListRestaurant(self, dictionaryCarRaces): #funcion para convertir el diccionario de la Api de carrera en lista
        listRestaurant = []
        listProducts = []
        listFood = []
        listDrink = []
        for restaurants in dictionaryCarRaces:
            for item in restaurants['restaurants']:
                for product in item['items']:
                    productRestaurant = Product(product['name'], product['type'], float(product['price']))
                    listProducts.append(productRestaurant)
                restaurant  = Restaurant(restaurants['circuit']['circuitId'], item['name'], listProducts)
                listRestaurant.append(restaurant)
                listProducts = []
                    
        for typeItem in listRestaurant:
            for productItem in typeItem.productRestaurant:
                if productItem.typeproduct == 'food':
                    food = Food(typeItem.circuitId, typeItem.restaurantName, productItem.typeproduct, productItem.typeproductKind, productItem.nameItem, float(productItem.price))
                    listFood.append(food)
                
                elif productItem.typeproduct == 'drink':
                    drink = Drink(typeItem.circuitId, typeItem.restaurantName, productItem.typeproduct, productItem.typeproductKind, productItem.nameItem, float(productItem.price))
                    listDrink.append(drink)      
                               
        return listRestaurant, listFood, listDrink   



    def showListPilots(self, listPilots): #funcion para mostrar todos los pilotos en orden 
        for i,pilots in enumerate(listPilots):
            print('\n       ............',i+1,'............')
            pilots.showPilot()
            
    def showListBuilders(self, listBuilders): #funcion para mostrar todos los constructores en orden 
        for i,builders in enumerate(listBuilders):
            print('\n       ............',i+1,'............')
            builders.showBuilders()
            
    def showListCarRaces(self, listCarRaces): #funcion para mostrar todos las carreras en orden 
                for i, carRaces in enumerate(listCarRaces):
                    print('\n       ............',i+1,'............')
                    carRaces.showCarRace()
                    
    def showListCircuit(self, listCircuit): #funcion para mostrar todos los circuitos en orden 
                for i, circuit in enumerate(listCircuit):
                    print('\n       ............',i+1,'............')
                    circuit.showCircuit()

    def showListRestaurant(self, listRestaurant): #funcion para mostrar todos los restaurantes en orden 
                for i, restaurant in enumerate(listRestaurant):
                    print('\n       ............',i+1,'............')
                    restaurant.showRestaurant()
                    for product in restaurant.productRestaurant:
                        product.showProducts()
                     
    def showListFood(self, listFood): #funcion para mostrar todos la comida de restaurante en orden 
                for i, restaurant in enumerate(listFood):
                    print('\n       ............',i+1,'............')
                    restaurant.showFood()  
                                     
    def showListDrink(self, listDrink): #funcion para mostrar toda la bebida de los restaurantes en orden 
                for i, restaurant in enumerate(listDrink):
                    print('\n       ............',i+1,'............')
                    restaurant.showDrink()  
    

    
    
    def createListPilots(self): #funcion que retorna la lista con los pilotos
        dictionaryPilots = self.requestPilots()
        listPilotos = self.TransformListPilots(dictionaryPilots)
        return listPilotos
    
    def createListBuilders(self): #funcion que retorna la lista con los constructores
        dictionaryPilots = self.requestPilots()
        listPilotos = self.TransformListPilots(dictionaryPilots)
        dictionaryBuilders = self.requestBuilders()
        listBuilders = self.TransformListBuilders(dictionaryBuilders, dictionaryPilots)
        return listBuilders
    
    def createListCarRaces(self): #funcion que retorna la lista con las carreras
        dictionaryCarRaces = self.requestCarRaces()
        listCarRaces = self.TransformListCarRaces(dictionaryCarRaces)
        return listCarRaces 
    
    def createListCircuit(self): #funcion que retorna la lista con los cirucuitos
        dictionaryCarRaces = self.requestCarRaces()
        listCircuit = self.TransformListCircuit(dictionaryCarRaces)
        return listCircuit  

    def createListRestaurant(self): #funcion que retorna la lista con los restuarantes
        dictionaryCarRaces = self.requestCarRaces()
        listRestaurant, listFood, listDrink = self.TransformListRestaurant(dictionaryCarRaces)
        return listRestaurant, listFood, listDrink



    def validateCarRace(self, listCarRaces):  # Funcion para validar que existe la carrera que se va a comprar el ticket
        while True:
            checkCarRace = input('\nIngrese el nombre o el id del circuito de la carrera que desea ver: ').lower()
            for race in listCarRaces:
                if race.name == checkCarRace.title() or race.circuitId == checkCarRace:      
                    return race.name
            else:
                print('\nError! Carrera no encontrada!\n')       
    
    def validateFinishPodium(self, listCarRaces): # Funcion para validar que todas las carrera han sido terminadas
        validate = True
        for race in listCarRaces:
            if race.podium == 'No establecido':
                validate = False
                print('\nTodavia no se han jugado todas la carreras!\n')
                return validate
            
        else:
            print('\nYa se jugaron todas la carreras!\n')
            return validate
                                                     
    def validateListTicket(self, listTicketGeneral, listTicketVIP, listTicket, listCarRaces): #funcion para verifica y apendear el ticket a una lista 
        print('\nLista de carreras: ')
        for i,car in enumerate(listCarRaces):
            print(f'''
        Carrera N°{i+1}:
        -Nombre: {car.name}     
        -Circuito ID: {car.circuitId}
                  ''')
            
        checkCarRace = self.validateCarRace(listCarRaces)
        print('\n')
        
        objectTicketGeneral, objectTicketVIP = TicketRegister().createTicket(checkCarRace, listTicket, listTicketGeneral, listTicketVIP, listCarRaces)
        
        if objectTicketGeneral == [] and objectTicketVIP == []:
            pass
        
        elif objectTicketGeneral != [] and objectTicketVIP == []:
            objectTicketGeneral.ticketId += str(random.randint(10000, 90000)) + str(len(listTicketGeneral))

            listTicketGeneral.append(objectTicketGeneral)
            listTicket.append(objectTicketGeneral)
            print(objectTicketGeneral.showEntranceTicket())   
            print('\nTicket Registrado con exito!\n')
            
        elif objectTicketVIP != [] and objectTicketGeneral == []:
            objectTicketVIP.ticketId += str(random.randint(10000, 90000)) + str(len(listTicketVIP))
            listTicketVIP.append(objectTicketVIP)
            listTicket.append(objectTicketVIP)
            print(objectTicketVIP.showEntranceTicket())
            print('\nTicket Registrado con exito!')   
        
        return listTicketGeneral, listTicketVIP, listTicket

    def validateRestaurant(self, listTicketVIP, listCarRaces): #Funcion para verificar que el cliente existe y pertenece al restaurante
        print('\nLista de cedulas VIP:')
        for i,ticket in enumerate(listTicketVIP):
            print(f'Cedula N°{i+1}: {ticket.dni}')
        validate = False
        while True:
            if listTicketVIP == []:
                print('\nNo existen usuario registrados en VIP!\n')
                return False, False
            
            else:
                dni = input('\nIngrese su cedula del ticket para la validacion: ')
                for carRace in listCarRaces:
                    for user in listTicketVIP:
                        if carRace.name == user.validateCarRace:
                            if user.dni == dni:
                                validate = True
                                return user.ticketId, carRace.circuitId
                    
                if validate == False:
                    print('\nNo existe ese usuario registrado! Asegurese de colocar la cedula sin simbolos numericos\n')
                                      
           
    def validateDni(self, listTicket):  #funcion que verificar que no se repita la cedula 
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
            value = True

    def validateTicket(self, listTicket): #funcion para validar que el ticket comprado sea valido
        print('\nLista de tickets:\n')
        for i, security in enumerate(listTicket):
            print(f'Ticket N°{i+1}: {security.ticketId}')
        
        validateID = input('\nIngrese su ID de validacion que sale en su boleto: ')
        while True:
            for ticket in listTicket:
                if ticket.ticketId == validateID:
                    if ticket.usedTicket == False:                    
                        ticket.usedTicket = True
                        return validateID
                    else:
                        print('\nBoleto ya usado, no se puede volver a usar!\n')
                        return False
                    
            print('\nTicket no registrado en el sistema, intentelo nuevamente!\n')
            validateID = input('\nIngrese su ID de validacion que sale en su boleto: ')
            
    def validateTicketCarRace(self, listTicket): #Funcion para validar que el ticket pertenezca a su carrera correspondiente
        validateID = self.validateTicket(listTicket)
        if validateID == False:
            return False
        
        for ticket in listTicket:
            if ticket.ticketId == validateID:
                checkCarRace = ticket.validateCarRace
                return checkCarRace
                       
      
      
                        
    def foundBuilders(self, listBuilders): # Funcion para comprobar y ver que existe el constructor buscada
        validate = False
        while True:
            print('\nLista de nacionalidades disponibles:\n ')
            listBuilderNew = []
            for builder in listBuilders:
                listBuilderNew.append(builder.nationality) 
            for i,builder in enumerate(list(set(listBuilderNew))):
                print(i+1,builder)
            checkBuildes = input('\nIngrese la nacionalidad del contructor que desea ver: ').lower()
            for i,builder in enumerate(listBuilders):
                if builder.nationality == checkBuildes.title():
                    validate = True
                    print(f'\nConstructor N°{i+1} encontrado con exito!\n')
                    builder.showBuilders()
                    
            if validate == True:
                break
                
            else:
                print('\nError! Constructor no encontrado!\n')   
    
    def foundPilots(self, listPilots, listBuilders): # Funcion para comprobar y ver que existe el piloto buscada
        validate = False
        while True:
            print('\nLista de codigos de referencia al piloto disponibles por constructor: \n')
            for i, builder in enumerate(listBuilders):
                print('\nConstructor N°',i+1)
                for pilot in builder.referencePilots:
                    print('Piloto:',pilot)
            checkPilots = input('\nIngrese la referencia del piloto que aparece en el constructor para buscarlo: ').lower()
            for i,pilot in enumerate(listPilots):
                if pilot.pilotId == checkPilots:
                    validate = True
                    print(f'\nPiloto N°{i+1} encontrado con exito!\n')
                    pilot.showPilot()
                                
            if validate == True:
                break
                
            else:
                print('\nError! Piloto no encontrado!\n') 
                
    def foundCarRace(self, listCircuit, listCarRaces):  # Funcion para comprobar y ver que existe la carrera buscada por circuito
        validate = False
        while True:
            print('\nLista de paises donde se correran las carreras: \n')
            for i,circuit in enumerate(listCircuit):
                print(i+1,circuit.country)
            checkCarRace = input('\nIngrese el pais donde se correra la carrera que desea ver: ').lower()
            for circuit, race in zip(listCircuit, listCarRaces):
                if circuit.country.lower() == checkCarRace:
                    validate = True
                    print(f'\nCarrera N°{race.round} encontrada con exito!\n')
                    race.showCarRace()
                    
            if validate == True:
                break
                
            else:
                print('\nError! Carrera no encontrada!\n')   
        
    def foundTimeCarRace(self, listCarRaces): # Funcion para ver las carreras que ocurren en un mes
        validate = False
        while True:
            print('\nLas fechas donde se realizaran las carreras son: \n')
            for car in listCarRaces:
                print(f'\nFecha de la Carrera N°{car.round}:\n{car.date}')
                
            checkCarRace = input('\nIngrese el mes en numeros en el que se desea ver las carreras que se daran: ')
            if len(checkCarRace) == 1:
                checkCarRace = '0' + checkCarRace
            for race in listCarRaces:
                date = race.date.split('-')
                if date[1] == checkCarRace:
                    validate = True
                    print(f'\nCarrera N°{race.round} encontrada con exito!\n')
                    race.showCarRace()
                        
            if validate == True:
                break
                
            else:
                print('\nError! Carrera no encontrada! Recuerde colocar el mes en numeros!\n')  

                
    def foundRestaurantName(self, listRestaurant):# Funcion que busca los restaurantes por el nombre
        value = False
        print('\nLista de nombres de restaurantes: \n')
        for i, restaurant in enumerate(listRestaurant):
            print(f'{i+1}.{restaurant.restaurantName}')
        while True:
            restaurantName = input('\nIngresa el nombre del restaurante: ')
            for i, restaurant in enumerate(listRestaurant):
                if restaurant.restaurantName.lower() == restaurantName.lower():
                    print('\n       ............',i+1,'............')
                    restaurant.showRestaurant()
                    for product in restaurant.productRestaurant:
                        product.showProducts()
                    value = True
            if value == True:
                print('\nProductos de restaurante encontrados con exito!')
                break
            
            print('\nError! Restaurante no encontrado!\n')
    
    def foundProductName(aelf, listRestaurant): #Funcion que busca los productos por nombre
        value = False
        print('\nLista de nombres de productos:\n')
        for i, restaurant in enumerate(listRestaurant):
            for product in restaurant.productRestaurant:
                print(f'{i+1}.{product.nameItem}')
        while True:
            productName = input('\nIngresa el nombre del producto que se desea buscar: ')
            for i, restaurant in enumerate(listRestaurant):
                for product in restaurant.productRestaurant:
                    if product.nameItem.lower() == productName.lower():
                        print(f'\nRestaurante N°{i+1}: {restaurant.restaurantName}')
                        product.showProducts()
                        value = True
            
                    
            if value == True:
                print('\nProductos encontrados con exito!')
                break 
            
            print('\nError! Producto no encontrado!\n')
    
    def foundRestaurantType(self, listFood, listDrink): # Funcion que busca los restaurantes por el tipo de comida\bebida
        while True:
            option = input('''\nIngresa la clase de producto que busca: 
                           
                                1. Comida
                                2. Bebida
                                Opcion: ''')
                                
            if option == '1':
                option2 = input('''\nIngresa el tipo de comida: 
                                
                                    1. Preparacion restaurante.
                                    2. Empaque rapido.
                                    Opcion: ''')
                if option2 == '1':
                    productType = 'restaurant'
                    for food in listFood:
                        if food.foodType == productType:
                            food.showFood()
                    break
                            
                    
                    
                elif option2 == '2':
                    productType = 'fast'
                    for food in listFood:
                        if food.foodType == productType:
                            food.showFood()
                    break
                            
        
                    
                else: 

                    print('\nOpcion incorrecta!\n')
                    
                    
            elif option == '2':
                productType = input('''\nIngresa el tipo de bebida:
                                     
                                    1. Alcoholica.
                                    2. No alcoholica.
                                    Opcion: ''')
                
                if productType == '1':
                    productType = 'alcoholic'
                    for drink in listDrink:
                        if drink.drinkType == productType:
                                drink.showDrink()
                    break
                
                    
                elif productType == '2':
                    productType = 'not-alcoholic'
                    for drink in listDrink:
                        if drink.drinkType == productType:
                            drink.showDrink()
                    break
                
                    
                else: 
                    print('\nOpcion incorrecta!\n')
                
                
            else:
                print('\nOpcion incorrecta!\n')   
    
    def foundRestaurantPrice(self, listRestaurant): # Funcion que busca los restaurantes por el rango de precio
        value = False
        print('\nLista de precios por producto:\n')
        for i, restaurant in enumerate(listRestaurant):
            for product in restaurant.productRestaurant:
                print(f'Precio N°{i+1}: {product.price}')
        
        while True:
            productPrice = input('\nIngresa el precio del producto: ')
            while not productPrice.isnumeric():
                productPrice = input('\nError! Ingresa un numero entero: ')
                
            for i, restaurant in enumerate(listRestaurant):
                for product in restaurant.productRestaurant:
                    if int(product.price) == int(productPrice):
                        print(f'\nRestaurante N°{i+1}: {restaurant.restaurantName}')
                        product.showProducts()
                        value = True
            
                    
            if value == True:
                print('\nProductos encontrados con exito!')
                break 
            
                
            print('\nError! Producto no encontrado!\n')
    

    def winnerPodium(self, listCarRaces, listPilots): # Funcion que muestra el ganador de la carrera por podium
        print('\nLista de carreras: \n')
        for carRace in listCarRaces:
            print(f'\nCarrera N°{carRace.round}\nNombre de la carrera: {carRace.name} \nID de la Carrera: {carRace.circuitId}')
            
        validateRace = self.validateCarRace(listCarRaces)
        self.listWinnerRaceCar = True
        newListPilots = listPilots
        
        for race in listCarRaces:
            if race.name == validateRace.title() or race.circuitId == validateRace.lower():
                if race.podium != 'Carrera Terminada':
                    race.podium = 'Carrera Terminada'
                    random.shuffle(newListPilots)
                    print('\n\nLos 10 primeros puestos de esta carrera fueron ganados por los siguientes corredores: \n\n')
                    for i, pilot in enumerate(newListPilots):
                        
                        if i == 0:
                            pilot.pointCarRace += 25
                            print('Felicidades quedo en el primer lugar!')
                            pilot.showPilot()

                            
                        elif i == 1:  
                            pilot.pointCarRace += 18
                            print('Felicidades quedo en el segundo lugar!')
                            pilot.showPilot()
                            
                        elif i == 2:
                            pilot.pointCarRace += 15
                            print('Felicidades quedo en el tercer lugar!')
                            pilot.showPilot()
                            
                        elif i == 3:
                            pilot.pointCarRace += 12
                            print(f'Su puesto de calificacion es: N°{i+1}')
                            pilot.showPilot()

                            
                        elif i == 4:
                            pilot.pointCarRace += 10
                            print(f'Su puesto de calificacion es: N°{i+1}')
                            pilot.showPilot()
                            
                        elif i == 5:
                            pilot.pointCarRace += 8
                            print(f'Su puesto de calificacion es: N°{i+1}')
                            pilot.showPilot()
                            
                        elif i == 6:
                            pilot.pointCarRace += 6
                            print(f'Su puesto de calificacion es: N°{i+1}')
                            pilot.showPilot()   
                            
                        elif i == 7:
                            pilot.pointCarRace += 4
                            print(f'Su puesto de calificacion es: N°{i+1}')
                            pilot.showPilot()
                            
                        elif i == 8:
                            pilot.pointCarRace += 2
                            print(f'Su puesto de calificacion es: N°{i+1}')
                            pilot.showPilot()
                            
                        elif i == 9:
                            pilot.pointCarRace += 1
                            print(f'Su puesto de calificacion es: N°{i+1}')
                            pilot.showPilot() 
                    return True
        print('\nYa se jugo esa carrera!\n')
        return False

    def winnerFinishTotal(self, listCarRaces, listPilots): #Funcion para terminar todas las carreras
        self.listWinnerRaceCar = True
        for car in listCarRaces:
            if car.podium == 'No establecido':
                car.podium = 'Carrera Terminada'
                newListCarRace = listPilots
                random.shuffle(newListCarRace)
                print(f'\nLos resultados de la carrera {car.round}:\n')
                for i, pilot in enumerate(newListCarRace):
                    if i == 0:
                        pilot.pointCarRace += 25
                        pilot.showPilot()
    
                    elif i == 1:
                        pilot.pointCarRace += 18
                        pilot.showPilot()
                        
                    elif i == 2:
                        pilot.pointCarRace += 15
                        pilot.showPilot()
                        
                    elif i == 3:
                        pilot.pointCarRace += 12
                        pilot.showPilot()
                        
                    elif i == 4:
                        pilot.pointCarRace += 10
                        pilot.showPilot()
                        
                    elif i == 5:
                        pilot.pointCarRace += 8 
                        pilot.showPilot()
                        
                    elif i == 6:
                        pilot.pointCarRace += 6 
                        pilot.showPilot()
                        
                    elif i == 7:
                        pilot.pointCarRace += 4
                        pilot.showPilot()
  
                    elif i == 8:
                        pilot.pointCarRace += 2
                        pilot.showPilot()
                        
                    elif i == 9:
                        pilot.pointCarRace += 1
                        pilot.showPilot()
           

    def showPilotWinner(self, listPilots): #Funcion que muestra el piloto ganador de la formula-1
        pilotWinner = 0
        for pilot in listPilots:
            if pilot.pointCarRace >= pilotWinner:
                pilotWinner = pilot.pointCarRace
        for pilot in listPilots:
            if pilot.pointCarRace == pilotWinner: 
                print('\nPiloto Ganador 🏆')
                print('\nEl Piloto ganador de la final de formula-1 es: \n')
                pilot.showPilot()
        
    def showBuilderWinner(self, listBuilders, listPilots): #Funcion que muestra el constructor ganador de la formula-1
        winner = 0

        if self.validate == True:
            for builder in listBuilders:
                for pilot in listPilots:
                    if pilot.pilotId == builder.referencePilots[0]:
                        builder.pointCarRace += pilot.pointCarRace
                    elif pilot.pilotId == builder.referencePilots[1]:
                        builder.pointCarRace += pilot.pointCarRace
                self.validate = False   
                        
        for win in listBuilders:
            if win.pointCarRace >= winner:
                winner = win.pointCarRace
                
        for builderWinner in listBuilders:
            if builderWinner.pointCarRace == winner:
                print('\nConstructor Ganador 🏆')
                print('\nEl Constructor ganador de la final de formula-1 es: \n')
                builderWinner.showBuilders()


    def watchCarRace(self, validateCarRace, listTicket, listCarRaces):#Funcion para "ver la carrera" para el cliente
        for ticket in listTicket:
            for carRace in listCarRaces:
                if ticket.ticketId == validateCarRace:
                    if carRace.name == ticket.validateCarRace:
                        carRace.showCarRace()
                        carRace.asistence += 1



    def mostAssistedRace(self, listCarRaces, listTicket): #Funcion de estadisticas para ver la carrera con mas asistencia
        countMostAssistedRace = []
        value = False
        for car in listCarRaces:
            for ticket in listTicket:
                if ticket.validateCarRace == car.name:
                    if ticket.usedTicket == True:
                        countMostAssistedRace.append(car.name)
                        value = True
        if value == True:
            print(f'\nLa carrera con mayor asistencia por ahora es: {statistics.mode(countMostAssistedRace)}')
                        
    def carRaceBestSellers(self, listCarRaces, listTicket): #Funcion de estadisticas para ver la carrera con mas boletos comprados
        value = False
        self.countcarRaceBestSellers = []
        for car in listCarRaces:
            for ticket in listTicket:
                if ticket.validateCarRace == car.name:
                    self.countcarRaceBestSellers.append(car.name)
                    value = True
                    
        if value == True:
            print(f'\nLa carrera con mayor boletos vendidos por ahora es: {statistics.mode(self.countcarRaceBestSellers)}')
      
    def averageVIPSpend(self, listTicketVIP, listCarRaces): # Funcion de estadisticas para calcular el promedio de gastos VIP
        count = 0
        lenCount = 0 
        for i, carRace in enumerate(listCarRaces):
            print(f'{i+1}. Nombre: {carRace.name} \n    ID: {carRace.circuitId}\n')
            
        check = self.validateCarRace(listCarRaces) 
        for ticket in listTicketVIP:
            if ticket.validateCarRace == check:
                count += ticket.spentMoney
                lenCount += 1
        if lenCount == 0:
            print('No existen clientes VIP que compraron en esa carrera!')   
        else:    
            print(f'Carrera: {check}\nEL Promedio de gasto de un cliente VIP en la carrera: {count/lenCount}')
    
    def topSellingProducts(self, listRestaurantProducts): #Funcion de estadistica para buscar el top 3 productos mas comprados
        topProducts = []
        for productRestaurant in listRestaurantProducts:
            for products in productRestaurant.listBuyProduct:
                for key, value in products.items(): 
                    products = (key+',')*value
                    topProducts.extend(str(products)[:-1].split(','))
        print('\nEl top de productos mas comprados es:')
        print(f'Top N°1 es: {statistics.mode(topProducts)}')
        top1 = statistics.mode(topProducts)
        for top in topProducts:
            if top == top1:
                topProducts.remove(top)
        if len(topProducts) == 0:
            print(topProducts)
            print('\nNo existen mas productos que se hayan comprado!')   
        else:   
            print(f'Top N°2 es: {statistics.mode(topProducts)}')
            top2 = statistics.mode(topProducts)
            for top in topProducts:
                if top == top2:
                    topProducts.remove(top)
                    
            if len(topProducts) == 0:
                print('\nNo existen mas productos que se hayan comprado!') 
                 
            else:   
                print(f'Top N°3 es: {statistics.mode(topProducts)}')        

    def topClient(self, listTicket): #Funcion de estadistica para buscar el top 3 de clientes que mas compraron ticket por su nombre
        topClients = []
        for ticket in listTicket:
            topClients.append(ticket.name)
        print('\nEl numero de boletos comprados se determina por el nombre!')  
        print('\nEl top 3 de clientes que mas compraron boletos son:\n')
        print(f'Top N°1 es: {statistics.mode(topClients)}')
        
        top1 = statistics.mode(topClients)
        for top in topClients:
            if top == top1:
                topClients.remove(top)
        if len(topClients) == 0:
                print('\nNo existen mas productos que se hayan comprado!') 
        else:       
            print(f'Top N°2 es: {statistics.mode(topClients)}')
            top2 = statistics.mode(topClients)
            for top in topClients:
                if top == top2:
                    topClients.remove(top)
                    
            if len(topClients) == 0:
                print('\nNo existen mas productos que se hayan comprado!') 
            else:        
                print(f'Top N°3 es: {statistics.mode(topClients)}')        

    def asistenceCarRace(self, listCarRaces, listTicket): #Funcion de estadistica de relacion tickets vendidos y precio
        countAssistedRace = []
        for ticket in listTicket:
            if ticket.usedTicket == True:
                countAssistedRace.append(ticket.validateCarRace)
                        
        countAssistedRace.sort()
        print('\nOrden de lugares:')
        for carRace in listCarRaces:
            for asistence in set(countAssistedRace):
                if carRace.name == asistence:
                    carRace.showCarRace()
             
        print('\n\nRelacion aisistencia venta:')
        print(f'\nTickets Vendidos: {len(listTicket)}')
        print(f'\nTickets con Asistencia en esta carrera: {len(countAssistedRace)}')
        print(f'\nEl total de asistencia en porcentaje por todos los boletos vendidos es de: {(len(countAssistedRace)*100)/len(listTicket)}%')
                   
                   
                                  
    
                             
    def menu(self): #menu principal de la aplicacion
        self.getData()
        listPilots = self.createListPilots()
        listBuilders = self.createListBuilders()
        listCarRaces = self.createListCarRaces()
        listCircuit = self.createListCircuit()
        listRestaurant, listFood, listDrink = self.createListRestaurant() 


        self.listTicket.extend(self.listTicketVIP)
        self.listTicket.extend(self.listTicketGeneral)
        listTicket = self.listTicket
        listTicketGeneral = self.listTicketGeneral
        listTicketVIP = self.listTicketVIP
        listWinners = []
        finishCarRace = False
        new = '''
        Todavia no han comenzado las carreras!
        Toca la Opcion-6 para comenzar con la carrera!
        
        PD: Recuerda comprar tu entrada antes de comenzar la carrera!
        '''
        count = 1
        
        print('''
        Bienvenido a nuestro sitio Web!
        
        Aquí encontrarás toda la información relacionada con la Formula-1! 
            ''')
        print('''

                     ⢀⣀⣀⣀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                     ⢸⣿⣿⡿⢀⣠⣴⣾⣿⣿⣿⣿⣇⡀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                     ⢸⣿⣿⠟⢋⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⡿⠓⡐⠒⢶⣤⣄⡀⠀⠀
                     ⠸⠿⠇⢰⣿⣿⡆⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⡷⠈⣿⣿⣉⠁⠀
                     ⠀⠀⠀⠀⠈⠉⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠈⠉⠁⠀⠈⠉⠉⠀⠀
                 
        ███████  ██████  ██████  ███    ███ ██    ██ ██       █████       ██ 
        ██      ██    ██ ██   ██ ████  ████ ██    ██ ██      ██   ██     ███ 
        █████   ██    ██ ██████  ██ ████ ██ ██    ██ ██      ███████      ██ 
        ██      ██    ██ ██   ██ ██  ██  ██ ██    ██ ██      ██   ██      ██ 
        ██       ██████  ██   ██ ██      ██  ██████  ███████ ██   ██      ██ 


''')
        while True:
            option = input(f'''
                           
        ------------------------------------------------------------------
          {new}  
        ------------------------------------------------------------------
          
          
        Seleccione el número de la opción que quiere elegir:

        1. Ver pilotos, constructoes, carreras y circuitos de la formula-1
        2. Buscar pilotos, constructores y carreras.
        3. Comprar un ticket.
        4. Restaurantes VIP.
        5. Ver las carreras.
        6. Comenzar las carreras.
        7. Ver resultados de la carreras (Necesita ver todas las carreras).
        8. Estadísticas.
        9. Ver Tickets Registrados.
        10. Salir.

        Opción seleccionada: ''')
            
            if option == '1':
                while True:
                    option2 = input('''
                                    Ingrese la opcion que desea:
                                    
                                    1. Ver constructores.
                                    2. Ver pilotos.
                                    3. Ver carreras.
                                    4. Ver circuitos.
                                    5. Volver al menu.
                                    
                                    Opcion: ''')
                    
                            
                    if option2 == '1':
                        self.showListBuilders(listBuilders)
                        
                    elif option2 == '2':
                        self.showListPilots(listPilots)
                            
                    elif option2 == '3':
                        self.showListCarRaces(listCarRaces)
                        
                    elif option2 == '4':
                        self.showListCircuit(listCircuit)   
                    
                    elif option2 == '5':
                        print('\nGracias por visualizar la informacion!\n')   
                        break
                    
                    else:
                        print('\nOpcion incorrecta!\n')                         
       
                           
            elif option == '2':
                while True:
                    option2 = input('''
                                    Ingrese la opcion que desea:
                                    
                                    1. Buscar constructores por pais.
                                    2. Buscar pilotos por constructor.
                                    3. Buscar a las carreras por país del circuito.
                                    4. Buscar carreras que se jugaran en un mes especifico.
                                    5. Volver al menu.
                                    
                                    Opcion: ''')
                    
                    if option2 == '1':
                        self.foundBuilders(listBuilders)
                        
                    elif option2 == '2':
                        self.foundPilots(listPilots, listBuilders)
                        
                        
                    elif option2 == '3':
                        self.foundCarRace(listCircuit, listCarRaces)
                    
                    elif option2 == '4':
                        self.foundTimeCarRace(listCarRaces)
                    
                    elif option2 == '5':
                        print('\nGracias por su tiempo de busqueda!\n')
                        break
                    
                    else:
                        print('\nOpcion incorrecta!\n')
             
                              
            elif option == '3':
                listTicketGeneral, listTicketVIP, listTicket = self.validateListTicket(listTicketGeneral, listTicketVIP, listTicket, listCarRaces)
    
                
            elif option == '4':
                while True:
                    option2 = input('''
                                    Bienvenido a la seccion de restaurantes VIP!
                                    
                                    Ingrese la opcion que desea realizar: 
                                    
                                    1. Ver Restaurantes.
                                    2. Buscar en los restaurantes.
                                    3. Entrar al Restaurante y comprar al circuito correspondiente a su boleto VIP.
                                    4. Volver al menu.
                                    
                                    Opcion: ''')
                    
                    if option2 == '1':
                        while True:
                            option3 = input('''
                                      Ingrese la opcion que desea:
                                      
                                      1. Ver todos los Restaurantes.
                                      2. Ver Restaurantes con Comida. 
                                      3. Ver Restaurantes con Bebida.
                                      4. Volver al menu de restaurantes.
                                      
                                      Opcion: ''')
                            
                            if option3 == '1':
                                self.showListRestaurant(listRestaurant)
                                
                            elif option3 == '2':  
                                self.showListFood(listFood)
                                
                            elif option3 == '3':
                                self.showListDrink(listDrink)
                                
                            elif option3 == '4':
                                print('\nGracias por su visita!\n')
                                break
                            
                            else:
                                print('\nOpcion incorrecta!\n')
                        
                    elif option2 == '2':
                        while True:
                            option3 = input('''
                                      Ingrese la opcion que desea:
                                      
                                      1. Buscar productos por el nombre del restaurante.
                                      2. Buscar productos por su nombre.
                                      3. Buscar productos por su tipo. 
                                      4. Buscar productos por tipo de precio.
                                      5. Volver al menu de restaurantes.
                                      
                                      Opcion: ''')
                            
                            if option3 == '1':
                                self.foundRestaurantName(listRestaurant)
                            
                            elif option3 == '2':
                                self.foundProductName(listRestaurant)
                                
                            elif option3 == '3':  
                                self.foundRestaurantType(listFood, listDrink)
                                
                            elif option3 == '4':
                                self.foundRestaurantPrice(listRestaurant)
                                
                            elif option3 == '5':
                                print('\nGracias por su visita!\n')
                                break
                            else:
                                print('\nOpcion incorrecta!\n')
                    
                    elif option2 == '3':
                        userID, carRaceID = self.validateRestaurant(listTicketVIP, listCarRaces)
                        if userID != False: 
                            listFoodProducts, listDrinkProducts = RestaurantManage().buyRestaurant(listTicketVIP, userID, listFood, listDrink, listRestaurant, carRaceID)
                            self.listFood.extend(listFoodProducts)
                            self.listDrink.extend(listDrinkProducts)
                            self.listRestaurantProducts.extend(self.listFood)
                            self.listRestaurantProducts.extend(self.listDrink)
                            if listFood != [] or listDrink != []:
                                self.safe = True
                            
                            
                    elif option2 == '4':
                        print('\nGracias por visualizar nuestro restaurantes!\n')
                        break
                    
                    else:
                        print('\nOpcion incorrecta!\n')
    
                
            elif option == '5':
                if listTicket == []:
                    print('\nNo existen tickets registrados! ')
                    
                else:
                    print('\nBienvendio al estadio de formula-1!\n')
                    
                    validateTicket = self.validateTicket(listTicket)
                    
                    if validateTicket != False:
                        self.watchCarRace(validateTicket, listTicket, listCarRaces)
                        print('\nGracias por su vista, espero que haya disfrutado de la carrera!\n')
                    else:
                        print('\nSi desea ver la carrera de nuevo le recomendamos comprar otro ticket en la tienda!\n')
                           
                       
            elif option == '6':
                while True:
                    option2 = input('''
                                    Ingrese una opcion:
                                    
                                    1. Comenzar todas las carreras.
                                    2. Comenzar una sola carrera especifica.
                                    3. Volver al menu
                                    Opcion: ''')
                    
                    if option2 == '1':
                        value = self.winnerFinishTotal(listCarRaces, listPilots)
                        if value == True:
                            new = f'''
                        
                        Todas las carreras han finalizado!
                        Puede verificar los ganadores en la opcion-7 del menu!
                                
                        Gracias por visualizar las carreras de la formula-1!
                        '''
                        else:
                            print('\nYa se jugaron todas las carreras!\n')
                            break
                
                    elif option2 == '2':
                        
                        if count > 1:
                            validate1 = self.validateFinishPodium(listCarRaces)
                            finishCarRace = validate1
                            
                        if finishCarRace == False:
                            listWinners = self.winnerPodium(listCarRaces, listPilots)
                            if listWinners == False:
                                pass
                            else:
                                new = f'''
                    La carrera N°{count} ya ha finalizado! 
                    Al finalizar puede verificar los ganadores en la opcion-7 del menu!
                            
                    Gracias por visualizar la carrera de la formula-1!
                            ''' 
                                
                                count += 1

                    elif option2 == '3':
                        print('\nGracias por la visita!\n')
                        break
                    
                    else:
                        print('\nError Opcion incorrecta!')
             
                        
            elif option == '7':  
                if self.listWinnerRaceCar == []:  
                    print('\nNo se ha jugado ninguna carrera!\n')   
                
                elif self.validateFinishPodium(listCarRaces) == False:
                    pass
                     
                
                else:         
                    while True:
                        option2 = input('''
                        Ingrese la opcion que desea:
                        
                        1. Ver Piloto Ganador
                        2. Ver Constructor Ganador.
                        3. Volver al menu.
                        
                        Opcion: ''')
                        
                        if option2 == '1':
                            self.showPilotWinner(listPilots)
                            
                        elif option2 == '2':
                            self.showBuilderWinner(listBuilders, listPilots)
                            
                        elif option2 == '3':
                            print('\nGracias por visualizar los ganadores!\n')
                            break
                    
                        else:
                            print('\nError! Opcion incorrecta\n')
              
                        
            elif option == '8':
                print('\nBienvenido a la seccion de estadisicas! ')
                while True:
                    option2 = input('''
                      Ingrese su opcion:
                      1. Ver promedio de gasto de un cliente VIP.
                      2. Ver tabla con la asistencia a las carreras de mejor a peor.
                      3. Ver la carrera con mayor asistencia.
                      4. Ver la carrera con mayor boletos vendidos.
                      5. Ver Top 3 productos más vendidos en el restaurante.
                      6. Ver Top 3 de clientes que mas compraron boletos.
                      7. Graficos.
                      8. Volver al menu
                      Opcion: ''')

                    if option2 == '1':
                        if listTicketVIP == []:
                            print('\nNo hay clientes VIP registrados!')
                        else:
                            self.averageVIPSpend(listTicketVIP, listCarRaces)
                        
                    elif option2 == '2':
                        if  listTicket == []:
                            print('\nNo se han visto carreras en este turno!\n')
                        
                        else:
                            self.asistenceCarRace(listCarRaces, listTicket)
                        
                    elif option2 == '3':
                        if listTicket == []:
                            print('\nNo existen clientes que hayan asistido a las carreras en este turno!\n')
                        else:
                            self.mostAssistedRace(listCarRaces, listTicket)
                            
                        
                    elif option2 == '4':
                        if listTicket == []:
                            print('\nNo existen boletos comprados en esta ronda!\n')
                            
                        else:
                            self.carRaceBestSellers(listCarRaces, listTicket)
                            
                    
                    elif option2 == '5':
                        if self.safe == False:
                            print('\nNo hay productos comprados en esta ronda!\n')  
                        else:
                            self.topSellingProducts(self.listRestaurantProducts)
                    
                    elif option2 == '6':
                        if listTicket == []:
                            print('\nNo hay usuarios registrados!\n')
                        else:
                            self.topClient(listTicket)
                    
                    elif option2 == '7':
                        print('\nLos graficos estan en construccion, proximamente se podran ver!\n')
                        
                    elif option2 == '8':
                        print('\nGracias por ver las estadisticas!\n')
                        break
                    
                    else:
                        print('\nError! Opcion incorrecta\n')
                        
                                           
            elif option == '9':
                print('\nEstos son los tickets registrados: ')
                for i in listTicket:
                    print(i.showEntranceTicket())
             
                    
            elif option == '10':
                print('\nGracias por su visita!\n')
                break
      
      
            else:
                print('\nError! Selecciona una opcion valida!\n')

        self.saveData(listTicketGeneral, listTicketVIP)



    