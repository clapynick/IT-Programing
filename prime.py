#For each i from 2 -> sqrt(n)
#if n % i == 0 then return not prime
userInput = raw_input("Enter a number you want to check if it is a prime: ")
while userInput != "Q":
    def isPrime(num):
    #loop through from 2 -> sqrt(n) i++
    #We add +1 to make sure the numbers isnt odd
        max = int(num ** 1/2) + 1 
        for i in range(2, max):
            if num % i == 0:
                print "Sorry but " + userInput +" isnt a prime!"
                return None
        print "Yay! " + userInput +" number is a prime!"
    print(isPrime(float(userInput)))
    userInput = raw_input("Enter a number you want to check if it is a prime (Press Q to quit): ")
exit(0)
