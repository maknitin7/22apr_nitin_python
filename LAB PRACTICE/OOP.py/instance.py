# we can only access values using instance but cant change it durinng runtime
class instance:
    id=101
    name="Nitin"

    def stid(self):

        print(f"Student ID: {self.id} \nStudent Name: {self.name}")
#calling via object
im=instance()
im.stid()
im.id=102
im.name="pratik"
im.stid()

#calling via instance
instance().stid()
instance().id=102
instance().name="Pratik"
instance().stid()

"""class studinfo:
    stid=101
    stnm="Sanket"

    def getdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)"""

#Calling via Object
"""st=studinfo()
st.getdata()
st.stid=102
st.stnm="Ashok"
st.getdata()"""



"""studinfo().getdata()
studinfo().stid=102
studinfo().stnm="Hitesh"
studinfo().getdata()"""