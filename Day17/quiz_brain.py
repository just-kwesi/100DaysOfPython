class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.questions_list = questions
        self.score = 0

    def next_question(self):
        """Returns the next question if there is more"""
        question = self.questions_list[self.question_number]
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")
        self.check_answer(user_answer, question.answer)

    def still_has_question(self):
        """Return True if there are more questions in the list"""
        currQ = self.question_number
        return currQ < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        """checks if the user inputted answer is correct"""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")
