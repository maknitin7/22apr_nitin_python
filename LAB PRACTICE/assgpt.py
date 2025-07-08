# quiz_game_file_based.py

import json
import os

# --------------------------------------
# 📁 File Storage
# --------------------------------------
QUESTION_FILE = "questions.json"

def load_questions():
    if os.path.exists(QUESTION_FILE):
        with open(QUESTION_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_questions(questions):
    with open(QUESTION_FILE, 'w') as f:
        json.dump(questions, f, indent=4)

# Load on program start
questions = load_questions()

# --------------------------------------
# 🎓 Quiz Master Functions
# --------------------------------------
def quiz_master_menu():
    global questions
    while True:
        print("\n📘 Quiz Master Menu:")
        print("1. Add Question\n2. View Questions\n3. Delete Question\n4. Exit to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            try:
                qid = input("Enter Question ID: ").strip()
                if qid in questions:
                    print("❌ Question ID already exists!")
                    continue
                question = input("Enter Question: ").strip()
                options = [input(f"Option {i+1}: ").strip() for i in range(4)]
                answer = input("Enter Correct Option (1-4): ").strip()
                if answer not in ['1', '2', '3', '4']:
                    print("❌ Invalid answer input. Must be 1-4.")
                    continue
                questions[qid] = {
                    'question': question,
                    'options': options,
                    'answer': answer
                }
                save_questions(questions)
                print("✅ Question added successfully.")
            except Exception as e:
                print("❌ Error adding question:", e)

        elif choice == '2':
            if not questions:
                print("⚠️ No questions available.")
                continue
            for qid, q in questions.items():
                print(f"\n🔹 ID: {qid}")
                print(f"Q: {q['question']}")
                for idx, opt in enumerate(q['options'], start=1):
                    print(f"   {idx}. {opt}")
                print(f"Answer: {q['answer']}")

        elif choice == '3':
            qid = input("Enter Question ID to delete: ").strip()
            if qid not in questions:
                print("❌ Question not found.")
                continue
            confirm = input("Are you sure you want to delete this question? (Y/N): ").strip().upper()
            if confirm == 'Y':
                del questions[qid]
                save_questions(questions)
                print("✅ Question deleted.")
            else:
                print("❌ Deletion cancelled.")

        elif choice == '4':
            break
        else:
            print("❌ Invalid input. Please try again.")

# --------------------------------------
# 🎮 Quiz Cracker (Play the Game)
# --------------------------------------
def quiz_cracker_menu():
    questions = load_questions()
    score = 0
    total = len(questions)
    if total == 0:
        print("⚠️ No questions available to play.")
        return

    for qid, q in questions.items():
        print(f"\n🧠 {q['question']}")
        for idx, opt in enumerate(q['options'], start=1):
            print(f"   {idx}. {opt}")
        try:
            user_ans = input("Your answer (1-4): ").strip()
            if user_ans == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer was option {q['answer']}")
        except Exception as e:
            print("❌ Error occurred during answer:", e)

    print(f"\n🎯 You scored {score} out of {total}.")

# --------------------------------------
# 🏁 Main Menu
# --------------------------------------
def main_menu():
    while True:
        print("\n🧩 Welcome to Quiz Game")
        print("1. Quiz Master (Manage Questions)")
        print("2. Quiz Cracker (Play Quiz)")
        print("3. Exit")

        choice = input("Choose an option: ").strip()
        if choice == '1':
            quiz_master_menu()
        elif choice == '2':
            quiz_cracker_menu()
        elif choice == '3':
            print("👋 Exiting the Quiz Game. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# --------------------------------------
# 🚀 Run Program
# --------------------------------------
if __name__ == "__main__":
    main_menu()
