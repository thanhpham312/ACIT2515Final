import datetime
from models.transaction import Transaction

class Account():
    def __init__(self, id, name, balance = 0, transaction_list = []):
        self.__id = id
        self.__name = name
        self.__balance = balance
        self.__transaction_list = transaction_list

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def balance(self):
        return self.__balance

    @property
    def transaction_list(self):
        return self.__transaction_list

    @transaction_list.setter
    def transaction_list(self, list):
        self.__transaction_list = list

    def withdraw(self, withdraw_amount):
        if withdraw_amount < self.balance:
            transaction_description = "Failed to withdraw money, balance not enough."
            transaction = Transaction(self, datetime.datetime.now(), "withdrawal", self.balance, self.balance, "failed",
                                      transaction_description)
            self.__transaction_list.append(transaction)
            return False
        else:
            balance_before = self.balance
            self.__balance -= withdraw_amount
            transaction_description = "Withdrawal successful."
            transaction = Transaction(self, datetime.datetime.now(), "withdrawal", balance_before, self.balance, "success",
                                      transaction_description)
            self.__transaction_list.append(transaction)
            return True

    def __str__(self):
        return "account_id: {}\nname: {}\nbalance: {}\ntransaction_list: {}".format(self.id, self.name, self.balance, self.transaction_list)