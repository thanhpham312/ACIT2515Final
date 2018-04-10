import json
import datetime
from models.data.transaction import Transaction

class Fee():
    def __init__(self, account, file_name):
        self.__account = account
        self.__file_name = file_name
        self.__fee_list = {}
        self._load_from_file()

    def _load_from_file(self):
        with open(self.__file_name, 'r') as f:
            f_content = json.load(f)
            if self.__account.type in f_content:
                self.__fee_list = f_content[self.__account.type]

    def _charge_fee(self, fee_type):
        before_balance = self.__account.balance
        transaction_description = "Fee charged - " + fee_type
        if self.__fee_list[fee_type]['type'] == "set_amount":
            self.__account.balance -= self.__fee_list[fee_type]['amount']
            transaction = Transaction(self.__account, datetime.datetime.now(), "transaction fee",
                                      before_balance, self.__account.balance, "success",
                                      transaction_description)
            self.__account.transaction_list.append(transaction.to_dict())

        elif self.__fee_list[fee_type].type == "percentage":
            self.__account.balance -= self.__account.balance.self.__fee_list[fee_type]['amount']
            transaction = Transaction(self.__account, datetime.datetime.now(), "transaction fee",
                                      before_balance, self.__account.balance, "success",
                                      transaction_description)
            self.__account.transaction_list.append(transaction.to_dict())

if __name__ == '__main__':
    pass