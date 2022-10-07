adedeji_theme = "Planting trees"
adedeji_questions = ["x in 3 * x + 5 = 11", "y in 20/y = 5", "x in 9 x 9 = x", "y in 21/3= y", "2 + (9/3) + (12 x 5)"]
adedeji_correct_answers = ['2', '4', '81', '7', '65']
adedeji_descr = "These are mathematical questions. Please solve them and provide the correct answers."
option_1 = [adedeji_questions, adedeji_correct_answers, adedeji_descr, adedeji_theme]

#########################################################################################

mehedi_theme = "Reduce, Reuse & Recycle"
mehedi_questions = ["Reducing,Reusing and Recycling, make the earth cleaner.",
                    "Recycling is something only adults can do.",
                    "Plastic bags are better for the environment.",
                    "Taking shorter shower and turning off the faucet while brushing is a smart move.",
                    "Reuse means: use something over and over."]
mehedi_correct_answers = ['T', 'F', 'F', 'T', 'T']
mehedi_descr = "These are true or false questions. Please provide 't' or 'f' as an answer."
option_2 = [mehedi_questions, mehedi_correct_answers, mehedi_descr, mehedi_theme]
###########################################################################################

bijay_theme = "Saving water"
bijay_questions = ["What is the average daily water requirement for a human body?   a) 0.5L,    b) 3L,      c) 100 L",
                   "What is the water percentage of adult human body?   a) 10%      b) 99%      c) 60%",
                   "How much of Earth's surface is covered by water?    a) 10%      b) 71%      c) 60%",
                   "How many days can human survive without water?      a) 1 day   b) 2 days    c) 3 days",
                   "What is the molecular formula of water?     a) H2O       b) N2O       c) CO2"]
bijay_correct_answers = ['B', 'C', 'B', 'C', 'A']
bijay_descr = "These are multiple choice questions. Please provide alphabet 'a', 'b' or 'c' as an answer."
option_3 = [bijay_questions, bijay_correct_answers, bijay_descr, bijay_theme]
###########################################################################################

wallace_theme = "Sorting waste"
wallace_questions = ["Which of this is not type of waste?   a) Organic      b) Hazardous        c) Kitchen water.",
                     "Which of this is not type of organic waste?       a)food      b)meat      b)wood",
                     "Should you clean non-organic from your organic waste to save the environment? a) Not sure b) No c) Yes",
                     "The hardest waste to sort or recycle is?  a)Milk carton   b)plastic bottle    c)glass",
                     "Which of this is a type of hazardous waste?   a)glass     b)batteries     c)plastic"]
wallace_correct_answers = ['C', 'A', 'C', 'A', 'B']
wallace_descr = "These are multiple choice questions. Please provide alphabet 'a', 'b' or 'c' as an answer."
option_4 = [wallace_questions, wallace_correct_answers, wallace_descr, wallace_theme]
###########################################################################################

zaheen_theme = "Saving Energy"
zaheen_questions = []
zaheen_correct_answers = []
zaheen_descr = ""
option_5 = [zaheen_questions, zaheen_correct_answers, zaheen_descr, zaheen_theme]


###########################################################################################

def quiz(option):
    print()
    print(f'Hello, you have selected the option "{option[-1]}". Thank you for your interest!')
    print("================================================================================================")

    print("There are 5 questions in total, for each right answer you will be rewarded 250 points.")
    print("Please answer the following questions.")
    print("================================================================================================")
    print(option[2])
    print()
    user_answers = []
    for i in range(0, 5):
        print()
        print(f"Question {i + 1}. {option[0][i]}")
        a = input("Your answer: ").upper()
        user_answers.append(a)
    # print(user_answers)
    result = 0
    for i in range(0, 5):
        if (option[1][i]) == (user_answers[i]):
            result += 250
    print()

    print("Summary")
    print("===========================================")
    print(f"correct answers: {option[1]}")
    print(f"your answers: {user_answers}")
    print(f"score: {result}")


quiz(option_4)
