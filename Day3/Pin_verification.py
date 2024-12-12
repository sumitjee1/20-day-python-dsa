#ATM Pin Verification
pin = "11992288456"  
entered_pin = input("Enter your PIN: ")

if entered_pin == pin:
    print("PIN verified! Access granted.")
else:
    print("Incorrect PIN! Access denied.")