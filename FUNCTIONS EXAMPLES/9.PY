"""9. Royal Kids Bank
Design a Banking App in Python that has the following functionalities:-
User can:-
◆OPEN ACCOUNT by username and password of his choice. On Opening account, his initial balance will be ₹ 25,000/-. Once he opens account, he can login by re-entering the same username & password.
◆LOGIN is compulsory to perform any task such as withdrawal, deposit or balance check. If the user name or password do not match, he can not Login. Once he is logged in, he can do as many transactions as he wants. He needs to Logout after he finishes all the transactions
◆DEPOSIT will enable user to deposit amount of money of his choice. His balance should be updated after the task completes.
◆WITHDRAW will enable user to withdraw amount of money of his choice. The only condition is that his balance at any point can not go less than ₹10,000/-. If this can happen after his withdrawal, your program must not allow that transaction. His balance should be updated after the task completes.
◆CHECK BALANCE will show the latest updated balance to user.
◆LOGOUT will exit the user from the program
You should use these functions in your program: login(), deposit(), withdraw(), checkBalance()"""

user = {
    "Hardik": 21549,
}
balance = {
    "Hardik": 25000,
}


def new_account():
    new_user = input("Enter Your UserName : ")
    if list(user.keys()).count(new_user) != 0:
        print("User Already Exist.")
        print("Try Again.")
    else:
        new_pwd = int(input("Enter Your Password :"))
        user[new_user] = new_pwd
        balance[new_user] = 25000
        print("Account Created Successfully! Your Default Balance Is Set To Rs.25000")


def login():
    check = input("Are You New User ? (Yes/No) : ")
    if check.lower() == "yes":
        new_account()
    else:
        uName = input("Enter Your Username : ")
        if list(user.keys()).count(uName) == 0:
            print("User Does Not Exist. Try Again.")
        else:
            uPassword = int(input("Enter Your Password : "))
            if user[uName] == uPassword:
                print("Login Successfull.")
                return uName
            else:
                print("Login Failed.")
                print("Try Again")
                exit()


def deposit():
    uName = login()
    deposit_amnt = int(input("Enter How Much Amount You Want To Deposit : "))
    balance[uName] += deposit_amnt


def withdraw():
    uName = login()
    withdraw_amnt = int(input("Enter How Much Amount You Want To Withdraw : "))
    if balance[uName] - withdraw_amnt <= 10000:
        print("Withdraw Not Possible Because After This Transaction Your Balance Will Be Less Than Rs.10000")
        print("Try Again")
        exit()
    else:
        balance[uName] -= withdraw_amnt


def checkBalance():
    uName = login()
    print(f"Balance Of {uName} = {balance[uName]}")


while (True):
    print("1--Create New Account")
    print("2--Deposit")
    print("3--Withdraw")
    print("4--CheckBalance")
    print("5--Exit")
    choice = int(input("Enter Your Choice : "))
    match choice:
        case 1: new_account()
        case 2: deposit()
        case 3: withdraw()
        case 4: checkBalance()
        case 5: exit(0)
