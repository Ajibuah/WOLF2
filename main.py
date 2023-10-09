# ATM PROCESS
# Assume your card is in the machine
try:
    with open("pin_user.txt", "r") as pin_file:
        pin_user = int(pin_file.read())
except FileNotFoundError:
    pin_user = None
try:
    with open("balance_user.txt", "r") as balance_file:
        balance_user = int(balance_file.read())
except FileNotFoundError:
    with open("balance_user.txt", "w") as balance_file:
        balance_file.write(str(balance_user))
while True:
    print(f"Your account balance: N{balance_user: }")
    choice = int(input("""Select your ATM transaction:
    1. Withdraw
    2. Transfer (current or savings):
    3. Buy Airtime
    4. Change Pin
    5. Quit
    6. Reset Account
    Enter the number corresponding to your choice: """))

    if choice == 1:
        pin = int(input("Please enter your PIN: "))
        if pin == pin_user:
            withdrawal_amount = float(input("Please enter the amount to withdraw: "))
            if withdrawal_amount <= balance_user:
                balance_user -= withdrawal_amount
                with open("user_balance.txt", "w") as balance_file:
                    balance_file.write(str(balance_user))
                print(f"Withdrawal Successful. Your new balance is N{balance_user:.2f}")
            else:
                print("Insufficient funds. Withdrawal failed.")
        else:
            print("Invalid PIN. Withdrawal failed.")
    elif choice == 2:
        pin = int(input("Please enter your PIN: "))
        if pin == pin_user:
            transfer_amount = len(input("Enter the amount to transfer: "))
            receiver_account_number = input("Enter receiver's account number: ")
            receiver_account_name = input("Enter receiver's account name: ")
            if transfer_amount <= balance_user:
                balance_user -= transfer_amount
                with open("user_balance.txt", "w") as balance_file:
                    balance_file.write(str(balance_user))
                print(f"Transfer Successful. Your new balance is N{balance_user:.2f}")
            else:
                print("Insufficient funds. Transfer failed.")
        else:
            print("Invalid PIN. Transfer failed.")
    elif choice == 3:
        pin = int(input("Please enter your PIN: "))
        if pin == pin_user:
            airtime_amount = float(input("Please enter the amount for airtime purchase: "))
            if airtime_amount <= balance_user:
                balance_user -= airtime_amount
                with open("user_balance.txt", "w") as balance_file:
                    balance_file.write(str(balance_user))
                print(f"Buy Airtime Successful. Your new balance is N{balance_user:.2f}")
            else:
                print("Insufficient funds. Buy Airtime failed.")
        else:
            print("Invalid PIN. Buy Airtime failed.")
    elif choice == 4:
        old_pin = int(input("Enter your old PIN: "))
        if old_pin == pin_user:
            new_pin = int(input("Enter your new PIN: "))
            user_pin = new_pin
            with open("user_pin.txt", "w") as pin_file:
                pin_file.write(str(new_pin))
            print("Change Pin Successful")
        else:
            print("Invalid old PIN. Change Pin failed.")
    elif choice == 5:
        print("Thank you for using the ATM. Goodbye!")
        break
    elif choice == 6:
        pin = int(input("Please enter your PIN: "))
        if pin == pin_user:
            with open("pin_user.txt", "w") as pin_file:
                 pin_file.write("120000")
    else:
        print("Invalid choice. Please select a valid transaction.")