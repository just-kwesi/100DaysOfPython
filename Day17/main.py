from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for ele in question_data:
    text = ele['text']
    answer = ele['answer']
    question = Question(text,answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}.")