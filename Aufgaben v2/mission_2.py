#Aufgabe 2: Kennwort Validierung
# - mindestens eine große und kleine Buchstabe   islower() isupper()
# - mindestens eine Zahl
# - mindestens ein Zeichen $#@%
# - minimum 4 Zeichen
# - maximum 10 Zeichen




from operator import truediv
from xmlrpc.client import boolean


def function(string):
    chars = ['$', '#', '@', '%']
    print("\n")
    bBool = False
    
    if not any(char.islower() for char in string): 
        print("Password must contain at least 1 lower case letter!") 
        bBool = True
        
    if not any(char.isupper() for char in string):
        print("Password must contain at least 1 upper case letter!") 
        bBool = True

    if not any(char.isnumeric() for char in string): 
        print("Password must contain at least 1 number!") 
        bBool = True

    if not any([char in string for char in chars]):
        print("Password must contain at least 1 char of ['$', '#', '@', '%']!")  
        bBool = True

    if (len(string) < 4):
        print("Password must contain at leat 4 characters!") 
        bBool = True
    
    if(len(string) > 10):
        print("Password can be a maximum of 10 characters long!") 
        bBool = True

    return bBool

def main():
    
    password = input("Enter your password: ")
    boo = function(password)
    while boo:
        print("\v\v ~~~PASSWORD NOT OKAY~~~ \v\v")
        password = input("Enter your password: ")
        boo = function(password)   
         
    print("\v\v ~~~PASSWORD OKAY~~~ \v\v")
if __name__ == "__main__":
    main()