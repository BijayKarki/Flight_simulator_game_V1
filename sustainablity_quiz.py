from time import sleep

quiz_adedeji = {
    'author': "Adedeji",
    'title': "Planting trees",
    'questions': [
        {
            'question': "Solve for x in 3 * x + 5 = 11",
            'correct_answer': "2"
        },
        {
            'question': "Solve for y in 20/y = 5",
            'correct_answer': "4"
        },
        {
            'question': "Solve for x in 9 x 9 = x",
            'correct_answer': "81"
        },
        {
            'question': "Solve for y in 21/3 = y",
            'correct_answer': "7"
        },
        {
            'question': "Solve, 2 + (9/3) + (12 x 5)",
            'correct_answer': "65"
        }

    ],
    'description': "These are mathematical questions. Please solve them and provide the correct answers.",
}
##################################################################################################################

quiz_mehdi = {
    'author': "Mehdi",
    'title': "Reduce, Reuse & Recycle",
    'questions': [
        {
            'question': "Reducing, Reusing and Recycling, make the earth cleaner.",
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
    'description': "These are true or false questions. Input 't' or 'f' as an answer (upper or lower case).",
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
    'description': "These are multiple choice questions. Input 'a', 'b' or 'c' as an answer (upper or lower case).",
}
##################################################################################################################

quiz_wallace = {
    'author': "Wallace",
    'title': "Sorting waste",
    'questions': [
        {
            'question': "Which of these wastes has higher impact on the nature?   a) Organic      b) Hazardous        c) Kitchen water",
            'correct_answer': "B"
        },
        {
            'question': "Which of this is not a bio waste?       a)food      b)plastic      c)wood",
            'correct_answer': "B"
        },
        {
            'question': "Sorting organic waste from other waste types saves the environment? a) Not sure b) No c) Yes",
            'correct_answer': "C"
        },
        {
            'question': "The hardest waste to sort or recycle is?  a)Electronics   b)plastic bottle    c)glass",
            'correct_answer': "A"
        },
        {
            'question': "Which of this is a type of hazardous waste?   a)glass     b)batteries     c)plastic",
            'correct_answer': "B"
        }

    ],
    'description': "These are multiple choice questions. Input 'a', 'b' or 'c' as an answer (upper or lower case).",
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

quizes = [quiz_adedeji, quiz_mehdi, quiz_bijay, quiz_wallace, quiz_zaheen]


def selectQuiz():
    quiz_length = len(quizes)
    sleep(1.0)
    print("===========================================================")
    print(f"There are {quiz_length} different categories of the quiz: ")
    print("===========================================================")
    for idx, quiz in enumerate(quizes):
        sleep(1.0)
        print(f"    {idx + 1}. {quiz['title']}")

    print()
    max_attempt = 5  # Player is allowed max 5 times to give invalid input before the game ends!
    for attempt_no in range(0, max_attempt):
        sleep(2.0)
        user_selected_quiz = input("Please select one of the options (1-5) to start the quiz : ")

        if user_selected_quiz.isdigit() and int(user_selected_quiz) in range(1, quiz_length + 1):
            return quizes[int(user_selected_quiz) - 1]
        else:
            print("❗Invalid Input❗")
            print(f" You have {max_attempt - (attempt_no + 1)} more attempts to give a valid input!")
            print()
            continue

    return None


test_score = 250
acutal_score = test_score * 10


def playQuiz():
    quiz = selectQuiz()
    if quiz == None:
        print("Invalid inputs given for the maximum allowed attempts!")
        return None
    print()
    print("================================================================================================")
    print(f'Hello, you have selected the option "{quiz["title"]}". Thank you for your interest!')
    print("================================================================================================")
    print("There are 5 questions in total, for each right answer you will be rewarded 250 points.")
    print()
    print(quiz['description'])

    print()

    user_score = 0
    selected_quiz_questions = quiz['questions']
    for idx, question in enumerate(selected_quiz_questions):

        print(f"Question {idx + 1}. {question['question']}")
        answer = input("Your answer: ").upper()
        if question['correct_answer'] == answer:
            print("✅ Correct answer! ")
            user_score += acutal_score
        else:
            print(f"❌ Wrong answer! The correct answer is '{question['correct_answer']}'.")

        print()
    return user_score

# For future !!
# quizes = [quiz_adedeji, quiz_mehdi, quiz_bijay, quiz_wallace, quiz_zaheen] #for randomizing the quiz
# If we want to randomize the quiz later in the future
# import random
# random_index = random.randint(0, len(quizes) - 1)
# randomized_quiz = quizes[random_index]
# quiz(randomized_quiz)
