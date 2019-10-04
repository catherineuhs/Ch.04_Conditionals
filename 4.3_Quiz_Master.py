'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''





score = 0
print("Welcome to the quiz! These questions will test your knowledge on strange facts!")
print("(T/F) The cigarette lighter was invented before the match.")



user_input = input("Answer:")
score = 0
if user_input.lower() == "t":
   score = score + 1
   print("Correct!")
   print("Score: ", score)
elif user_input.lower() == "true":
   score = score + 1
   print("Correct!")
   print("Score: ", score)

else:
   print("wrong")
   print("Score:", score)



print(" \n \n How many people are in the world?")
print("A. 10.3 million \n B. 7.53 billion \n C. 6.7 billion \n D. 7.66 trillion \n ")

user_input2 = input("Answer:")

if user_input2.lower() == "b":
    score = score + 1
    print("correct!")
    print("Score: ", score)

else:
    print("wrong")
    print("Score:", score)

print("\n \nWhats 3 + 4?")
user_input3 = int(input("Answer:"))

if user_input3 == 7:
    score = score + 1
    print("Correct!")
    print("Score: ", score)
else:
    print("wrong")
    print("Score:", score)



score = 0

print("\n \n Who is one of the founders of the Apple company?")
user_input4 = input("Answer:")

if user_input4.lower() == "steve jobs":
    score = score +1
    print("Correct!")
    print("Score:", score)
elif user_input4.lower() == "ronald wayne":
    score = score + 1
    print("Correct!")
    print("Score:", score)
elif user_input4.lower() == "steve wozniac":
    score = score + 1
    print("Correct!")
    print("Score:", score)

else:
    print("wrong")
    print("Score:", score)




print("\n \n(T/F)Its physically impossible to lick your elbow")
user_input5 = input("Answer:")

if user_input5.lower() == "T" or "true":
    print("Correct")
    score = score + 1
    print("Score:", score)
else:
    print("wrong")
    print("Score:", score)

print("When did NASA officially land on the moon? \n A. 1970 \n B. 1999 \n C. 1962 \n D. 1969")
user_input6 = input("Answer:")

if user_input6 == "D" or "d" or "1969":
    print("Correct!")
    score = score + 1
    print("Score:", score)

else:
    print("wrong")
    print("Score:", score)
score = 4
print("Whats 30 plus 6?")
user_input7 = int(input("Answer:"))

if user_input7 == 36:
    print("correct!")
    score = score + 1
    print("Score:", score)
else:
    print("wrong")
    print("Score:", score)

percentage = score
print("You've completed the test! Rerun code if you want to retake for a better score.")
print("Test score:", percentage, "/ 7")













