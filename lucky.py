import random

num = set()

x = 1
while x != 6:
    guess = input('Pick a number 1-70')
    while guess.isdigit() == False:
        guess = input('no letters only numbers')
    int(guess)   
    x += 1
    if int(guess) > 70:
        guess = input('LESS THAN 70!')
    guess=int(guess)
    num.add(guess)
    print(num)
    

#computers random luckynumbers
def rand70():
    return random.randint(0,70)
comList = set()
while len(comList) != 5:  
    comList.add (rand70())  
print(comList)


#point system
score = len(comList.intersection(num))

if score == 0:
    print("you got them all wrong")
elif score ==1:
    print("you got one right")
elif score ==2:
    print("you got two right")
elif score ==3:
    print("you got three right")
elif score ==4:
    print("you got four right")
elif score ==5:
    print("you got five right")






       
