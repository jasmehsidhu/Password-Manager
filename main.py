def createAcc():
  user_name = input("Please choose a username: ")
  pass_word = input("please choose a password: ")
  pass_open = open("password.txt", "w")
  user_open = open("username.txt", "w")
  print("account created")
  pass_open.write(pass_word)
  user_open.write(user_name)
def loginId():
  user_open = input("Please enter the username: ")
  with open("username.txt") as f:
    l = f.read()
  with open("password.txt") as m:
    o = m.read()
  if user_open == l:
    pass_open = input("Please enter the password: ")
    if pass_open == o:
      print("access given")
    else:
      print("invalid password,access denied")
  else:
    print("incorrect username")
def forgotPass():
  check_user = input("Please enter your username: ")
  with open("username.txt") as f:
    l = f.read()
  if check_user == l:
    j = input("please enter first digit of your password: ")
    try:
      m1 = open("password.txt")
      l1 = m1.read()
      if l1[0] == j:
        try:
          print(f"your password is'{l1}'")
        except:
          print("Something wrong happend")
      else:
          print("can't provide the password,you entered wrong letter")
    except:
      print("Something wrong happend")
  else:
    print("can't provide the password")
def changePass():
  j = input("Enter your username: ")
  with open("username.txt") as f:
    l = f.read()
  if j == l:
    c = input("Enter the old password: ")
    try:
      m = open("password.txt")
      m1 = m.read()
      if m1 == c:
        try:
          m2 = input("Enter the new password: ")
          m3 = open("password.txt", "w")
          m3.write(m2)
          print("Password changed succesfully")
        except:
          print("Something went wrong")
      else:
        print("Wrong passsword")
    except:
      print("something went wrong")
  else:
    print("incorrect username")
check_pass = input("What do you wanna do: ")
if check_pass == "create account":
  createAcc()
elif check_pass == "login":
  loginId()
elif check_pass == "forgot password":
  forgotPass()
elif check_pass == "change password":
  changePass()
else:
  print("Invalid entry")
