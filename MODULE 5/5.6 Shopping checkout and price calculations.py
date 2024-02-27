class shoping:
    def __init__(self,name) -> None:
        self.name=name
        self.cart=[]
    
    def add_to_cart(self,item,price,quntity):
        product = {'item': item, 'price': price, 'quntity':quntity}
        self.cart.append(product)
    
    def checkout(self,amount):
        total=0
        for item in self.cart:
            total +=item['price']*item['quntity']
        print("You buy this product ,need this amount",total)
        if amount>total:
            extra=amount-total
            print('you pay extra  take it',extra)
            
        elif amount<total:
            need_extra=total-amount
            print('you pay only ',amount, "Need extra amount",need_extra)
    def remove(self,remove_iltem):
        
        for item in self.cart:
            this_item_remove=self.cart.pop(remove_iltem)
        
                
            
            
shahab=shoping('shahab khan')
shahab.add_to_cart('alu',25,5)
shahab.add_to_cart('lal',30,5)
shahab.add_to_cart('oil',2,140)
shahab.add_to_cart('rice',5,56)

print(shahab.cart)

print(',..........................................,')



shahab.checkout(100)

print("........................................")
shahab.remove(4)

print(shahab.cart)