import tkinter as tk
from tkinter import messagebox, simpledialog

class Account:
    def __init__(self, acc_no, pin, balance=0):
        self.acc_no = acc_no
        self.pin = pin
        self.balance = balance
        self.transactions = []
        self.locked = False
        self.attempts = 0

    def deposit(self, amount):
        if amount <= 0:
            return False, "Please enter a valid amount."
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}")
        return True, "Transaction Successful."

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Please enter a valid amount."
        if amount > self.balance:
            return False, "Insufficient Balance."
        self.balance -= amount
        self.transactions.append(f"Withdrawn ₹{amount}")
        return True, "Transaction Successful."

    def change_pin(self, old_pin, new_pin):
        if old_pin != self.pin:
            return False, "Incorrect old PIN."
        self.pin = new_pin
        return True, "PIN changed successfully."


class ATMSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Simulator")
        self.root.geometry("400x400")

        # Multiple accounts
        self.accounts = {
            "101": Account("101", "1234", 5000),
            "102": Account("102", "5678", 8000)
        }

        self.current_account = None

        self.login_screen()

    # ---------------- LOGIN ----------------
    def login_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Welcome to ATM", font=("Arial", 18, "bold")).pack(pady=20)

        tk.Label(self.root, text="Account Number").pack()
        self.acc_entry = tk.Entry(self.root)
        self.acc_entry.pack()

        tk.Label(self.root, text="PIN").pack()
        self.pin_entry = tk.Entry(self.root, show="*")
        self.pin_entry.pack()

        tk.Button(self.root, text="Login", command=self.authenticate).pack(pady=10)

    def authenticate(self):
        acc_no = self.acc_entry.get()
        pin = self.pin_entry.get()

        account = self.accounts.get(acc_no)

        if not account:
            messagebox.showerror("Error", "Account not found.")
            return

        if account.locked:
            messagebox.showerror("Locked", "Account is locked due to multiple failed attempts.")
            return

        if pin == account.pin:
            account.attempts = 0
            self.current_account = account
            self.menu_screen()
        else:
            account.attempts += 1
            remaining = 3 - account.attempts
            if remaining == 0:
                account.locked = True
                messagebox.showerror("Locked", "Account locked after 3 failed attempts.")
            else:
                messagebox.showerror("Error", f"Incorrect PIN. {remaining} attempts left.")

    # ---------------- MENU ----------------
    def menu_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="ATM Menu", font=("Arial", 16, "bold")).pack(pady=20)

        tk.Button(self.root, text="Check Balance", width=20, command=self.check_balance).pack(pady=5)
        tk.Button(self.root, text="Deposit Money", width=20, command=self.deposit_money).pack(pady=5)
        tk.Button(self.root, text="Withdraw Money", width=20, command=self.withdraw_money).pack(pady=5)
        tk.Button(self.root, text="Transaction History", width=20, command=self.show_transactions).pack(pady=5)
        tk.Button(self.root, text="Change PIN", width=20, command=self.change_pin).pack(pady=5)
        tk.Button(self.root, text="Logout", width=20, command=self.login_screen).pack(pady=20)

    # ---------------- FUNCTIONS ----------------
    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is ₹{self.current_account.balance}")

    def deposit_money(self):
        try:
            amount = simpledialog.askinteger("Deposit", "Enter amount:")
            if amount is None:
                return
            success, msg = self.current_account.deposit(amount)
            if success:
                self.show_receipt("Deposit", amount)
            messagebox.showinfo("Info", msg)
        except:
            messagebox.showerror("Error", "Invalid input.")

    def withdraw_money(self):
        try:
            amount = simpledialog.askinteger("Withdraw", "Enter amount:")
            if amount is None:
                return
            success, msg = self.current_account.withdraw(amount)
            if success:
                self.show_receipt("Withdrawal", amount)
            messagebox.showinfo("Info", msg)
        except:
            messagebox.showerror("Error", "Invalid input.")

    def show_transactions(self):
        txns = self.current_account.transactions
        if not txns:
            messagebox.showinfo("Transactions", "No transactions yet.")
        else:
            messagebox.showinfo("Transactions", "\n".join(txns))

    def change_pin(self):
        old_pin = simpledialog.askstring("Change PIN", "Enter old PIN:", show="*")
        if old_pin is None:
            return
        new_pin = simpledialog.askstring("Change PIN", "Enter new PIN:", show="*")
        if new_pin is None:
            return

        success, msg = self.current_account.change_pin(old_pin, new_pin)
        messagebox.showinfo("Info", msg)

    def show_receipt(self, txn_type, amount):
        receipt = f"""
-------- RECEIPT --------
Account: {self.current_account.acc_no}
Transaction: {txn_type}
Amount: ₹{amount}
Remaining Balance: ₹{self.current_account.balance}
-------------------------
Thank you for banking with us!
"""
        messagebox.showinfo("Receipt", receipt)

    # ---------------- UTILITY ----------------
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ATMSimulator(root)
    root.mainloop()
