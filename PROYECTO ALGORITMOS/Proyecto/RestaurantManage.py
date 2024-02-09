from BuyProduct import BuyProduct

class RestaurantManage():
    def __init__(self):
        self.listProductFood = []
        self.listProductDrink = []
        self.listRestaurant = []
        self.listBuyRestaurantDrink = []
        self.listBuyRestaurantFood = []



    def showRestaurantCarRace(self, listRestaurant, carRaceID): # Funcion que busca los restaurantes de su respectiva carrera
        self.listRestaurant = []
        print('\nRestuarantes al que tiene acceso:\n')
        for i, restaurant in enumerate(listRestaurant):
            if restaurant.circuitId == carRaceID:
                print('\n       ............',i+1,'............')
                restaurant.showRestaurant()
                self.listRestaurant.append(restaurant)
                
    def viewListFood(self, listFood): # Funcion para ver y guardar los restaurantes de comida de la carrera
        newListFood = []
        for restaurant in self.listRestaurant:
            for food in listFood:
                if restaurant.restaurantName == food.restaurantName:
                    food.showFood()
                    newListFood.append(food)
        return newListFood
    
    def viewListDrink(self, listDrink): # Funcion para ver y guardar los restaurantes de bebida de la carrera
        newListDrink = []
        for restaurant in self.listRestaurant:
            for drink in listDrink:
                if restaurant.restaurantName == drink.restaurantName:
                    drink.showDrink()
                    newListDrink.append(drink)
        return newListDrink
    
    def perfectNumberDni(self,dni): # Funcion para verificar si la cedula es numero perfecto
        sum = 0
        dni = int(dni)
        for i in range(1,dni):
            if dni % i == 0:
                sum += i

        if sum == dni:
            return 0.15

        else:
            discount = 'No aplica'
            return discount
    
    
        
    def buyProductFood(self, listFood): # Funcion para comprar comida en el restaurante
        value = False
        print('\nLista con nombres de comida:\n ')
        for i, food in enumerate(listFood):
            print(f'{i+1}.{food.nameItem}')
        product = input('\nIngrese el nombre del producto que desea comprar: ')
        amountProduct = input('Ingrese la cantidad que desea comprar: ')
        while not amountProduct.isnumeric() or not 0 < int(amountProduct) <= 100:
            amountProduct = input('Error! Ingrese un numero entero positivo entre el 1 y 100: ')
        amountProduct = int(amountProduct)
        for food in listFood:
            if food.nameItem == product:
                food.amount += amountProduct
                food.inventory -= amountProduct
                self.listProductFood.append(food)
                food.showFood()
                value = True
                
                
        if value == False:
            print('\nEl producto que selecciono no existe!\n')
            return False
        
        else:
            option = input('\nDesea comprar algo mas:\n 1.Si \n (cualquier caracteres).No\n')
            if option == '1':
                self.buyProductFood(listFood)
                return True
                
            else:
                return True
            
    def buyProductDrink(self, listDrink, dni): # Funcion para comprar bebidas en el restaurante
        value = False
        print('\nLista con nombres de bebida:\n ')
        for i, drink in enumerate(listDrink):
            print(f'{i+1}.{drink.nameItem}')
        product = input('\nIngrese el nombre del producto que desea comprar: ')
        amountProduct = input('Ingrese la cantidad que desea comprar: ')
        while not amountProduct.isnumeric() or not 0 < int(amountProduct) <= 100:
            amountProduct = input('Error! Ingrese un numero entero positivo entre el 1 y 100: ')
        amountProduct = int(amountProduct)
            
        for drink in listDrink:
            if drink.nameItem == product:
                if drink.drinkType == 'alcoholic':
                    if int(dni) < 18:
                        drink.showDrink()
                        print('\nUsted es menor de edad y no puede comprar este producto!')
                        return False
                    
                    else:
                        self.listProductDrink.append(drink)
                        drink.amount += amountProduct
                        drink.inventory -= amountProduct
                        drink.showDrink()
                        value = True
                        
                elif drink.drinkType == 'not-alcoholic':
                        self.listProductDrink.append(drink)
                        drink.amount += amountProduct
                        drink.inventory -= amountProduct
                        drink.showDrink()
                        value = True
                        
        if value == False:
            print('\nEl producto que selecciono no existe!\n')
            return False

        
        else:
            option = input('\nDesea comprar algo mas:\n 1.Si \n (cualquier caracteres).No\n')
            if option == '1':
                self.buyProductDrink(listDrink, dni)
                return True
                
            else:
                return True           
            
    def buyRestaurant(self, listTicketVIP, userID, listFood, listDrink, listRestaurant, carRaceID): # Funcion para comprar productos e imprimir factura
        self.showRestaurantCarRace(listRestaurant, carRaceID)
        for user in listTicketVIP:
            if user.ticketId == userID:
                name = user.name
                dni = user.dni 
                age = user.age
        if self.listRestaurant == []:
            print('\nNo existen restaurantes para esta carrera!')  
            return [], []
        else: 
            while True:       
                product = input('''
                                Ingrese una opcion que desea comprar:
                                1. Comprar comida
                                2. Comprar bebida.
                                3. Salir del restaurante
                                Opcion: ''')
                
                if product == '1':
                    listFood = self.viewListFood(listFood)
                    if listFood == []:
                        print('\nEl restaurante no vende comida!\n')
                    else:
                        listBuyFood = []
                        while True:
                            value = self.buyProductFood(listFood)
                            if value == True:
                                priceTicket = 0
                                for food in set(self.listProductFood):
                                    priceTicket = food.price * food.amount 
                                    dictFood = {food.nameItem:food.amount}
                                    listBuyFood.append(dictFood)
                                discountPerfectNumber = self.perfectNumberDni(dni)
                                if discountPerfectNumber == 'No aplica':
                                    discount = 'No aplica'  
                                    priceIVA = priceTicket * 0.16
                                    subtotalPrice = priceTicket 
                                    totalPrice = subtotalPrice + priceIVA
                                else:    
                                    discount = priceTicket * discountPerfectNumber
                                    subtotalPrice = priceTicket - discount
                                    priceIVA = subtotalPrice * 0.16
                                    totalPrice = subtotalPrice + priceIVA
                                    
                                buyFood = BuyProduct(name, dni, age, listBuyFood, discount, subtotalPrice, priceIVA, totalPrice)
                                listShopping = []
                                for i, product in enumerate(listBuyFood):
                                    for key, value in product.items():
                                        products = f'{i+1}. {key}: {value}\t'
                                        listShopping.append(products)
                                print(f'''
                        -----------------------------------
                                    FACTURA 
                        -----------------------------------
                        Nombre: {name}
                        Cedula: {dni}
                        Edad: {age}                        
                        Descuento: {discount}
                        Productos comprados:''')
                                for shopping in listShopping:
                                    print(f'''                        {shopping}''')
                                
                                buyFood.showProducts()
                                
                                option = input('\nDesea proceder con la compra: \n 1.Si \n (cualquier caracteres).No\nOpcion: ')
                                if option == '1':
                                    print('\nGracias por comprar los productos de comida!\n')
                                    for ticket in listTicketVIP:
                                        if ticket.dni == dni:
                                            ticket.spentMoney += totalPrice
                                    for food in self.listProductFood:
                                        food.inventory = 0
                                    self.listProductFood = []
                                    self.listBuyRestaurantFood.append(buyFood)
                                    break
                                    
                                
                                else:
                                    for food in self.listProductFood:
                                        food.amount = 0
                                        food.inventory = 0
                                    self.listProductFood = []
                                    print('\nGracias por ver los productos de comidas!\n')
                                    break 
                            
                            elif value == False:
                                continue
                            
                                
                elif product == '2':
                    listDrink = self.viewListDrink(listDrink)
                    if listDrink == []:
                        print('\nEl restaurante no vende bebidas!\n')
                    else:   
                        listBuyDrink = []
                        listBuy = []
                        while True:
                            value = self.buyProductDrink(listDrink, dni)
                            if value == True:
                                priceTicket = 0
                                for drink in set(self.listProductDrink):
                                    priceTicket = drink.price * drink.amount
                                    listBuy.append(drink.nameItem)
                                    dictDrink = {drink.nameItem:drink.amount}
                                    listBuyDrink.append(dictDrink)
                                discountPerfectNumber = self.perfectNumberDni(dni)
                                if discountPerfectNumber == 'No aplica':
                                    discount = 'No aplica'  
                                    priceIVA = priceTicket * 0.16
                                    subtotalPrice = priceTicket 
                                    totalPrice = subtotalPrice + priceIVA
                                else:    
                                    discount = priceTicket * discountPerfectNumber
                                    subtotalPrice = priceTicket - discount
                                    priceIVA = subtotalPrice * 0.16
                                    totalPrice = subtotalPrice + priceIVA
                                
                                buyDrink = BuyProduct(name, dni, age, listBuyDrink, discount, subtotalPrice, priceIVA, totalPrice)
                                listShopping = []
                                for i, product in enumerate(listBuyDrink):
                                    for key, value in product.items():
                                        products = f'{i+1}. {key}: {value}\t'
                                        listShopping.append(products)
                                print(f'''
                        -----------------------------------
                                    FACTURA 
                        -----------------------------------
                        Nombre: {name}
                        Cedula: {dni}
                        Edad: {age}                        
                        Descuento: {discount}
                        Productos comprados:''')
                                for shopping in listShopping:
                                    print(f'''                        {shopping}''')
                                        
                                buyDrink.showProducts()
                                
                                option = input('\nDesea proceder con la compra: \n 1.Si \n (cualquier caracteres).No\nOpcion: ')
                                if option == '1':
                                    print('\nGracias por comprar los productos de bebida!\n')
                                    for ticket in listTicketVIP:
                                        if ticket.dni == dni:
                                            ticket.spentMoney += totalPrice
                                    for drink in self.listProductDrink:
                                        drink.inventory = 0
                                    self.listProductDrink = [] 
                                    self.listBuyRestaurantDrink.append(buyDrink)
                                     
                                    break
                                
                                else:
                                    for drink in self.listProductDrink:
                                        drink.inventory = 0
                                    self.listProductDrink = []
                                    print('\nGracias por ver los productos de bebida!\n')
                                    break 
                            
                            elif value == False:
                                break

                elif product == '3':
                    print('\nGracias por su visita!\n')
                    return self.listBuyRestaurantFood, self.listBuyRestaurantDrink
                else:
                    print('\nOpcion incorrecta!\n')
                    
        
                
            
        