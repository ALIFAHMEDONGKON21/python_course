class parson:
    cart=[]
    def __init__(self,his_name) -> None:
        self.his_name=his_name
    
    def add_to_cart(self,item):
        self.cart.append(item)


alif=parson('alif')
alif.add_to_cart('phone')
alif.add_to_cart('some food')
alif.add_to_cart('some book')
alif.add_to_cart('drinks')

print(alif.cart)

chacha_shabab=parson('shabab')
chacha_shabab.add_to_cart('take some food')
chacha_shabab.add_to_cart('take some shoping bag')
chacha_shabab.add_to_cart('take english book')
chacha_shabab.add_to_cart('take some somke')

print(chacha_shabab.cart)