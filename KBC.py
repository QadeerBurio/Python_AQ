# import random
#
# # Define a class for the quiz game
# class KBCGame:
#     def __init__(self):
#         self.questions = [
#             {
#                 'question': "What is the capital of France?",
#                 'options': ['A. Berlin', 'B. Madrid', 'C. Paris', 'D. Rome'],
#                 'answer': 'C'
#             },
#             {
#                 'question': "What is 2 + 2?",
#                 'options': ['A. 3', 'B. 4', 'C. 5', 'D. 6'],
#                 'answer': 'B'
#             },
#             {
#                 'question': "Which planet is known as the Red Planet?",
#                 'options': ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Venus'],
#                 'answer': 'B'
#             },
#             {
#                 'question': "Who wrote 'To Kill a Mockingbird'?",
#                 'options': ['A. Harper Lee', 'B. J.K. Rowling', 'C. Ernest Hemingway', 'D. Mark Twain'],
#                 'answer': 'A'
#             },
#             {
#                 'question': "What is the largest ocean on Earth?",
#                 'options': ['A. Atlantic Ocean', 'B. Indian Ocean', 'C. Arctic Ocean', 'D. Pacific Ocean'],
#                 'answer': 'D'
#             }
#         ]
#         self.score = 0
#
#     def ask_question(self, question):
#         print(question['question'])
#         for option in question['options']:
#             print(option)
#         answer = input("Enter the correct option (A, B, C, D): ").strip().upper()
#         return answer == question['answer']
#
#     def play(self):
#         print("Welcome to Kaun Banega Crorepati!")
#         random.shuffle(self.questions)  # Shuffle questions to ensure random order
#         for question in self.questions:
#             if self.ask_question(question):
#                 print("Correct!\n")
#                 self.score += 1
#             else:
#                 print("Wrong answer!\n")
#         print(f"Game over! Your final score is: {self.score}/{len(self.questions)}")
#
# # Run the game
# if __name__ == "__main__":
#     game = KBCGame()
#     game.play()
#
# import random
#
#
# class KBCGame:
#     def __init__(self):
#         self.questions = [
#             {
#                 'question': "What is the capital of France?",
#                 'options': ['A. Berlin', 'B. Madrid', 'C. Paris', 'D. Rome'],
#                 'answer': 'C'
#             },
#             {
#                 'question': "What is 2 + 2?",
#                 'options': ['A. 3', 'B. 4', 'C. 5', 'D. 6'],
#                 'answer': 'B'
#             },
#             {
#                 'question': "Which planet is known as the Red Planet?",
#                 'options': ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Venus'],
#                 'answer': 'B'
#             },
#             {
#                 'question': "Who wrote 'To Kill a Mockingbird'?",
#                 'options': ['A. Harper Lee', 'B. J.K. Rowling', 'C. Ernest Hemingway', 'D. Mark Twain'],
#                 'answer': 'A'
#             },
#             {
#                 'question': "What is the largest ocean on Earth?",
#                 'options': ['A. Atlantic Ocean', 'B. Indian Ocean', 'C. Arctic Ocean', 'D. Pacific Ocean'],
#                 'answer': 'D'
#             }
#         ]
#         self.levels = [
#             {'level': 1, 'prize': 1000},
#             {'level': 2, 'prize': 2000},
#             {'level': 3, 'prize': 3000},
#             {'level': 4, 'prize': 4000},
#             {'level': 5, 'prize': 5000}
#         ]
#         self.current_level = 0
#         self.score = 0
#
#     def ask_question(self, question):
#         print(question['question'])
#         for option in question['options']:
#             print(option)
#         answer = input("Enter the correct option (A, B, C, D): ").strip().upper()
#         return answer == question['answer']
#
#     def play(self):
#         print("Welcome to Kaun Banega Crorepati!")
#         print("Answer the questions to win money. Let's get started!\n")
#
#         random.shuffle(self.questions)  # Shuffle questions to ensure random order
#
#         for i, question in enumerate(self.questions):
#             if self.current_level >= len(self.levels):
#                 print("Congratulations! You've completed all levels!")
#                 break
#
#             print(f"Level {self.current_level + 1}: Prize money is {self.levels[self.current_level]['prize']}")
#
#             if self.ask_question(question):
#                 print("Correct!\n")
#                 self.score += 1
#                 print(f"You have won {self.levels[self.current_level]['prize']}")
#                 self.current_level += 1
#             else:
#                 print("Wrong answer! Game over.\n")
#                 print(f"You won {self.levels[self.current_level]['prize']}")
#                 break
#
#         if self.current_level == len(self.levels):
#             print(f"Game over! You have completed all levels. Your final prize is {self.levels[-1]['prize']}")
#
#
# # Run the game
# if __name__ == "__main__":
#     game = KBCGame()
#     game.play()


questions = [
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):

    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"a. {question[1]}          b. {question[2]} ")
    print(f"c. {question[3]}          d. {question[4]} ")
    reply = int(input("Enter your answer (1-4) or  0 to quit:\n"))
    if (reply == 0):
        money = levels[i - 1]
        break
    if (reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
        elif (i == 14):
            money = 10000000
    else:
        print("Wrong answer!")
        break

print(f"Your take home money is {money}")

