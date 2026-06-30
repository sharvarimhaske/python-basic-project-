def start_quiz():
    questions = [
        {
            "question": "What is the capital of India?",
            "answer": "delhi"
        },
        {
            "question": "What is 2 + 2?",
            "answer": "4"
        },
        {
            "question": "Which language is used for AI?",
            "answer": "python"
        },
        {
            "question": "What is the color of sky?",
            "answer": "blue"
        }
    ]

    score = 0

    print("\n===== QUIZ STARTED =====")

    for q in questions:
        print("\n" + q["question"])
        user_ans = input("Your Answer: ").lower()

        if user_ans == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(" Wrong!")

    total = len(questions)
    percentage = (score / total) * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 40:
        grade = "C"
    else:
        grade = "F"

    print("\n===== QUIZ RESULT =====")
    print(f"Your Score: {score}/{total}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")


while True:
    print("\n===== QUIZ SYSTEM MENU =====")
    print("1. Start Quiz")
    print("2. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        start_quiz()
    elif choice == "2":
        print("Thank you for using Quiz System!")
        break
    else:
        print("Invalid Choice!")


