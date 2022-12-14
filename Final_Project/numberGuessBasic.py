#Number Guesser (Basic) 
#By Fearsome Foursome - Wayne Tobias, Usman Ahmed, Kirk Martin, Ed Hawkins

import random

#Variable to track number of guesses
counter = 0

#Computer picks Secret Number
num = random.randint(1, 10)

#Uncomment to show Secret Number while testing/comment out for game play
print("Secret Number = ",num)

#Variable for exit condition (True when player wins)
win = False

#While loop to continue game until player guesses the Secret Number
while win == False:
    
#Ask player to input a guess    
    guess = int(input('Enter Your Guess: '))

#Update Guess Counter
    counter += 1
  
#Check whether player guessed the Secret Number
    if guess == num:
        win = True
    else:
        print('Try again!')
        continue

#Output results
print('You win! The Secret Number is', num)
print('Number of guesses =', counter)