class Quizbrain():
    def __init__(self, ques_list):
        self.question_num = 0
        self.question_list = ques_list
        self.score = 0

    def still_has_question(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        current_ques = self.question_list[self.question_num]
        self.question_num += 1
        play_answer =  input(f"Q{self.question_num}: {current_ques.text} (True/False): ")
        self.check_answer(play_answer, current_ques.answer)

    def check_answer(self, play_answer, correct_answer):
        if play_answer.lower() == correct_answer.lower():
            print("You right !!!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your score is {self.score}/{self.question_num} \n")






