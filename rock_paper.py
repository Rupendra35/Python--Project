import   random
user_wins=0
computer_wins=0
options=["rock","paper","scissor"]
while True:
    user_input=input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input=="q":
        break
    if user_input not in options :
        continue
    random_number=random.randint(0,2)
    computer_picks=options[random_number]
    print("computer picked",computer_picks+".")
    if user_input==computer_picks:
        print("try again")
        continue
    elif user_input=="rock" and computer_picks=="scissor":
        print("you won")
        user_wins+=1

    elif user_input == "paper" and computer_picks == "rock":
        print("you won")
        user_wins += 1

    elif user_input=="scissor" and computer_picks=="paper":
        print("you won")
        user_wins+=1

    else:
        print("you lose")
        computer_wins+=1
print("you won",user_wins,"times.")
print("computer wins",computer_wins,"times.")
print("goodbye")
