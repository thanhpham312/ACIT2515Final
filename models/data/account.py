import datetime
from models.data.transaction import Transaction
from models.data.fee import Fee

class Account():
    def __init__(self, id, name, type="normal", balance=0, transaction_list=[]):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__balance = balance
        self.__transaction_list = transaction_list
        self.__fees = Fee(self, 'data/fees.json')

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__type

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.__balance = amount

    @property
    def transaction_list(self):
        return self.__transaction_list

    @transaction_list.setter
    def transaction_list(self, list):
        self.__transaction_list = list

    @property
    def fees(self):
        return self.__fees

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            balance_before = self.balance
            self.balance += deposit_amount
            transaction_description = "Deposit successful."
            transaction = Transaction(self, datetime.datetime.now(), "deposit", balance_before, self.balance,
                                      "success",
                                      transaction_description)
            self.transaction_list.append(transaction.to_dict())
            return True
        else:
            transaction_description = "Deposit failed. Amount incorrect"
            transaction = Transaction(self, datetime.datetime.now(), "deposit", self.balance, self.balance,
                                      "failed",
                                      transaction_description)
            self.transaction_list.append(transaction.to_dict())
            return False


    def withdraw(self, withdraw_amount):
        if withdraw_amount > 0:
            if withdraw_amount < self.balance:
                transaction_description = "Failed to withdraw money, balance not enough."
                transaction = Transaction(self, datetime.datetime.now(), "withdrawal", self.balance, self.balance, "failed",
                                          transaction_description)
                self.transaction_list.append(transaction.to_dict())
                return False
            else:
                balance_before = self.balance
                self.balance -= withdraw_amount
                transaction_description = "Withdrawal successful."
                transaction = Transaction(self, datetime.datetime.now(), "withdrawal", balance_before, self.balance, "success",
                                          transaction_description)
                self.transaction_list.append(transaction.to_dict())
                return True
        else:
            transaction_description = "Withdrawal failed. Amount incorrect"
            transaction = Transaction(self, datetime.datetime.now(), "withdrawal", self.balance, self.balance,
                                      "failed",
                                      transaction_description)
            self.transaction_list.append(transaction.to_dict())
            return False

    def __str__(self):
        return "account_id: {}\nname: {}\ntype: {}\nbalance: {}\ntransaction_list: {}".format(self.id, self.name, self.type, self.balance, self.transaction_list)

class ChequingAccount(Account):
    def __init__(self, id, name, type="chequing", balance=0, transaction_list=[]):
        super().__init__(id, name, type, balance, transaction_list)
        self.__overdraft = -500.0

    def withdraw(self, withdraw_amount):
        if withdraw_amount > 0:
            if self.balance - withdraw_amount < self.__overdraft:
                transaction_description = "Failed to withdraw money, balance not enough."
                transaction = Transaction(self, datetime.datetime.now(), "withdrawal", self.balance, self.balance, "failed",
                                          transaction_description)
                self.transaction_list.append(transaction.to_dict())
                return False
            elif withdraw_amount > self.balance + self.__overdraft:
                balance_before = self.balance
                self.balance -= withdraw_amount
                transaction_description = "Withdrawal successful."
                transaction = Transaction(self, datetime.datetime.now(), "withdrawal", balance_before, self.balance, "success",
                                          transaction_description)
                self.transaction_list.append(transaction.to_dict())

                self.fees._charge_fee("overdraft_fee")
                return True
            else:
                balance_before = self.balance
                self.balance -= withdraw_amount
                transaction_description = "Withdrawal successful."
                transaction = Transaction(self, datetime.datetime.now(), "withdrawal", balance_before, self.balance, "success",
                                          transaction_description)
                self.transaction_list.append(transaction.to_dict())

                self.fees._charge_fee("withdraw_fee")
                return True
        else:
            transaction_description = "Withdrawal failed. Amount incorrect"
            transaction = Transaction(self, datetime.datetime.now(), "withdrawal", self.balance, self.balance,
                                      "failed",
                                      transaction_description)
            self.transaction_list.append(transaction.to_dict())
            return False

class SavingAccount(Account):
    def __init__(self, id, name, type="saving", balance=0, transaction_list=[]):
        super().__init__(id, name, type, balance, transaction_list)

    def withdraw(self, withdraw_amount):
        if withdraw_amount > 0:
            if withdraw_amount < self.balance:
                transaction_description = "Failed to withdraw money, balance not enough."
                transaction = Transaction(self, datetime.datetime.now(), "withdrawal", self.balance, self.balance, "failed",
                                          transaction_description)
                self.__transaction_list.append(transaction.to_dict())
                return False
            else:
                balance_before = self.balance
                self.balance -= withdraw_amount
                transaction_description = "Withdrawal successful."
                transaction = Transaction(self, datetime.datetime.now(), "withdrawal", balance_before, self.balance, "success",
                                          transaction_description)
                self.__transaction_list.append(transaction.to_dict())

                self.fees._charge_fee("withdraw_fee")
                return True
        else:
            transaction_description = "Withdrawal failed. Amount incorrect"
            transaction = Transaction(self, datetime.datetime.now(), "withdrawal", self.balance, self.balance,
                                      "failed",
                                      transaction_description)
            self.__transaction_list.append(transaction.to_dict())
            return False