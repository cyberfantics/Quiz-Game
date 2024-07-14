import os
from QuizBrain import QuizBrain
from QuizModel import Question
from Data import question_data
question_bank = []

os.system('cls')

for question_stru in question_data:
    question_text = question_stru["text"]
    answer_text = question_stru["answer"]
    new_question = Question(question_text , answer_text)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_question():
    quiz.next_question()

os.system("cls")    
print(f"\n\n\n\nYou've completed the quiz.\nYour final score was {quiz.score}/{quiz.question_number}")

input()