import random
guesses = 0
the_number = random.randint(1, 100) # determines the number for the game
print "I am thinking of a number between 1 and 100."
print "You have to guess it in 6 guesses or less!"

while guesses < 6:        # loops when guesses is less than 6
    print "Take a guess."
    user_guess = int(raw_input())   #Asks for your guess
    guesses = guesses + 1           # +1 to guesses
    if user_guess < the_number:       #11-14 determines the relation of your guess vs. the actual guess
         print "Your guess is too low."
    if user_guess > the_number:
      print "Your guess is too high."
    if user_guess == the_number:       
         break            #stops the loop if guess and number are the same.
       
if user_guess != the_number:    #tells the number after 6 failed attempts
    the_number = str(the_number)
    print('Nope. The number I was thinking of was ' + the_number)

if user_guess == the_number:    #tells you how many tries it took to win
    guesses = str(guesses)
    print('Good job, You guessed my number in ' + guesses + ' guesses!')
    
  
