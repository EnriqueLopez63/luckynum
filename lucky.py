from audioop import add
import random
from secrets import choice
num = []


x = 1
while x != 6:
    guess = input('Pick a number 1-70')
    while guess.isdigit() == False:
        guess = input('no letters only numbers')
    int(guess)   
    x += 1
    if int(guess) > 70:
        guess = input('LESS THAN 70!')
    num.append(guess)
    print(num)
    

#computers random luckynumbers
comList = []
x = 1
value = ("yurr") 
comList = set()
while x !=6: 
    value = random.randint(1, 70)   
    comList.add (value)  
    x += 1
print(comList)


#point system




       
