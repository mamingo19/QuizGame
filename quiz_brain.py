from question_model import Question

class QuizBrain:
    def __init__(self,questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.questions_list) #this either return True or False

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer[0].lower() == correct_answer[0].lower():
            self.score += 1
            print(f"You got it right! The answer indeed is {correct_answer}")
        else:
            print(f"That is so wrong! The correct answer is: {correct_answer}")



