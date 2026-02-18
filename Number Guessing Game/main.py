from random import randint

def play(chances:int)->None:
    print()
    num = randint(1,100)
    attempts = 0
    while(attempts<chances):
        try:
            usr_input = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter the number in between 1 and 100")
        if(usr_input == num):
            print(f"Congratulations! you guessed the correct number in {attempts} attempts")
            return
        elif(usr_input>num):
            print(f"Incorrect! The number is less than {usr_input}.")
        else:
            print(f"Incorrect! The number is greater than {usr_input}.")
        attempts+=1
    print("Better luck next time.")

def difficulty()->None:
    flag = True
    level = {1:(10,"Easy"),2:(5,"Medium"),3:(3,"Hard")}
    while flag:
        print()
        print("Please select the difficuly level: ")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")
        print()
        try:
            choice = int(input("Enter your choice: "))
            flag = False
            print(f"Great! you have selected the {level.get(choice)[1]} level.")
            play(level.get(choice)[0])
        except KeyError:
            print("Wrong difficuly level")
            print()
        except ValueError as e:
            print("That was no valid option")

def greet()->None:
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
def main()->None:
    greet()
    difficulty()

if __name__ == "__main__":
    main()