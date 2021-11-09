class QuizBrain:

    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def still_has_question(self):

        return self.question_number < len(self.question_list)

    def next_question(self):

        while self.still_has_question():
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            q_answer = input(f"Q {self.question_number  }. {current_question.text} (True/False): ")
            if q_answer == current_question.answer.lower():
               print("Correct answer")
               self.score += 1

            else:
               print(f"You got it wrong")
            print(f"The correct Answer is {current_question.answer}")
            print(f"Score : {self.score} / {self.question_number}")
            print("\n")





