class Father:
    def skills(self):
        print("Father: Knows carpentry.")

class Mother:
    def skills(self):
        print("Mother: Knows cooking.")

class Child(Father, Mother):
    def skills(self):
        print("Child: Inherits skills from both parents.")
        Father.skills(self)  
        Mother.skills(self)

c = Child()
c.skills()
