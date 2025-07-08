import pandas as pd
import datetime
#qa= pd.read_csv("general_knowledge_qna.csv")

questions = {}

def quiz_master():

    while True:

        print("                 Welcome Master          \n Shake your brain and Add some challenging questions... \n")
        print("---------- MENU---------- \n Press 1 for add questions. \n Press 2 for view questions. \n Press 3 for delete questions. \n Press 4 for exit.")
    
        choice= int(input("Enter your choice: "))
        if choice==1:
                try:
                    print("Add your question here: ")
                    qid= input("Enter question ID: ")
                    if qid in questions:
                        print(" Qustion ID already Exists.!")
                        continue
                    question= input("Enter your question: ")
                    option1= input("Option 1: ")
                    option2= input("Option 2: ")
                    option3= input("Option 3: ")
                    answer= input("Enter the correct answer: (1-4) ")
                    if answer not in ['1', '2', '3', '4']:
                        print("Choice must be in 1 to 4!")
                        continue
                    questions[qid] = {
                        "question": question,
                        "options": [option1, option2, option3],
                        "answer": answer}
                except Exception as e:
                     print(" Error: ", e)
                print("Question added successfully.")
                import json
                with open("question_bank", "a") as qb:
                    qb.write(json.dumps({question: questions[qid]}) + "\n")
                    
                
        elif choice==2:
                print("\n View your questions here: ")
                print("-------------------------------------------------") 
                qustion_bank=open("question_bank","r") 
                print(qustion_bank.readline())
                

        elif choice==3:

                print("Delete your question here: ")
                question_to_delete = input("Enter the question ID you want to delete: ")
                if question_to_delete in questions:
                    confirm=input(" Do u really want to delete this question? (Y|N)")
                    if confirm=="Y":
                        del questions[question_to_delete]
                        print("Question deleted successfully.")
        
                else:
                    print("Question not found. Enter Proper ID !!")

                    
        elif choice==4:
                print(" 'Going Back To Main Menu' ")
                break
        
def quiz_cracker():
    print("Empty.")
                

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