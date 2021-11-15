login = "Rustem"
or_password = 12345

name = input("Enter your login  ")
password = input("Enter password  ")
print(password)
if or_password == password:
    print("Hello, ", name, "!", sep="")
else:
    print("Error")
