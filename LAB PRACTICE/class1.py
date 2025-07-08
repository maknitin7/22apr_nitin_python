"""class student:
    stid=77
    stname="Nitin"

    def getdata(self):
        print("This is just an example of class and object!")

    def getsum(self, a, b):
            print("Sum is: ", a + b)

st=student()

print("Student ID: ", st.stid)
print("Student Name: ", st.stname)
st.getdata()
st.getsum(10, 20)"""

class student:
    stid=int(input("Enter your ID: "))
    stname=input("Enter your name: ")

    def getdata(self):
        print(f"Student ID:{self.stid} \nStudent name: {self.stname}")
        #print("Student Name: ", self.stname)

st=student()

st.getdata()
