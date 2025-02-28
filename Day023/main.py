def simple_login():
  username = "username"
  password = "password"
  user_answer = ""
  pass_answer = ""

  while user_answer != username:
    while pass_answer != password:
      user_answer = input("What is your username? ")
      pass_answer = input("What is your password? ")
      if user_answer != username or pass_answer != password:
        print("Wrong username or password. Try again.")
      else:
        print("You have successfully logged in!")
        break
          
simple_login()
