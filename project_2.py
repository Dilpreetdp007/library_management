balance = 0.0
history = []

while True:
    print("\n1. Balance | 2. Withdraw | 3. Deposit | 4. Statement | 5. Exit")
    choice = input("Select an option (1-5): ")

    if choice == '1':
        print(f"Current Balance: ${balance}")
        
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            history.append(f"Withdrew: ${amount}")
            print("Withdrawal successful.")
        else:
            print("Insufficient funds!")
            
    elif choice == '3':
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        history.append(f"Deposited: ${amount}")
        print("Deposit successful.")
        
    elif choice == '4':
        print("\n--- Transaction Statement ---")
        for record in history:
            print(record)
        if not history:
            print("No transactions yet.")
            
    elif choice == '5':
        print("Exiting ATM. Have a good day!")
        break
        
    else:
        print("Invalid choice.")


