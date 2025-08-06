class info:

    def data(self):
        self.name=input("enter your name:")
        self.age=int(input("enter your age:"))
        self.city=input("enter your city:")

        print(f"Name:{self.name} Age:{self.age} City:{self.city}")

i=info()
i.data()
