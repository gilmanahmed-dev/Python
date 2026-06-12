import random

rps = ["Rock","Paper","Scissors"]

while True:
    shoot = random.choice(rps)
    me = input("Rock, Paper or Scissors ? ")
    if me.lower() == "exit":
        break
    
    if me.capitalize() not in rps:
        print("Enter a valid choice")
        
    elif me.lower() == shoot.lower():
            print("Tie")
            
    elif (me.lower() == "rock" and shoot.lower() == "scissors") or\
         (me.lower() == "paper" and shoot.lower() == "scissors") or\
         (me.lower() == "scissors" and shoot.lower() == "paper"):
            print("Win")
    else:
        print("Lost")