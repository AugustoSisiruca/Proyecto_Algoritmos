class BuyProduct():
    def __init__(self, name, dni, age, listBuyProduct, discount, subtotalPrice, priceIVA, totalPrice):
        self.name = name
        self.dni = dni
        self.age = age
        self.listBuyProduct = listBuyProduct
        self.discount = discount 
        self.subtotalPrice = subtotalPrice
        self.priceIVA = priceIVA
        self.totalPrice = totalPrice

            

                
                         
    def showProducts(self): #Funcion que imprime la factura
        print(f'''                        
                        -----------------------------------
                        SUBTOTAL: {self.subtotalPrice}
                        Impuesto por IVA: {self.priceIVA}
                        
                        El impuesto al IVA incluye el 16% de  
                        la compra total
                        
                        -------------------------------------
                        TOTAL: {self.totalPrice}
                        -------------------------------------
                    ''')
        
        