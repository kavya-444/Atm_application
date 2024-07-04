import time
print("Please enter your atm card")
time.sleep(1)
password=1234
pin=int(input("enter your atm pin:"))
balance=10000
if pin==password:
    print("""
    1==balance
    2==withdraw
    3==deposit
    4==exit
    """)
    try:
        option =int(input("Enter your choice:"))
        if option==1:
            print(f"Your balnce is {balance}")
        elif option==2:
                withdraw=int(input("enter withdrawal amount:"))
                balance=balance-withdraw
                if balance>0:
                    print(f"Your Balance is {balance}")
                else:
                    print("Insufficient amount to withdraw")
        elif option==3:
            deposit=int(input("enter deposit amount"))
            balance=balance+deposit
            print(f"Your current balance is {balance}")
        elif option==4:
            print("quit")
        else:
            print("Invalid option")
    except:
       print("Invalid input,enter a number ")
    
else:
    print("Wrong password,Try again ")
    
