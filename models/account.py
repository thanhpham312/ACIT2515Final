import datetime
from models.transaction import Transaction
from models.fee import Fee

class Account():
    '''
    Account model, that asks for account type, balance and list of transactions
    It has its functions to manage account.
    '''
    def __init__(self, type="normal", balance=0, transaction_list=[]):
        self.__type = type
        self.__balance = balance
        self.__transaction_list = transaction_list

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

    def deposit(self, deposit_amount):
        '''
        Deposing money on the account, writes to a json file for specific user. Checks for type validations.
        :param deposit_amount: Amount to deposit
        :return:None
        '''
        try:
            deposit_amount = float(deposit_amount)
            if deposit_amount < 0:
                transaction_description = "Deposit failed - Amount incorrect."
                transaction = Transaction(self, datetime.datetime.now(), "deposit", self.balance, self.balance,
                                          "failed",
                                          transaction_description)
                self.transaction_list.append(transaction._to_dict())
                return False
        except ValueError:
            return False

        balance_before = self.balance
        self.balance += deposit_amount
        transaction_description = "Deposit succeeded."
        transaction = Transaction(self, datetime.datetime.now(), "deposit", balance_before, self.balance,
                                  "succeeded",
                                  transaction_description)
        self.transaction_list.append(transaction._to_dict())
        return True


    def withdraw(self, withdraw_amount):
        '''
        withdraw money from the account, writes to a json file for specific user. Checks for type validations.
        :param withdraw_amount: amount to withdraw from account
        :return:None
        '''
        try:
            withdraw_amount = float(withdraw_amount)
            if withdraw_amount < 0:
                transaction_description = "Withdrawal failed - Amount incorrect."
                transaction = Transaction(self, datetime.datetime.now(), "withdrawal", self.balance, self.balance,
                                          "failed",
                                          transaction_description)
                self.transaction_list.append(transaction._to_dict())
                return False
        except ValueError:
            return False

        if withdraw_amount < self.balance:
            transaction_description = "Withdrawal failed - Balance not enough."
            transaction = Transaction(self, datetime.datetime.now(), "withdrawal", self.balance, self.balance, "failed",
                                      transaction_description)
            self.transaction_list.append(transaction._to_dict())
            return False
        else:
            balance_before = self.balance
            self.balance -= withdraw_amount
            transaction_description = "Withdrawal succeeded."
            transaction = Transaction(self, datetime.datetime.now(), "withdrawal", balance_before, self.balance, "succeeded",
                                      transaction_description)
            self.transaction_list.append(transaction._to_dict())
            return True


    def _to_dict(self):
        return {
            "balance": self.balance,
            "transactions": self.transaction_list
        }

    def __str__(self):
        return "type: {}\nbalance: {}\ntransaction_list: {}".format(self.type, self.balance, self.transaction_list)

class ChequingAccount(Account):
    '''
    Chequing account and its functions. Child of Account type. It is different with its fees.
    Has minimun negative limit $500.
    '''
    def __init__(self, type="chequing", balance=0, transaction_list=[]):
        super().__init__(type, balance, transaction_list)
        self.__overdraft = -500.0
        self.__fees = Fee(self)

    @property
    def fees(self):
        return self.__fees

    def withdraw(self, withdraw_amount):
        '''
                withdraw money from the account, writes to a json file for specific user. Checks for type validations.
                :param withdraw_amount: amount to withdraw from account
                :return:None
                '''
        try:
            withdraw_amount = float(withdraw_amount)
            if withdraw_amount < 0:
                transaction_description = "Withdrawal failed - Amount incorrect."
                transaction = Transaction(self, datetime.datetime.now(), "withdrawal", self.balance, self.balance,
                                          "failed",
                                          transaction_description)
                self.transaction_list.append(transaction._to_dict())
                return False
        except ValueError:
            return False

        if self.balance - withdraw_amount - self.fees._get_fee("withdraw_fee") > 0:
            balance_before = self.balance
            self.balance -= withdraw_amount
            transaction_description = "Withdrawal succeeded."
            transaction = Transaction(self, datetime.datetime.now(), "withdrawal", balance_before, self.balance,
                                      "succeeded",
                                      transaction_description)
            self.transaction_list.append(transaction._to_dict())

            self.fees._charge_fee("withdraw_fee")
            return True
        elif self.balance - withdraw_amount - self.fees._get_fee("overdraft_fee") < 0 and self.balance - withdraw_amount - self.fees._get_fee("overdraft_fee") > self.__overdraft\
                or self.balance - withdraw_amount - self.fees._get_fee("withdraw_fee")  and self.balance - withdraw_amount - self.fees._get_fee("withdraw_fee") > self.__overdraft < 0:
            balance_before = self.balance
            self.balance -= withdraw_amount
            transaction_description = "Withdrawal succeeded."
            transaction = Transaction(self, datetime.datetime.now(), "withdrawal", balance_before, self.balance, "success",
                                      transaction_description)
            self.transaction_list.append(transaction._to_dict())

            self.fees._charge_fee("overdraft_fee")
            return True
        else:
            transaction_description = "Withdrawal failed - Balance not enough."
            transaction = Transaction(self, datetime.datetime.now(), "withdrawal", self.balance, self.balance,
                                      "failed",
                                      transaction_description)
            self.transaction_list.append(transaction._to_dict())
            return False

class SavingsAccount(Account):
    '''
    Saving account does not have negative limit
    '''
    def __init__(self, type="savings", balance=0, transaction_list=[]):
        super().__init__(type, balance, transaction_list)
        self.__fees = Fee(self)

    @property
    def fees(self):
        return self.__fees

    def withdraw(self, withdraw_amount):
        '''
                withdraw money from the account, writes to a json file for specific user. Checks for type validations.
                :param withdraw_amount: amount to withdraw from account
                :return:None
                '''
        try:
            withdraw_amount = float(withdraw_amount)
            if withdraw_amount < 0:
                transaction_description = "Withdrawal failed - Amount incorrect."
                transaction = Transaction(self, datetime.datetime.now(), "withdrawal", self.balance, self.balance,
                                          "failed",
                                          transaction_description)
                self.transaction_list.append(transaction._to_dict())
                return False
        except ValueError:
            return False

        if self.balance - withdraw_amount - self.fees._get_fee("withdraw_fee") > 0:
            balance_before = self.balance
            self.balance -= withdraw_amount
            transaction_description = "Withdrawal successful."
            transaction = Transaction(self, datetime.datetime.now(), "withdrawal", balance_before, self.balance,
                                      "succeeded",
                                      transaction_description)
            self.transaction_list.append(transaction._to_dict())

            self.fees._charge_fee("withdraw_fee")
            return True
        else:
            transaction_description = "Withdrawal failed - Balance not enough."
            transaction = Transaction(self, datetime.datetime.now(), "withdrawal", self.balance, self.balance,
                                      "failed",
                                      transaction_description)
            self.transaction_list.append(transaction._to_dict())
            return False
