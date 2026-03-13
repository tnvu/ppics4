# Write a program that simulates an automatic teller machine (ATM). Since
# you probably don’t have access to a card reader, have the initial screen ask
# for user ID and a PIN. The user ID will be used to look up the information
# for the user’s accounts (including the PIN to see whether it matches what
# the user types). Each user will have access to a checking account and a
# savings account. The user should able to check balances, withdraw cash,
# and transfer money between accounts. Design your interface to be similar
# to what you see on your local ATM. The user account information should
# be stored in a file when the program terminates. This file is read in again
# when the program restarts.

import hashlib
import pickle

ADMIN_ID = "admin"
ADMIN_PIN = '8c505a11e953f6a400a904e86ca074b1'

class User:
    def __init__(self, userid, pin):
        self.userid = userid
        self.pin = pin
        self.checking = 0.00
        self.savings = 0.00

class TextInterface:
    def __init__(self):
        pass

    def setResult(self, success, msg):
        if success:
            print(msg)
        else:
            print(f"ERROR: {msg}")

    def promptLogin(self):
        userid = input("UserID: ").strip()
        pin = input("PIN: ")
        return userid, pin
    
    def promptAdminTxn(self):
        txn = input("""\
Transaction choices:
    (A)dd a user
    (D)elete a user
    (S)hutdown
    (Q)uit
Which transaction? """)
        if txn[0] in ['a', 'A']:
            return "ADD_USER"
        elif txn[0] in ['d', 'D']:
            return "DELETE_USER"
        elif txn[0] in ['s', 'S']:
            return "SHUTDOWN"
        elif txn[0] in ['q', 'Q']:
            return "QUIT"
        else:
            print(f"Try again: Invalid transaction choice: {txn}")

    def promptAddUser(self):
        userid, pin = self.promptLogin()
        return userid, pin
    
    def promptDeleteUser(self):
        userid = input("UserID: ").strip()
        return userid
    
    def promptUserTxn(self):
        while True:
            ans = input("""\
Transactions choices:
    (C)heck balances
    (D)eposit
    (W)ithdraw cash
    (T)ransfer money between accounts
    (Q)uit
Which transaction? """).strip()
            if len(ans) == 0:
                print("Try again")
            elif ans[0] in ['c', 'C']:
                return "CHECK_BALANCES"
            elif ans[0] in ['d', 'D']:
                return "DEPOSIT"
            elif ans[0] in ['w', 'W']:
                return 'WITHDRAW_CASH'
            elif ans[0] in ['t', 'T']:
                return "TRANSFER_MONEY"
            elif ans[0] in ['q', 'Q']:
                return "QUIT"
            else:
                print("Try again")

    def promptAccount(self, label):
        while True:
            ans = input(f"""\
{label} account selection:
    (C)hecking
    (S)avings
Which account? """).strip()
            if len(ans) == 0:
                print("Try again")
            elif ans[0] in ['c', 'C']:
                return "CHECKING"
            elif ans[0] in ['s', 'S']:
                return "SAVINGS"
            else:
                print("Try again")
    
    def promptAmount(self, action):
        while True:
            amt = input(f"""How much to {action}? """).strip()
            if amt[0] == "$":
                amt = amt[1:]
            try:
                amt = float(amt)
                if amt <= 0.00:
                    print("Try again")
                else:
                    return amt
            except ValueError:
                print("Try again")

    def checkBalance(self, checking, savings):
        print(f"Checking: ${checking:0.2f}, Savings: ${savings:0.2f}")

    def promptDeposit(self):
        dst = self.promptAccount("Deposit")
        amt = self.promptAmount("deposit")
        return dst, amt

    def promptWithdrawCash(self):
        src = self.promptAccount("Withdraw")
        amt = self.promptAmount("withdraw")
        return src, amt
    
    def promptTransferMoney(self):
        src = self.promptAccount("Transfer from")
        amt = self.promptAmount("transfer")
        return src, amt

