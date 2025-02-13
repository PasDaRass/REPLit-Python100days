from getpass import getpass as input

print("Welcome to Rock, Paper, Scissors!")
print("Type either R, P or S on your turn")

player1_move = input("Player 1 > ").upper()
while(player1_move != "R" 
      and player1_move != "P" 
      and player1_move != "S"):
  print("You did not select *R*, *P* or *S*, please try again")
  player1_move = input("Player 1 > ").upper()
player2_move = input("Player 2 > ").upper()
while(player2_move != "R" 
      and player2_move != "P" 
      and player2_move != "S"):
  print("You did not select *R*, *P* or *S*, please try again")
  player2_move = input("Player 2 > ").upper()
print()
print("Player 1 selected", player1_move)
print("Player 2 selected", player2_move)

if player1_move == player2_move:
  print("Both players tie with a draw")
elif player1_move == "R":
  if player2_move == "P":
    print("Player 2 wins")
  else:
    print("Player 1 wins")
elif player1_move == "P":
  if player2_move == "S":
    print("Player 2 wins")
  else:
    print("Player 1 wins")
elif player1_move == "S":
  if player2_move == "R":
    print("Player 2 wins")
  else:
    print("Player 1 wins")
