class user1:

    def number(self):
        self.no=input("enter your number:")


class user2(user1):
    
    def gmail(self):
        self.email=input("enter your email:")
        

class user3(user2):

    def password(self):
        self.passw=input("enter your password")

class display(user3):

    def disp(self):
        self.name=input("name:")


d=display()
d.disp()
d.gmail()
d.number()
d.password()

