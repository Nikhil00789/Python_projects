import random

results = [("rock","scissors"), ("scissors", "paper"), ("paper", "rock"), ("rock", "lizard"), ("lizrd", "spock"),
           ("spock", "scissors"),("scissors", "lizard"), ("lizard" ,"paper"), ("paper", "spock"), ("spock", "rock")]
moves = [result[1] for result in results]

player_score, computer_score = (0,0)
player = input("Enter rock / paper / scissors / lizard / spock / quit: ").lower()
while player != "quit":
    computer = random.choice(moves)
    print("You chose {}, I chose {}".format(player, computer))
    if player == computer:
        print("It's a tie!")
    elif(player, computer) in results:
        print("You win")
        player_score += 1
    elif (computer, player) in results:
        print("I win")
        computer_score += 1
    else:
        print("Invalid input")
    player = input("Enter rock/ paper/ scissors / lizard / spock / quit: ").lower()

print("FINAL SCORES")
print("You {}, Me {}".format(player_score, computer_score))
