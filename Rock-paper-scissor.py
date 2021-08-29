import random

comp_wins = 0
player_wins = 0

def Choose_Option():
    user_Choice = input("Choose Rock, Paper or Scissors: ")
    if user_Choice in ["Rock", "rock", "r", "R"]:
        user_Choice = "R"

    elif user_Choice in ["Paper", "paper", "p", "P"]:
        user_Choice = "P"    

    elif user_Choice in ["Scissors", "scissors", "s", "S"]:
        user_Choice = "S"    

    else:
        print("I don't understand, try again. :-)") 
        Choose_Option()

    return user_Choice

def Computer_Option():
    Comp_Choice = random.randint(1,3)
    if Comp_Choice == 1:
        Comp_Choice = "R"

    elif Comp_Choice == 2:
        Comp_Choice = "p"

    else:
        Comp_Choice = "S"   

    return Comp_Choice

while True:
    print(" ")
    user_Choice = Choose_Option()
    Comp_Choice = Computer_Option()
    print(" ")

    if user_Choice == "R":
        if Comp_Choice == "R":
            print("You Choose Rock. The computer Choose Rock.You tied.")
            
        elif Comp_Choice == "P":
            print("you choose rock.computer choose paper.You lose.")
            comp_wins += 1

        elif Comp_Choice == "S":
            print("you choose rock.computer choose scissors.You win.")
            player_wins += 1

    elif user_Choice == "P":
        if Comp_Choice == "R":
            print("You Choose Paper. The computer Choose Rock.You win.")
            player_wins += 1
           
        elif Comp_Choice == "P":
            print("you choose paper.computer choose paper.You tied")
            
        elif Comp_Choice == "S":
            print("you choose paper.computer choose scissors.You lose.")
            comp_wins += 1    
    
    elif user_Choice == "S":
         if Comp_Choice == "R":
            print("You Choose scissors. The computer Choose Rock.You loose.")
            comp_wins += 1

         elif Comp_Choice == "S":
            print("you choose scissors.computer choose scissors.You tied.")
            
         elif Comp_Choice == "P":
            print("you choose scissors.computer choose paper.You win.")
            player_wins += 1            

    print(" ")
    print("Player Wins: " + str(player_wins))
    print("Computer Wins: " + str(comp_wins)) 
    print(" ")


    user_Choice = input("Do you want to play again? (y/n)")
    if user_Choice in ["Y", "y", "yes", "Yes"]: 
        pass
    elif user_Choice in ["No", "no", "N", "n"]:
        break
    else:
        break      