#login project

print("Please input your username and password.\n")
username = input("username: ")
password = input("password: ")

with open("login.txt", "w") as f:
    f.write("Username: {}\nPassword: {}".format(username, password))
