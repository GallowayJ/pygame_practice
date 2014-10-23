import random

guessesTaken=0

print "What's good famalam?"
playerName=raw_input("Tell me your name, innit?\n")
print "{0} I've been waiting for you, let's play a game! :)".format(playerName)

number = random.randint(1,20)
#print number

def validNumber(rawinput):
    if rawinput.isdigit() == True
    print great

while guessesTaken < 6:
    lives = 6-guessesTaken
    print "{0}, you have {1} lives remaining!".format(playerName, lives)
    #print guessesTaken
    print "Guess the integer that I'm thinking of"

    guess = int(raw_input("What's your guess?"))
    if guess.isdigit() == True:
    guessesTaken +=1 
    if guessesTaken ==6:
        print "You're all out of guesses {}, better luck next time...biatch!!".format(playerName)
        break
    elif guess > 20:
        print "{0} is {1} less than 20?".format(playerName,guess)

    elif guess < 0:
        print "{0} is {1} more than 0?".format(playerName,guess)
           
    elif guess == number and guessesTaken <2 :
        print "{0}, be honest did you cheat or are you just lucky?".format(playerName)
        break
    
    elif guess == number:
        print "Congrats, you got it with {} lives remaining!".format(lives)
        break
    
    elif guess < number:
        print "Too low, mofo!"
        
    else:
        print "Too high, cherrypie!"
    

