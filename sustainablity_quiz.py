quiz_adedeji = {
    'author': "Adedeji",
    'title': "Planting trees",
    'questions': [
        {
            'question': "x in 3 * x + 5 = 11",
            'correct_answer': "2"
        },
        {
            'question': "y in 20/y = 5",
            'correct_answer': "4"
        },
        {
            'question': "x in 9 x 9 = x",
            'correct_answer': "81"
        },
        {
            'question': "y in 21/3= y",
            'correct_answer': "7"
        },
        {
            'question': "2 + (9/3) + (12 x 5)",
            'correct_answer': "65"
        }

    ],
    'description': "These are mathematical questions. Please solve them and provide the correct answers.",
}
##################################################################################################################

quiz_mehedi = {
    'author': "Mehedi",
    'title': "Reduce, Reuse & Recycle",
    'questions': [
        {
            'question': "Reducing,Reusing and Recycling, make the earth cleaner.",
            'correct_answer': "T"
        },
        {
            'question': "Recycling is something only adults can do.",
            'correct_answer': "F"
        },
        {
            'question': "Plastic bags are better for the environment.",
            'correct_answer': "F"
        },
        {
            'question': "Taking shorter shower and turning off the faucet while brushing is a smart move.",
            'correct_answer': "T"
        },
        {
            'question': "Reuse means: use something over and over.",
            'correct_answer': "T"
        }

    ],
    'description': "These are true or false questions. Please provide 't' or 'f' as an answer.",
}
##################################################################################################################

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
##################################################################################################################

quiz_wallace = {
    'author': "Wallace",
    'title': "Sorting waste",
    'questions': [
        {
            'question': "Which of this is not type of waste?   a) Organic      b) Hazardous        c) Kitchen water.",
            'correct_answer': "C"
        },
        {
            'question': "Which of this is not type of organic waste?       a)food      b)meat      b)wood",
            'correct_answer': "A"
        },
        {
            'question': "Should you clean non-organic from your organic waste to save the environment? a) Not sure b) No c) Yes",
            'correct_answer': "C"
        },
        {
            'question': "The hardest waste to sort or recycle is?  a)Milk carton   b)plastic bottle    c)glass",
            'correct_answer': "A"
        },
        {
            'question': "Which of this is a type of hazardous waste?   a)glass     b)batteries     c)plastic",
            'correct_answer': "B"
        }

    ],
    'description': "These are multiple choice questions. Please provide alphabet 'a', 'b' or 'c' as an answer.",
}

##################################################################################################################

quiz_zaheen = {
    'author': "Zaheen",
    'title': "Saving energy",
    'questions': [
        {
            'question': "",
            'correct_answer': ""
        },
        {
            'question': "",
            'correct_answer': ""
        },
        {
            'question': "",
            'correct_answer': ""
        },
        {
            'question': "",
            'correct_answer': ""
        },
        {
            'question': "",
            'correct_answer': ""
        }

    ],
    'description': "",
}

quizes = [quiz_adedeji, quiz_mehedi, quiz_bijay, quiz_wallace, quiz_zaheen]


def selectQuiz():
    quiz_length = len(quizes)
    print("===========================================================")
    print(f"There are {quiz_length} different categories of the quiz: ")
    print("===========================================================")
    for idx, quiz in enumerate(quizes):
        print(f"    {idx + 1}. {quiz['title']}")

    print()
    user_selected_quiz = int(input("Please select one of the options (1-5) to start the quiz : "))

    return quizes[user_selected_quiz - 1]


def playQuiz():
    quiz = selectQuiz()
    print()
    print(f'Hello, you have selected the option "{quiz["title"]}". Thank you for your interest!')
    print("================================================================================================")
    print("There are 5 questions in total, for each right answer you will be rewarded 250 points.")
    print(quiz['description'])
    print("================================================================================================")

    print()

    user_score = 0
    selected_quiz_questions = quiz['questions']
    for idx, question in enumerate(selected_quiz_questions):

        print(f"Question {idx + 1}. {question['question']}")
        answer = input("Your answer: ").upper()
        if (question['correct_answer']) == answer:
            user_score += 250
        print()
    return user_score

# For future !!
# quizes = [quiz_adedeji, quiz_mehedi, quiz_bijay, quiz_wallace, quiz_zaheen] #for randomizing the quiz
# If we want to randomize the quiz later in the future
# import random
# random_index = random.randint(0, len(quizes) - 1)
# randomized_quiz = quizes[random_index]
# quiz(randomized_quiz)
