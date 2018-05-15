import random

number = random.randint(0,3)

words = ("strawberry","blueberry","raspberry","blackberry")
hint1= ["red fruit","blue fruit","fruit with an r","black fruit"]
hint2= ["straw","circular","sweet","bush"]

guess = ""

counter = 1

secretword = words[number]

while True:
    print("Guess the secret word!")
    print("Type 'hint1', 'hint2', 'first letter', 'last letter', or 'give up' for help.")
    guess = input()

    if guess == secretword:
        print("You win!")
        print("It took you " + str(counter) + "guesses.")
        break

    elif guess == "hint1":
        print(hint1[number])

    elif guess == "hint2":
         print (hint2[number])

    elif guess == "first letter":
         print(secretword[0])

    elif guess == "last letter":
         print(secretword[-1])

    elif guess == "give up":
         print("The secret word was " + secretword)
         break

    else:
        print("Try again!")
        counter += 1
            
        
