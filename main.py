# class quiz:
#   def__init__(option,desc,question,answer):
#   self.option = option
#   self.desc = desc
#    self.question = question
#   self.answer = answer

quiz_bijay = {
    'author': "Bijay",
    'title': "Saving water",
    'questions': [
        {
            'question': "What is the average daily water requirement for a human body?   a) 0.5L,    b) 3L,      c) 100 L",
            'correct_answer': "B"
        },
        {
            'question': "What is the water percentage of adult human body?   a) 10%      b) 99%      c) 60%",
            'correct_answer': "C"
        },
        {
            'question': "How much of Earth's surface is covered by water?    a) 10%      b) 71%      c) 60%",
            'correct_answer': "B"
        },
        {
            'question': "How many days can human survive without water?      a) 1 day   b) 2 days    c) 3 days",
            'correct_answer': "C"
        },
        {
            'question': "What is the molecular formula of water?     a) H2O       b) N2O       c) CO2",
            'correct_answer': "A"
        }

    ],
    'description': "These are multiple choice questions. Please provide alphabet 'a', 'b' or 'c' as an answer.",
}
user_score = 0
selected_quiz_questions = quiz_bijay['questions']

print(selected_quiz_questions)
for idx, question in enumerate(selected_quiz_questions):
    print(idx, question)
    # print(f"Question {idx + 1}. {question['question']}")
    # answer = input("Your answer: ").upper()
    # if (question['correct_answer']) == answer:
    # user_score += 250

    # print(user_score)
