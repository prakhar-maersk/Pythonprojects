import csv
import emoji
data={"username":["z","Amit","Prakhar","Praveen"],
      "password":["1","1234","prakhar","waytosearch"]}
with open("login.csv","w",newline="") as f:
    write=csv.writer(f,delimiter=",")
    write.writerow(data.keys())
    for i in zip(data["username"],data["password"]):
        write.writerow(i)


def userreg():
    name=input("Enter New Username\n",)
    pas=input("Enter Password\n")
    cnfmpas=input("Enter Password again\n")
    if pas!=cnfmpas:
        print("Enter same password in password and confirm password\n")
        userreg()
    else:
        lst=[name,pas]
        with open("login.csv",mode="a") as f:
            likhna=csv.writer(f,delimiter=",")
            likhna.writerow(lst)
            # likhna.writerows(pas)
        print(f"New user created with username {name}\n")

def userlogin(attempts=3):
    if attempts>0:
        with open("login.csv","r") as f:
            name = input("Enter your username\n")
            pas = input("Enter password\n")
            log = 0

            for i in f:

                if i==name + "," + pas+"\n":
                    log+=1
                    break
            if log==1:
                print(f"Welcome {name}! \n")
                return True
            else:
                print("User account not found.Please enter correct information")

                attempts-=1
                print(f"You have {attempts} attempts left")
                userlogin(attempts)
    else:
        print("You have exceded max attempts. Please try again Later\n")

def logout():
    print("You have successfully logged out\n")
    # r = int(input("Press 1 for New User Registration\n Press 2 for User Login\n"))
    # return r


x=1
while x==1:
    try:
        p = int(input("1. New User Registration\n2. User Login\n3. logout\n"))
    except:
        print("Enter a valid integer\n")
        continue
    if p==1:
        userreg()
    elif p==2:
        userlogin(attempts=3)
    elif p==3:
        logout()
        break
    else:
        print("Enter Correct Input\n")
    try :
        x=int (input("press 1 to Perform more action\n"))
    except:
        print("Enter a valid integer\n")
print("Thank you, visit again",emoji.emojize(":grinning_face_with_big_eyes:"))