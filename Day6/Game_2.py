import random

player1_position = 0
player2_position = 0

condition_dict = {24: 1, 17: 9, 14: 3, 19: 7, 9: 0}

for turn in range(1, 101):
    input("Player 1, press Enter to roll the die: ")
    roll = random.randint(1, 6)
    player1_position += roll
    
    if player1_position in condition_dict:
        original_position = player1_position
        player1_position = condition_dict[player1_position]
        print(f"Player 1 landed on {original_position}, so back to {player1_position}")
    else:
        print(f"Player 1 rolled a {roll}. Player 1's current position is {player1_position}")
    
    if player1_position >= 30:
        print("Player 1 wins!")
        break
    
    input("Player 2, press Enter to roll the die: ")
    roll = random.randint(1, 6)
    player2_position += roll
    
    if player2_position in condition_dict:
        original_position = player2_position
        player2_position = condition_dict[player2_position]
        print(f"Player 2 landed on {original_position}, so back to {player2_position}")
    else:
        print(f"Player 2 rolled a {roll}. Player 2's current position is {player2_position}")
    
    if player2_position >= 30:
        print("Player 2 wins!")
        break

else:
    print("Game over, maximum attempts reached!")



 