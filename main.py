from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# print(data)
# print(data["response_code"])
# print(data["results"])
# print(data["results"][0])
# print(data["results"][0]["question"])
# print(data["results"][0]["correct_answer"])

# quiz_dict = {"response_code": data["response_code"]},
# {"results" : data["results"]},
# {"category" : data["results"][0]},
# {"question" :  data["results"][0]["question"]},
# {"correct_answer" : data["results"][0]["correct_answer"]}, 


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
