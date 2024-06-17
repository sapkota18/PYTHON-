import random

# Generate a random choice for the computer: 1 for scissors, 2 for paper, 3 for rock
a = random.randint(1, 3)

# Prompt the user to enter their choice
b = int(input("Enter a number - (1 for scissors) - (2 for paper) - (3 for rock): "))

# Print the computer's choice
print(f"Python chose: {a}")

# Determine and print the result of the game
if a == b:
    print("Draw")
elif (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print("Python won 😓😓😓😓😓")
elif (b == 1 and a == 2) or (b == 2 and a == 3) or (b == 3 and a == 1):
    print("You won 👍👍👍👍👍👍")
else:
    print("Invalid input")
