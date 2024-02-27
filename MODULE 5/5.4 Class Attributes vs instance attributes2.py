class shoping_mol:
    def __init__(self,parson_name) -> None:
        self.parson_name=parson_name
        self.cart=[]
    def add_to_cart(self, item):
        self.cart.append(item) #instance attributes
alif=shoping_mol('alif')
alif.add_to_cart('phone')
alif.add_to_cart('some food')
alif.add_to_cart('some book')
alif.add_to_cart('drinks')

print(alif.cart)

chacha_shabab=shoping_mol('shabab')
chacha_shabab.add_to_cart('take some food')
chacha_shabab.add_to_cart('take some shoping bag')
chacha_shabab.add_to_cart('take english book')
chacha_shabab.add_to_cart('take some somke')

print(chacha_shabab.cart)