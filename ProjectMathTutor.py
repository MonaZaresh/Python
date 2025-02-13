#pseudocode:
# English or own language description of what you wanna do.
# there aren't any real rule for how to do this :

#import modules
# ask how many questions user wants
#set score start at zero
#loop through number of questions
# create two random numbers and calc answer
# show user the question
# capture answer and modify user score
# output final score 



from  random import randrange as r 
from time import time as t
no_questions = int(input('How many questions do you want?: '))
max_num =int(input('Highest number used in practice?: '))
score = 0
answer_list = []

start = t()
for q in range(no_questions):
    # num1,num2 = r(1,11),r(1,11)
    num1,num2 = r(1,max_num+1),r(1,max_num+1)
    ans = num1 * num2
    u_ans =int(input(f'{num1} X {num2} = '))
    answer_list.append(f'{num1} X {num2} = {ans} your answer : {u_ans}')
    if u_ans == ans:
        score += 1
    end = t()
print(f'Thank you for playing! \nYou got {score} 
      out of {no_questions} ({round(score/no_questions*100)}%) 
      correct in {round(end-start,1)} 
      seconds ({round((end-start)/no_questions,1)}seconds/question)')

for a in answer_list:
    print(a)