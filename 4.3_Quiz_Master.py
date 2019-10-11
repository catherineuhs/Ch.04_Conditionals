'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''





score = 0
print(" \n \n Welcome to the quiz! These questions will test your knowledge on strange facts!")
print("\n \n \n 1. (T/F) The cigarette lighter was invented before the match.")



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



print(" \n \n 2. How many people are in the world?")
print("A. 10.3 million \n B. 7.53 billion \n C. 6.7 billion \n D. 7.66 trillion \n ")

user_input2 = input("Answer:")

if user_input2.lower() == "b":
    score = score + 1
    print("correct!")
    print("Score: ", score)

else:
    print("wrong")
    print("Score:", score)

print("\n \n 3. Whats 3 + 4?")
user_input3 = int(input("Answer:"))

if user_input3 == 7:
    score = score + 1
    print("Correct!")
    print("Score: ", score)
else:
    print("wrong")
    print("Score:", score)




print("\n \n 4. Who is one of the founders of the Apple company?")
user_input4 = input("Answer:")

if user_input4.lower() == "steve jobs":
    score = score + 1
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




print("\n \n 5. (T/F)Its physically impossible to lick your elbow")
user_input5 = input("Answer:")

if user_input5.lower() == "t" or "true":
    print("Correct")
    score = score + 1
    print("Score:", score)

elif user_input5.lower() == "true":
    print("Correct")
    score = score + 1
    print("Score:", score)

else:
    print("wrong")
    print("Score:", score)

print(" \n \n 6. When did NASA officially land on the moon? \n A. 1970 \n B. 1999 \n C. 1962 \n D. 1969")
user_input6 = input("Answer:")
if user_input6.lower() == "d":
    print("Correct!")
    score = score + 1
    print("Score:", score)

else:
    print("wrong")
    print("Score:", score)


print(" \n \n 7. Whats 30 plus 6?")
user_input7 = int(input("Answer:"))

if user_input7 == 36:
    print("correct!")
    score = score + 1
    print("Score:", score)
else:
    print("wrong")
    print("Score:", score)

percentage = score
print(" \n \n \nYou've completed the test! Rerun code if you want to retake for a better score.")
print("Test score:", percentage, "/ 7")

final_exam_worth=percentage/7*100
print(final_exam_worth)

if final_exam_worth >= 90:
    print("You got an A!")
elif final_exam_worth>=80:
    print("You got a B!")
elif final_exam_worth>=70:
    print("You got a C!")
elif final_exam_worth>=60:
    print("You got a D")
else:
    print("Tansfer!")













