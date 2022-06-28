#Create user accounts
#Create a master password for the user
#Store that password to a text file..
#Encrypt that password..
class User:
    #variables
    #functions
#///////////////////////////////////////////////////////////////
def create_user():
    print("Create user name")
    name = input()
    print("Your name is " + name)
    return name
#///////////////////////////////////////////////////////////////
def create_pass(user):
    state = True
    print("Please enter a password")
    psw1 = input()
    print("Please confirm password")
#///////////////////////////////////////////////////////////////
    while state:
        psw2 = input()
        if psw1 == psw2:
            print("Okay " + user + " password is all set")
            state = False
        elif psw1 != psw2:
            print("Incorrect. Please confirm password again..")
#////////////////////////////////////////////////////////////////
def main():
    '''obj = User()
    obj.username
    obj.password
    obj.encryptpass()'''
#///////////////////////////////////////////////////////////////
    user = create_user()
    create_pass(user)

if __name__=="__main__":
    main()
