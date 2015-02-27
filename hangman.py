#Code done by Nick Parsons
import random
import time
playAgain = "yes"
while playAgain == "yes":
    letUsed = []
    print "Enter if you are"
    print "1.) Playing by yourself"
    playerAmount = raw_input("2.) Playing with two or more players: ")
    if playerAmount == "2":
        word = raw_input("Enter a word you want the user to guess: ")
        for i in range(0, 45):
            print ""
    elif playerAmount == "1":
        ##Random word gen
        print "Loading random word..."
        time.sleep(2)
        #This will set lineChooser to a random interger between 0 and 232.
        lineChooser = random.randint(0, 232)
        
        #Here we read from the words.txt file to choose a random word!
        word_file = open("words.txt", "r")
        #Here we set word equal to a random line from the file words. 
        word = word_file.readlines()[lineChooser]
        #Here we set word equal to the whole word except for the last character because for some reason it genrates an extra file when reading from a file.
        word = word[0:len(word)-1]
        word_file.close()
    else:
        print "Please enter 1 or 2 next time not " +playerAmount
        time.sleep(3)
        exit(0)
        
    print ""
    print "Hangman by: Nick Parsons"
    print "Please note that entering a capital Q will quit the game!"
    print ""
    print "You have 11 lives. Good luck!"
    print ""
    wordList = []
    display = []
    guess = None
    lives = 11
    for i in range(0, len(word)):
        wordList.append(word[i])
                
        display.append("_ ")
    #Displays word interface
    print "Word: " +"".join(display)
    print "Lives: " + str(lives)
    print "Letters Used: You have used no letters!"
    while guess != "Q":
        guess = raw_input("Make your guess: ")
        letUsed.append(guess)
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
            print "Letters used: " +", ".join(letUsed)

            if lives <= 0 and guess != "hack(force.win(hangman))":
                print "You lost!"
                guess = "Q"

            elif guess == "hack(force.win(hangman))":
                print "Well done you guessed the word!"
                print word
                i = 1
                guess = "Q"

            elif guess == "hack(add.lives())":
                lives += 100

            elif guess == "hack(show.text(ans))":
                print ""
                time.sleep(2)
                print "Executing hack..."
                time.sleep(3)
                for i in range(0, 10):
                    print "432865465723hgdfYYGFhkfhdHFGYYU&^53ygjd"
                    print "UKdlhdksl&#84o5835938759HFhfgfhfbfd.s>>fd.fu3"
                    print "uduDJdnnsla;fnsnfsnska&36%vVVmd"
                    print "JavaToPython.words(acces).CODE(327465663~@VVMAv267GDFvdvstYSydu{key:AccesPoint event})"
                print ""
                print "Decompiling word..."
                time.sleep(2.5)
                print ""
                print "Accesing main python variables..."
                time.sleep(2)
                print ""
                print "unwrapping vMAv python PDY..."
                time.sleep(1.5)
                print "Done!..."
                print "THE WORD ANSWER IS: " +word

        elif i == 1:
            print ""
            print "Correct!"
            print "Word: " +"".join(display)
            print "Lives: " + str(lives)
            print "Letters used: " +", ".join(letUsed)

            if currentWord == wordList:
                print "Well done you guessed the word!"
                guess = "Q" 
            
    if i != 1:
        print "The word was: " +word

    playAgain = raw_input("Would you like to play again?: ")
    for i in range(0, 45):
        print ""

print "Thankyou for using my hangman game"
print "Quiting..."
time.sleep(2.5)
exit(0)

