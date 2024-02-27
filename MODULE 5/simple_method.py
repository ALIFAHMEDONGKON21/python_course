def call():
    print("calling some one ")
    return 'call done'


class phone:
    price=10000
    brand='sumsung'
    color='red'
    feature=['camera','speaker', 'hammer']
    
    def call(self):
        print("nobody not call me")
        
    def send_sms(self,phone,sms):
        taxt=f'Sending to sms {phone} to massage {sms} '
        return taxt

my_phone=phone()
print(my_phone.feature)
my_phone.call()

result=my_phone.send_sms(122222,'alif how are you')
print(result)