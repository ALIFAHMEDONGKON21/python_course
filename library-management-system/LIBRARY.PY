class book:
    
    def __init__(self,id,name,quantity) -> None:
        self.id=id
        self.name=name
        self.quantity=quantity

class user:
    def __init__(self,id,name,password) -> None:
        self.id=id
        self.name=name
        self.password=password
        self.borrowedbooks=[]
        self.returnedbook=[]
        

class Library:
    def __init__(self,name) :
        self.name=name
        self.users=[]
        self.books=[]
    
    def addbook(self,id,name,quantity):
        
        for book in self.books:
            if book.id==id:
               print(f"\n\t---> !! Book Id {book.id} already exists")
            return  
        
        book=book(id,name,quantity)
        self.books.append(book)
        print(f"\n\t---> {book.name} X {quantity} added succesfully !")
    
    
    def adduser(self,id,name,password):
        
        for user in self.users:
            if self.id==id:
                print(f"\n\t---> !! Book Id {book.id} already exists")
            return
        
        user=user(id,name,password)
        self.users.append(user)
        return user


bsk=Library("Bishwa Shahitja Kendro")
admin=bsk.addUser(1000,"admin","admin")
ratin=bsk.addUser(17,"ratin","123")
cpBook=bsk.addBook(11,"CP book",5)

currentUser=admin

