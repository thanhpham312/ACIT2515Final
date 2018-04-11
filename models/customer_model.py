import json
from models.account import Account, ChequingAccount, SavingsAccount

class CustomerModel():
    def __init__(self, file_name, customer_id):
        self.__file_name = file_name
        self.__customer_id = customer_id
        self.__customer_name = None
        self.__customer_account_dict = {}
        self.__current_account = None

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, id):
        self.__customer_id = id

    @property
    def customer_name(self):
        return self.__customer_name

    @customer_name.setter
    def customer_name(self, name):
        self.__customer_name = name

    @property
    def customer_account_dict(self):
        return self.__customer_account_dict

    @customer_account_dict.setter
    def customer_account_dict(self, account_dict):
        self.__customer_account_dict = account_dict

    @property
    def current_account(self):
        return self.__current_account

    @current_account.setter
    def current_account(self, account):
        self.__customer_account_dict = account

    def _load_from_file(self):
        with open(self.__file_name, 'r') as f:
            return json.load(f)

    def _save_to_file(self, data):
        with open(self.__file_name, 'w') as f:
            json.dump(data, f, indent=2)

    def _load_customer(self):
        customers_dict = self._load_from_file()
        if self.customer_id in customers_dict:
            self.customer_name = customers_dict[self.customer_id]['name']
            self.customer_account_dict = customers_dict[self.customer_id['accounts']]


    def _set_current_account(self, account_type):
        if len(self.customer_account_dict) != 0:
            if account_type in self.customer_account_dict:
                if account_type == 'chequing':
                    self.current_account = ChequingAccount(account_type,
                                                           self.customer_account_dict[account_type]['balance'],
                                                           self.customer_account_dict[account_type]['transactions'])
                elif account_type == 'savings':
                    self.current_account = SavingsAccount(account_type,
                                                          self.customer_account_dict[account_type]['balance'],
                                                          self.customer_account_dict[account_type]['transactions'])


if __name__ == '__main__':
    pass

