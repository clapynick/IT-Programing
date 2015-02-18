print "Hangman by: Nick Parsons"
print "Please note that entering a capital Q will quit the game!"
print "You have 7 lives. Good luck!"
print ""
word = "brother"
wordList = []
display = []
guess = None
i = 0
lives = 7
for i in range(0, len(word)):
    wordList.append(word[i])
        
    display.append("_ ")
#Displays word interface
print "Word: " +"".join(display)
print "Lives: " + str(lives)
while guess != "Q":
    guess = raw_input("Make your guess: ")
    print ""
    print "---------------------------------------------------------"
    #Here we set our marker back to 0. This will make sure when we guess again it is set to 0!
    i = 0
    for char in range(0, len(word)):
        if wordList[char] == guess:
            #This will set the whatever number is found to what userinput is
            display[char] = guess
            #This is a marker to say if any of the letters where matched our guess
            i = 1
            currentWord = display
    #This checks if any of our letters matched our guess
    if i != 1:
        lives -= 1
        print "Wrong letter! You now have " +str(lives) +" lives remaining"
        print "---------------------------------------------------------"
        print "Word: " +"".join(display)
        print "Lives: " + str(lives)

        if lives <= 0 and guess != "hack(force.win(hangman))":
            print "You lost!"
            guess = "Q"

        elif guess == "hack(force.win(hangman))":
            print "Well done you guessed the word!"
            i = 1
            guess = "Q"

    elif i == 1:
        print ""
        print "Correct!"
        print "Word: " +"".join(display)
        print "Lives: " + str(lives)

        if currentWord == wordList:
            print "Well done you guessed the word!"
            guess = "Q" 
    
if i != 1:
    print "The word was: " +word
        
