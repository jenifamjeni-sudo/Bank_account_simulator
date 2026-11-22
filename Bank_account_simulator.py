balance = 1000
history = []

def check_balance():
    print("Current balance:", balance)

def deposit():
    global balance
    amount = int(input("Enter deposit amount: "))
    if amount > 0:
        balance += amount
        history.append("Deposited: " + str(amount))
        print("Money deposited successfully!")
    else:
        print("Invalid amount")

def withdraw():
    global balance
    amount = int(input("Enter withdrawal amount: "))
    if amount > 0 and amount <= balance:
        balance -= amount
        history.append("Withdrawn: " + str(amount))
        print("Money withdrawn successfully!")
    else:
        print("Insufficient balance or invalid amount")

def transaction_history():
    print("\nTransaction History:")
    for item in history:
        print(item)

while True:
    print("\n--- Bank Account Simulator ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        transaction_history()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
