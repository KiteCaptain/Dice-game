import random

def roll():

    min_value = 1

    max_value = 6

    roll = random.randint(min_value, max_value)

    return roll

while True:

    players = input("enter the number of players(2-4): ")


    if players.isdigit():

        players = int(players)

        if 2 <= players <= 4:

            break
        else:

            print(" players must be between 2 and 4")

    else:

        print(" invalid choice, try again!")


max_score = 50

player_scores = [0 for player_idx in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):

        print("\n turn for player",player_idx + 1, "has started \n")

        print("your total score is",player_scores[player_idx], "\n")

        

        current_score = 0

        while True:

            should_roll = input("Do you want to roll(y):")

            if should_roll.lower() != "y":

                break

            value = roll()

            if value == 1:

                print("Your rolled 1, your turn done!")

                current_score = 0

                break

            else:

                current_score += value

                print( "you rolled a", value)

                print(" your current score is:", current_score)



        player_scores[player_idx] += current_score

        print("your total score is:",player_scores[player_idx])


max_score = max(player_scores)

winning_idx = player_scores.index(max_score)

print ("player number",winning_idx + 1, " won with",max_score, "points")

input("press enter to exit")

            

    
