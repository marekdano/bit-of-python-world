from random import randint

print("Play rock, paper, scissors game.")

player = input("Player, make your move: ").lower()
# p2 = input("Player 2: rock, paper, or scissors ")
rand_num = randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else: 
	computer = "scissors" 

print(f"Computer plays {computer}")

if player == computer:
  print("It's a tie!")
elif player == "rock":
	if computer == "scissors":
		print("player wins!")
	elif computer == "paper":
		print("computer wins!")
elif player == "paper":
	if computer == "rock":
		print("player wins!")
	elif computer == "scissors":
		print("computer wins!")
elif player == "scissors":
	if computer == "paper":
		print("player wins")
	elif computer == "rock":
		print("computer wins!")
else:
  print("Something went wrong.")