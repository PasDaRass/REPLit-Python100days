from replit import audio
import os, time


def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    os.system("clear")
    # Start taking user input and doing something with it
    print("Press P to Play / Pause")
    print("Press Q to Exit to Menu")
    press = input().upper()
    if press == "P":
      source.paused = not source.paused
    elif press == "Q":
      source.paused = True
      break
    else:
      continue

running = True
while running == True:
  # clear the screen 
  os.system("clear")
  # Show the menu
  print("-- Music Player --")
  print()
  print("Press 1: Go to Track")
  print("Press 2: Exit App")
  # take user's input
  press=int(input())
  # check whether you should call the play() subroutine depending on user's input
  if press == 1:
    os.system("clear")
    play()
  elif press == 2:
    running = False
    os.system("clear")
    quit()
  else:
    continue
