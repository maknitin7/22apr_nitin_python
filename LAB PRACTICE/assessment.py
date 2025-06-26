questions = {}
print("Welcome to TOPS QUIZ GAMING CHALLENGE")

print(" Select your role:, press 1 for Quiz master and press 2 for Quiz cracker: ")
role= int(input("Select your role: "))
if role==1:
    print("         Welcome Master          \n Shake your brain and Add some challenging questions..")
    print("---------- MENU---------- \n Press 1 for add questions. \n Press 2 for view questions. \n Press 3 for delete questions. \n Press 4 for exit.")
    while True:
        choice= int(input("Enter your choice: "))
        if choice==1:
            print("Add your question here: ")
            question= input("Enter your question: ")
            option1= input("Enter option 1: ")
            option2= input("Enter option 2: ")
            option3= input("Enter option 3: ")
            answer= input("Enter the correct answer: ")
            questions[question] = {
                'options': [option1, option2, option3],
                'answer': answer
            }
        elif choice==2:

        elif choice==3:
            print("Delete your question here: ")
            question_to_delete = input("Enter the question you want to delete: ")
            if question_to_delete in questions:
                del questions[question_to_delete]
                print("Question deleted successfully.")
            else:
                print("Question not found.")

            

