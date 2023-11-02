import random

# Define quiz questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "correct_answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "correct_answer": "B"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A) Elephant", "B) Giraffe", "C) Blue Whale", "D) Lion"],
        "correct_answer": "C"
    }
]

# Function to present a quiz question
def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    user_answer = input("Your answer (A/B/C/D): ").upper()
    if user_answer == question_data["correct_answer"]:
        print("Correct!\n")
        return 1
    else:
        print(f"Incorrect. The correct answer is {question_data['correct_answer']}.\n")
        return 0

# Function to calculate the final score
def calculate_score(score):
    return f"Your score: {score}/{len(quiz_data)}"

# Function to play the quiz game
def play_quiz():
    score = 0
    random.shuffle(quiz_data)
    
    for question in quiz_data:
        score += ask_question(question)
    
    print(calculate_score(score))
    
# Main game loop
while True:
    print("Welcome to the Quiz Game!")
    print("Rules: Answer the following multiple-choice questions.")
    
    play_quiz()
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thank you for playing!")
        break
