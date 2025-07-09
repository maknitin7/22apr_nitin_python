
import datetime

questions = {}

def quiz_master():
    while True:
        print("                 Welcome Master          \n Shake your brain and Add some challenging questions... \n")
        print("---------- MENU---------- \n Press 1 for add questions. \n Press 2 for view questions. \n Press 3 for delete questions. \n Press 4 for exit.")
        choice = int(input("Which operation you want to perform?: "))
        if choice == 1:
            try:
                print("Add your question here: ")
                qid = input("Enter question ID: ")
                if qid in questions:
                    print(" Qustion ID already Exists.!")
                    continue
                question = input("Enter your question: ")
                option1 = input("Option 1: ")
                option2 = input("Option 2: ")
                option3 = input("Option 3: ")
                answer = input("Enter the correct answer: (1-3) ")
                if answer not in ['1', '2', '3']:
                    print("Choice must be in 1 to 3!")
                    continue
                questions[qid] = {
                    "question": question,
                    "options": [option1, option2, option3],
                    "answer": answer
                }
            except Exception as e:
                print(" Error: ", e)
            print("Question added successfully.")

            with open("question_bank", "a") as qb:
                qb.write(f"\nQuestion added at {datetime.datetime.now()} \nQuestion ID:{qid} \nQuestion: {question} \nOption 1: {option1} \nOption 2:{option2} \nOption 3: {option3} \nAnswer:  {answer}\n")

        elif choice == 2:
            print("\n 'Your Question Bank' ")
            print("-------------------------------------------------")
            with open("question_bank", "r") as qustion_bank:
                print(qustion_bank.read())

        elif choice == 3:
            print("Delete your question here: ")
            q2d = input("Enter the question ID you want to delete: ")
            if q2d in questions:
                confirm = input(" Do u really want to delete this question? (y|n)")
                if confirm == "y":
                    del questions[q2d]
            else:
                print("Question not found. Enter Proper ID !!")

            with open("question_bank", "a") as qb:
                qb.write(f"Question deleted at {datetime.datetime.now()} \nQuestion ID:{q2d} \n")
            print("Question deleted successfully.")
            
        elif choice == 4:
            print(" 'Going Back To Main Menu' ")
            break

def quiz_cracker():
    print("Empty.")