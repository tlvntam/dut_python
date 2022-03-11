from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for question in question_data:
    ques_text = question["text"]
    ques_answer = question["answer"]
    new_ques = Question(ques_text, ques_answer)
    question_bank.append(new_ques)

new_quiz = Quizbrain(question_bank)

while new_quiz.still_has_question():
    new_quiz.next_question()

print("You've completed the quiz")
print(f"Ur final score was: {new_quiz.score}/{new_quiz.question_num} ")
