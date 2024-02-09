
class BuyTicket():
    def __init__(self, ticketObject, discount, subtotalPrice, vatTax, totalPrice):
        self.ticketObject = ticketObject
        self.discount = discount
        self.subtotalPrice = subtotalPrice
        self.vatTax = vatTax
        self.totalPrice = totalPrice
            
            
    
    
    def showPreviewBill(self): # Funcion que imprime factura
        print(f'''
                Aplicando todos los descuentos y el IVA, 
                el precio de su entrada cuesta: {self.totalPrice}$
                ''')
          
    def showBillGeneral(self): # Funcion que imprime factura
        print(f'''
                -----------------------------------
                            FACTURA
                -----------------------------------
                Nombre: {self.ticketObject.name}
                Cedula: {self.ticketObject.dni}
                Edad: {self.ticketObject.age}
                Carrera: {self.ticketObject.validateCarRace}
                Asiento: {self.ticketObject.generalRaceSeat}
                Ticket ID: {self.ticketObject.ticketId}
                Ticket Usado: {self.ticketObject.usedTicket}
                Descuento: {self.discount}$
                
                -----------------------------------
                SUBTOTAL: {self.subtotalPrice}$
                Impuesto por IVA: {self.vatTax}$
                
                El impuesto al IVA incluye el 16% de  
                la compra total
                
                -------------------------------------
                TOTAL: {self.totalPrice}$
                -------------------------------------
                    ''')
        
    def showBillVIP(self):
        print(f'''
                -----------------------------------
                            FACTURA
                -----------------------------------
                Nombre: {self.ticketObject.name}
                Cedula: {self.ticketObject.dni}
                Edad: {self.ticketObject.age}
                Carrera: {self.ticketObject.validateCarRace}
                Asiento: {self.ticketObject.VIPRaceSeat}
                Ticket ID: {self.ticketObject.ticketId}
                Ticket Usado: {self.ticketObject.usedTicket}
                Descuento: {self.discount}$
                
                -----------------------------------
                SUBTOTAL: {self.subtotalPrice}$
                Impuesto por IVA: {self.vatTax}$
                
                El impuesto al IVA incluye el 16% de  
                la compra total
                
                -------------------------------------
                TOTAL: {self.totalPrice}$
                -------------------------------------
                    ''')