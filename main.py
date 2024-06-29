import random
print("Welcome to number guessing game!")
print("A number would be randomly generated from 0 to 100.")
difficulty = input("Choose the difficulty hard or easy : ").lower()
chances = 0
if difficulty == "hard":
    print("You have a total of 5 chances to guess the number.")
    chances = 5
elif difficulty == "easy":
    print("You have a total of 10 chances to guess the number.")
    chances = 10
else:
    print("Choose correct difficulty")
    exit
number = random.randint(0,100)

while chances!=0:
    player_input = int(input("Enter the number: "))
    if player_input == number:
        print("You guessed the correct number.")
        break
    elif player_input > number:
        chances-=1
        print(f"Too high. You have {chances} left.")
    else:
        chances-=1
        print(f"Too low. You have {chances} left.")
    
if chances == 0:
    print("You ran out of chances. You Lost.")
    exit
        
