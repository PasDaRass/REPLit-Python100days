from getpass import getpass as input

p1_rounds_won = 0
p2_rounds_won = 0

game_run = True
print(
  "👊 ✋ ✌️ ", "Welcome to Rock, Paper, Scissors", "👊 ✋ ✌️"
)
print()
print("Which player can win 3 rounds first")
print()
while game_run == True:
  print("Rounds won:")
  print("P1 -", p1_rounds_won, "|", "P2 -", p2_rounds_won)
  if p1_rounds_won == 3:
    print("🏆 Player 1 has won 3 rounds! 🏆")
    game_run = False
    break
  elif p2_rounds_won == 3:
    print("🏆 Player 2 has won 3 rounds! 🏆")
    game_run = False
    break
  print()
  print("Type either R, P or S on your turn")

  # input validation
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
  print()
  # game result
  if player1_move == player2_move:
    print("Both players tie with a draw")
  elif player1_move == "R":
    if player2_move == "P":
      print("Player 2 wins this round")
      p2_rounds_won += 1
      continue
    else:
      print("Player 1 wins this round")
      p1_rounds_won += 1
      continue
  elif player1_move == "P":
    if player2_move == "S":
      print("Player 2 wins this round")
      p2_rounds_won += 1
      continue
    else:
      print("Player 1 wins this round")
      p1_rounds_won += 1
      continue
  elif player1_move == "S":
    if player2_move == "R":
      print("Player 2 wins this round")
      p2_rounds_won += 1
      continue
    else:
      print("Player 1 wins this round")
      p1_rounds_won += 1
      continue
print()
print("🕹️  Thank you for playing! 🕹️")
