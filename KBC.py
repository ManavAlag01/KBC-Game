questions = [
    "for Rs 5000\nWhat is the capital of India?",
    "for RS 10000\nWho is the current President of the United States?",
    "for Rs 25000\nWhich planet is known as the Red Planet?",
    "for Rs 50,000\nWho painted the Mona Lisa?",
    "for Rs 1,00,000\nWhat is the currency of Japan?"
]

options = [
    ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
    ["A. Joe Biden", "B. Barack Obama", "C. Donald Trump", "D. Kamala Harris"],
    ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
    ["A. Leonardo da Vinci", "B. Pablo Picasso", "C. Vincent van Gogh", "D. Michelangelo"],
    ["A. Yen", "B. Euro", "C. Dollar", "D. Pound"]
]

answers = ['B', 'A', 'B', 'A', 'A']

prize_money = [5000, 10000, 25000, 50000, 100000]

total_questions = len(questions)
current_question = 0
total_prize = 0

print("Welcome to Kaun Banega Crorepati!")
print("You will be asked a series of questions. Answer each question correctly to win the corresponding prize money.")
print("To answer, enter the option letter (A, B, C, D) or 0 to quit and press Enter.\n")


for question,options_list,answer,prize in zip(questions,options,answers,prize_money):
    print(f"Question {current_question + 1} {question}")
    for option in options_list:
        print(option)
    print("enter 0 to exit")    
    user=input("Choose your answer:").upper()
    if user=='0':
       print("you choose to quit the game")
       print("you won total price Rs",total_prize,)
       break
    if user==answer:
     total_prize=total_prize+prize
     print("correct answer")        
     print("you have won Rs",prize)
     print("your total prize is Rs",total_prize)  
    
    else:
     print("Wrong answer,your take home money is",total_prize)
     break

    current_question=current_question+1
    print()

if current_question==total_questions:
    print("Congratulations! You've won the maximum prize of Rs", total_prize)