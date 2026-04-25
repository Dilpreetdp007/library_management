balance = 1000

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input(" emtere")
    if choice == '1':
          print("Balance:", balance)
    elif choice == '2':
          amount = float(input("Enter amount: "))
          balance += amount
          print("Deposited successfully.")
    elif choice == '3':
          amount = float(input("Enter amount: "))
          if amount <= balance:
            balance -= amount
            print("Withdraw successful.")
    else:
            print("Insufficient balance!")
            elif choice == '4':
            print("Exiting...")
            break
else: print("Invalid choice!")