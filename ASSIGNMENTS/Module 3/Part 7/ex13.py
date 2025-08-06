class parent:
    def info(self):
        self.name=input("enter your name :")
        self.surname=input("enter your surname:")
        


class child(parent):

    def display(self):
        print(f"Full Name: {self.name} {self.surname}")
        

    
c=child()
c.info()
c.display()