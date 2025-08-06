from module_code import *

def main_code():
    while True:
        print("Welcome to TOPS QUIZ GAMING CHALLENGE \n")

        print(" Select your role: \n1. Quiz Master \n2. Quiz Cracker: \n3. Exit \n")
        role= int(input("Select your role: "))
        if role==1:
            quiz_master()
        elif role==2:
            quiz_cracker()
        elif role==3:
            print("Exiting the program. Thanks For using Us. Visit again ! ")
            break
        else:
            print("Invalid input selected. Please Enter between (1 , 2, 3)")
main_code()
