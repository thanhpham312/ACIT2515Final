import json
import datetime
from models.transaction import Transaction

class Fee():
    '''
    Class model for different fees
    '''
    def __init__(self, account, file_name = './models/data/fees.json'):
        self.__account = account
        self.__file_name = file_name
        self.__fee_list = {}
        self._load_from_file()

    def _load_from_file(self):
        with open(self.__file_name, 'r') as f:
            f_content = json.load(f)
            if self.__account.type in f_content:
                self.__fee_list = f_content[self.__account.type]

    def _get_fee(self, fee_type):
        if self.__fee_list[fee_type]['type'] == "set_amount":
            return self.__fee_list[fee_type]['amount']
        elif self.__fee_list[fee_type]['type'] == "percentage":
            return abs(self.__account.balance*self.__fee_list[fee_type]['amount'])

    def _charge_fee(self, fee_type):
        '''
        Charges fees from the current account of the current user.
        :param fee_type: Amount of fees to charge
        :return:
        '''
        before_balance = self.__account.balance
        transaction_description = "Fee charged - " + fee_type + '.'
        if self.__fee_list[fee_type]['type'] == "set_amount":
            self.__account.balance -= self.__fee_list[fee_type]['amount']
            transaction = Transaction(self.__account, datetime.datetime.now(), "transaction fee",
                                      before_balance, self.__account.balance, "success",
                                      transaction_description)
            self.__account.transaction_list.append(transaction._to_dict())

        elif self.__fee_list[fee_type]['type'] == "percentage":
            self.__account.balance -= abs(self.__account.balance*self.__fee_list[fee_type]['amount'])
            transaction = Transaction(self.__account, datetime.datetime.now(), "transaction fee",
                                      before_balance, self.__account.balance, "success",
                                      transaction_description)
            self.__account.transaction_list.append(transaction._to_dict())

if __name__ == '__main__':
    pass