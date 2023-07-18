from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
#gathers the question data from the data file and turns it into a question class and puts it into the question bank list
for i in question_data:
    question_text = i['text']
    question_answer = i['answer']
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)

#quiz will run until all questions are gone through
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is {quiz.user_score} out of {quiz.question_number}")