class ATMApp:
    def __init__(self, interface):
        self.interface = interface
        # Load user accounts
        try:
            with open('atm.db', 'rb') as infile:
                self.users = pickle.load(infile)
        except FileNotFoundError:
            self.users = []
        # Make sure no one is logged in
        self.logout()
        self.running = True

    def flush(self):
        with open('atm.db', 'wb') as outfile:
            pickle.dump(self.users, outfile)

    def run(self):
        while self.running:
            # Login
            userid, pin = self.interface.promptLogin()
            sessionType = self.login(userid, pin)
            # Start session
            if sessionType == "ADMIN":
                self.adminSession()
            elif sessionType == "USER":
                self.userSession()
            elif sessionType == "NONE":
                self.interface.setResult(False, "Invalid userid/pin")
            # Logout
            self.logout()
    
    def login(self, userid, pin):
        if self.adminLogin(userid, pin):
            return "ADMIN" 
        for user in self.users:
            if userid == user.userid and pin == user.pin:
                self.user = user
                return "USER"
        return "NONE"

    def logout(self):
        self.user = None

    def adminLogin(self, userid, pin):
        if userid == ADMIN_ID and \
            hashlib.md5(pin.encode('utf-8')).hexdigest() == ADMIN_PIN:
            return True
        return False

    def adminSession(self):
        while True:
            txn = self.interface.promptAdminTxn()
            if txn == "ADD_USER":
                userid, pin = self.interface.promptAddUser()
                self.addUser(userid, pin)
            elif txn == "DELETE_USER":
                userid = self.interface.promptDeleteUser()
                self.deleteUser(userid)
            elif txn == "SHUTDOWN":
                self.shutdown()
                break
            elif txn == "QUIT":
                break

    def addUser(self, userid, pin):
        if userid == "" or userid == ADMIN_ID:
            self.interface.setResult(False, f"Invalid userid: {userid}")
            return
        for user in self.users:
            if userid == user.userid:
                self.interface.setResult(False, f"User already exists: {userid}")
                return
        user = User(userid, pin)
        self.users.append(user)
        self.flush()

    def deleteUser(self, userid):
        userFound = False
        for user in self.users[:]:
            if user.userid == userid:
                self.users.remove(user)
                self.flush()
                userFound = True
        if not userFound:
            self.interface.setResult(False, f"User not found: {userid}")

    def shutdown(self):
        self.running = False

    def userSession(self):
        while True:
            txn = self.interface.promptUserTxn()
            if txn == "CHECK_BALANCES":
                checkings, savings = self.checkBalances()
                self.interface.checkBalance(checkings, savings)
            elif txn == "DEPOSIT":
                dst, amt = self.interface.promptDeposit()
                self.deposit(dst, amt)
            elif txn == "WITHDRAW_CASH":
                src, amt = self.interface.promptWithdrawCash()
                self.withdrawCash(src, amt)
            elif txn == "TRANSFER_MONEY":
                src, amt = self.interface.promptTransferMoney()
                self.transferMoney(src, amt)
            elif txn == "QUIT":
                break
            else:
                self.interface.setResult(False, f"Unknown transaction: {txn}")
    
    def checkBalances(self):
        return (self.user.checking, self.user.savings)
    
    def deposit(self, dst, amt):
        if amt <= 0:
            self.interface.setResult(False, f"Amount <= 0: ${amt:0.2f}")
            return
        if dst == "CHECKING":
            self.user.checking = self.user.checking + amt
        elif dst == "SAVINGS":
            self.user.savings = self.user.savings + amt
        else:
            self.interface.setResult(False, f"Unknown account: {dst}")
            return
        self.flush()
        self.interface.setResult(True, f"Deposit ${amt:0.2f} in to {dst}")
    
    def withdrawCash(self, src, amt):
        if amt <= 0:
            self.interface.setResult(False, f"Amount <= 0: ${amt:0.2f}")
            return
        if src == "CHECKING":
            if amt > self.user.checking:
                self.interface.setResult(
                    False, f"Amount (${amt:0.2f}) exceeds checking (${self.user.checking:0.2f})")
                return
            self.user.checking = self.user.checking - amt
            self.flush()
            self.interface.setResult(True, f"Withdrew ${amt:0.2f} from {src}")
            return
        if src == "SAVINGS":
            if amt > self.user.savings:
                self.interface.setResult(
                    False, f"Amount (${amt:0.2f}) exceeds savings (${self.user.savings:0.2f})")
                return
            self.user.savings = self.user.savings - amt
            self.flush()
            self.interface.setResult(True, f"Withdrew ${amt:0.2f} from {src}")
            return
        self.interface.setResult(False, f"Unknown account: {src}")
        return
    
    def transferMoney(self, src, amt):
        if amt <= 0:
            self.interface.setResult(False, f"Amount is <= 0: ${amt:0.2f}")
            return
        if src == "CHECKING":
            if amt > self.user.checking:
                self.interface.setResult(
                    False, f"Amount (${amt:0.2f}) exceeds checking (${self.user.checking:0.2f})")
                return
            self.user.checking = self.user.checking - amt
            self.user.savings = self.user.savings + amt
            self.flush()
            self.interface.setResult(True, f"Tranferred from CHECKING to SAVINGS: ${amt:0.2f}")
            return
        elif src == "SAVINGS":
            if amt > self.user.savings:
                self.interface.setResult(
                    False, f"Amount (${amt:0.2f}) exceeds savings (${self.user.savings:0.2f})")
                return
            self.user.savings = self.user.savings - amt
            self.user.checking = self.user.checking + amt
            self.flush()
            self.interface.setResult(True, f"Tranferred from SAVINGS to CHECKING: ${amt:0.2f}")
            return

def main():
    interface = TextInterface()
    app = ATMApp(interface)
    app.run()

main()