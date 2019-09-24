import random
theComputerNumber =(random.randint(1,1000000))
print(theComputerNumber)
gameOver = False #This is the game loop'
lowGuessRange=1
highGuessRange=1000000
numberOfGuesses=20
guess = int(input ("Enter a guess: ")) #Ask user to enter an integer guess
while   (gameOver!=True):  
    if guess>theComputerNumber:
        numberOfGuesses-=1 # Number of guess goes down by 1
        print("Wrong answer! You guessed to high! You now have", numberOfGuesses, 'guesses')
        lowGuessRange=guess
        print("The number is between %d and %d!" % (highGuessRange,lowGuessRange)) #Figure out how to change the bounds
        guess = int(input ("Enter in another guess: "))
    elif guess<theComputerNumber:
        numberOfGuesses-=1 
        print("Wrong! You guessed to low! You now have", numberOfGuesses, 'guesses')
        highGuessRange=guess
        print("The number is between %d and %d!" % (highGuessRange,lowGuessRange))
        guess = int(input ("Enter in another guess: "))
    elif guess==theComputerNumber:
       print("Congratulations, you have won the game! It took you %d guesses" %(20-numberOfGuesses))
       gameOver=True 
    if numberOfGuesses==1:
        print("Sorry! You're out of guesses and have lost the game!")
        print("The number was %d" % (theComputerNumber))
        gameOver=True
            
    




