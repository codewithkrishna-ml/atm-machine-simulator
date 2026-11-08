#PROJECT-Atm Machine Simulator
class ATM:
    def __init__(self):
        self.balance = 0
        self.pin = "1234"
        self.menu()

    def menu(self):
        while True:
            print("\n--------ATM machine simulator----------")
            print("choose options: 1.check balance | 2.Deposit | 3.Withdraw | 4.change pin | 5.Exit")
            choice = input("Choose option (1-5): ")
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.change_pin()
            elif choice == "5":
                print("Exit! Thank you for using ATM")
                break
            else:
                print("Invalid option! please try again")

    def check_balance(self):
        userpin = input("Enter your pin: ")
        if userpin == self.pin:
            print(f"Current Balance: {self.balance}")
        else:
            print("Wrong Pin! Access Denied")

    def deposit(self):
        amount = int(input("How much money needs to be deposited: "))
        if amount > 0:
            self.balance += amount
            print(f"{amount} Deposit successfully! New balance: {self.balance}")
        else:
            print("Invalid Amount!")

    def withdraw(self):
        userpin = input("Enter your PIN: ")
        if userpin == self.pin:
            amount = int(input("How much money needs to be withdrawn: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} withdraw successfully! Sufficient Balance")
                print(f"Remaining Balance: {self.balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Wrong PIN! Access Denied.")
        
    def change_pin(self):
        userpin = input("Enter your current pin: ")
        if userpin != self.pin:
            print("Wrong current pin! No pin change")
            return
        new_pin = input("Enter your new pin: ")
        self.pin = new_pin
        print("PIN changed successfully!")

if __name__ == "__main__":
    my_atm = ATM()