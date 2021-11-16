login = "rustem"
or_password = "12345"

name = input("Enter your login  ")
password = input("Enter password  ")

if password == or_password and name.lower() == login:
    print("Hello, ", name.upper(), "!", sep="") 
else:
    print("Error")
