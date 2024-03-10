def doble_decker():
    print('doble deacker bus')
    def inner_fun():
        print('inside the inner')
        return 3000
    return inner_fun

def do_any(work):
    print('work stsrted ')
    print(work)
    print('work ended')
    
    
def sleeping():
    print('sleping and draming in python' )
    
# print(doble_decker)

print(doble_decker()())

do_any('1')

do_any(sleeping())
