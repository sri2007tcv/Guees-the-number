import random
number = random.randint(1,50)
playername = input("Hey there! What's your name :")
numberofguesses = 0
print('Fine! ' + playername + ' lets guess a number between 1 and 50' )
while numberofguesses < 4:
    guess = int(input())
    numberofguesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('your guess is too high')  
    if guess == number:
         break
if guess == number:
    print('Your guess is correct! You have guessed the number in ' + str(numberofguesses))
else:
    print('Your guess was wrong. The correct number is' + str(number))