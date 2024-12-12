#ATM-Menu-System
print("Menu:")
print("1. View Account")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Viewing account...")
elif choice == 2:
    print("Depositing money...")
elif choice == 3:
    print("Withdrawing money...")
elif choice == 4:
    print("Exiting the system. Goodbye!")
else:
    print("Invalid choice. Please select a number between 1 and 4.")
