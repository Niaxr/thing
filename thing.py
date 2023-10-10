def register():
    name = []
    usernames = []
    passwords = []
    name.append(input("enter name"))
    usernames.append(input("make a username"))
    passwords.append(input("make a strong password password"))
    return usernames
def login(usernames, password):
    username = input("enter usnername")
    password = input("enter password")
    usernames = []
    passwords = []
    username = ""
    password = ""
    
    if password == passwords[username.index(username)]:
        print("welcome") 
        
    else:  
        print("incorrect username or password")
        
accound_ans = " "
while True:
    account_ans = input("choose: a) login      b) sign up       c) quit")
    if account_ans == "a":
        login(password, username)
        password = []
        username = []
    elif account_ans == "b":
        register()
    else: break
    
