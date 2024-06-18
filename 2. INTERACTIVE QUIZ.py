
# ICT 09 – Programming 1

# FINAL PROJECT

# 2. Interactive quiz:
# - Create and interactive quiz in python. The quiz program should have at least 100 questions
# with answers. There should be a prompt that shows the problem statement and a way for
# the user to input his/her answer. In addition, the application keeps track of the user’s
# progress and allows them to look at their answers at the end of the quiz. 

def interactive_quiz():
    questions = [
        {"question": "1. What shape does not have any sides and corners.?", "answer": "Circle"},
        {"question": "2. What is 2 + 2?", "answer": "4"},
        {"question": "3. What is the largest planet in our solar system?", "answer": "Jupiter"},
        {"question": "4. How many legs does a spider have?", "answer": "8"},
        {"question": "5. What galaxy do we live in?", "answer": "Milky Way"},
        {"question": "6. How many sides does a triangle have?", "answer": "3"},
        {"question": "7. Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
        {"question": "8. What is the square root of 64?", "answer": "8"},
        {"question": "9. What is the chemical symbol for gold?", "answer": "Au"},
        {"question": "10. How many lives are cats said to have?", "answer": "9"},
    ]

    score = 0

    for q in questions:
        user_answer = input(q["question"] + " Enter your answer: ")
        if user_answer.lower() == q["answer"].lower():
            score += 1

    print(f"Your score is {score} out of {len(questions)}")

if __name__ == "__main__":
    interactive_quiz()
