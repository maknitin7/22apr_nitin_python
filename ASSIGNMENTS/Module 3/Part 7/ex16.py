
class Employee:
    def show_details(self):
        print("I am an employee of the company.")

class Manager(Employee):
    def show_role(self):
        print("Iam a manager. I manage the team and projects.")

class Developer(Employee):
    def show_role(self):
        print(" I am a Developer. I write and maintain code.")

class Intern(Employee):
    def show_role(self):
        print("I am a Intern.I assist in small tasks and learn from seniors.")

m = Manager()
d = Developer()
i = Intern()

m.show_details()
m.show_role()

d.show_details()
d.show_role()

i.show_details()
i.show_role()
