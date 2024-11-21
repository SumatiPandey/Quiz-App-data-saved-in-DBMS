import sqlite3


DB_FILE = "quiz_app.db"


def initialize_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL,
            correct_option INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def add_sample_data():
    sample_data = [
        ("What is the capital of France?", "Paris", "Berlin", "Rome", "Madrid", 1),
        ("What is 2 + 2?", "3", "4", "5", "6", 2),
        ("Which programming language is this?", "Java", "C++", "Python", "Ruby", 3)
    ]

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    
    cursor.executemany('''
        INSERT INTO questions (question, option1, option2, option3, option4, correct_option)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', sample_data)

    conn.commit()
    conn.close()
    print("Sample data added to the database.")


def fetch_quiz_data():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    
    cursor.execute('SELECT * FROM questions')
    rows = cursor.fetchall()

    conn.close()

    return rows


def display_question(question_data, question_number):
    print(f"\nQuestion {question_number}: {question_data[1]}")
    print(f"  1. {question_data[2]}")
    print(f"  2. {question_data[3]}")
    print(f"  3. {question_data[4]}")
    print(f"  4. {question_data[5]}")
    return question_data[6] - 1  


def get_user_answer():
    while True:
        try:
            user_input = int(input("Your answer (1-4): ")) - 1
            if 0 <= user_input <= 3:
                return user_input
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def run_quiz():
    print("Welcome to the Quiz App!\n")
    quiz_data = fetch_quiz_data()
    score = 0

    for i, question_data in enumerate(quiz_data, start=1):
        correct_answer = display_question(question_data, i)
        user_answer = get_user_answer()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question_data[correct_answer + 2]}\n")

    print(f"Quiz Over! Your score: {score}/{len(quiz_data)}")
    if score == len(quiz_data):
        print("Congratulations! You got all answers correct!")
    elif score > len(quiz_data) // 2:
        print("Great job! Keep practicing to get a perfect score!")
    else:
        print("Better luck next time!")


if __name__ == "__main__":
    
    initialize_database()
    
    
    
    run_quiz()
