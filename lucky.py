import random
num = []


x = 1
while x != 6:
    guess = input('Pick a number 1-70')
    while guess.isdigit() == False:
        guess = input('no letters only numbers')
    int(guess)
    num.append(guess)
    print(num)
    x += 1
    if int(guess) > 70:
        print('LESS THAN 70!')
    print(num)

    

#computers random luckynumbers
comList = []
x = 1
while x !=6:
    value = random.randint(1, 10)
    x += 1
    comList.append(value)
    print(comList)
    #comList = []
    #l = list(set(l))




       
   
