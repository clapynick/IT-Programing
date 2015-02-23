#Code done by Nick Parsons
import random
import time
playAgain = "yes"
while playagain == "yes":
    print "Enter if you are"
    print "1.) Playing with two or more players"
    playerAmount = raw_input("2.) Playing with one person: ")
    if playerAmount == "1":
        word = raw_input("Enter a word you want the user to guess: ")
        for i in range(0, 45):
            print ""
    elif playerAmount == "2"
        ##Random word gen
        print "Loading random word..."
        time.sleep(2)
        wordChooser = random.randint(1, 20)
        
        if wordChooser == 1:
            word = "jazz"
        elif wordChooser == 2:
            word = "brother"
        elif wordChooser == 3
            word = "python"
        elif wordChooser == 4:
            word = "fantastic"
        elif wordChooser == 5:
            word = "tennis"
        elif wordChooser == 6:
            word = "chair"
        elif wordChooser == 7:
            word = "table"
        elif wordChooser == 8:
            word = "tie"
        elif wordChooser == 9:
            word = "bucket"
        elif wordChooser == 10:
            word = "clock"
        elif wordChooser == 11:
            word = "hangman"
        elif wordChooser == 12:
            word = "chess"
        elif wordChooser == 13:
            word = "planet"
        elif wordChooser == 14:
            word = "noodles"
        elif wordChooser == 15:
            word = "pancake"
        elif wordChooser == 16:
            word = "hair"
        elif wordChooser == 17:
            word = "computer"
        elif wordChooser == 18:
            word = "bookstore"
        elif wordChooser == 19:
            word = "church"
        elif wordChooser == 20:
            word = "glass"
        else:
            print "Error: RandomInt is not a number that suits the if"
    else:
        print "Sorry but " +playerAmount +" isn't valid. Please enter 1 or two next time!"
        time.sleep(3)
        exit(0)
    print ""
    print "Hangman by: Nick Parsons"
    print "Please note that entering a capital Q will quit the game!"
    print ""
    print "You have 7 lives. Good luck!"
    print ""
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
    while guess != "Q"
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

            if lives <= 0 and guess != "hack(force.win(hangman))" and guess != hack(add.lives()) and guess != hack(show.text(ans)):
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
                print "THE WORD ANSWER IS: " +word

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

    playAgain = raw_input("Would you like to play again?: ")
    for i in range(0, 45):
        print ""

print "Thankyou for using my hangman game"
print "Quiting..."
time.sleep(2.5)
exit(0)

