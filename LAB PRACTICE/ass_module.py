def add():
        
    if choice==1:
            print("Add your question here: ")
            question= input("Enter your question: ")
            option1= input("Enter option 1: ")
            option2= input("Enter option 2: ")
            option3= input("Enter option 3: ")
            answer= input("Enter the correct answer: ")
            questions[question] = {
                'options': [option1, option2, option3],
                'answer': answer}
def view():
    if choice==2:
        print("View your questions here: ")
        for question, details in questions.items():
            print(f"Question: {question}")
            print("Options:")
            for i, option in enumerate(details['options'], start=1):
                print(f"{i}. {option}")
            print(f"Answer: {details['answer']}\n") 