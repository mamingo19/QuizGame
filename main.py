from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_store = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_store.append(new_question)

quiz = QuizBrain(question_store)
quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()

if quiz.score >= 10:
    print("GIGATY! You are doing really good")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}")
elif quiz.score < 10 and quiz.score > 5:
    print("Doing not so good bruh! be better")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}")
else:
    print("LOL you are trash")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}")
