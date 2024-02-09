class Product():
    def __init__(self, nameItem, typeItem, price):
        self.nameItem = nameItem
        self.typeItem = typeItem.split(':')
        self.price = price
        self.typeproduct = self.typeItem[0]
        self.typeproductKind = self.typeItem[1]
        
    def showProducts(self):
        print(f'''
        Nombre del producto: {self.nameItem}
        Precio Sin IVA: {self.price}$
        Tipo de producto: {self.typeproduct}
        Tipo de empaque/bebida: {self.typeproductKind}''')