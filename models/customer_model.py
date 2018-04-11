import json
from models.account import ChequingAccount, SavingsAccount

class CustomerModel():
    def __init__(self, file_name, card_number, pin):
        self.__card_number = card_number
        self.__pin = pin
        self.__file_name = file_name
        self.__customer_id = None
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
        self.__current_account = account

    def _load_from_file(self):
        with open(self.__file_name, 'r') as f:
            return json.load(f)

    def _save_to_file(self):
        customer_dict = {}
        self.customer_account_dict[self.current_account.type] = self.current_account._to_dict()
        with open(self.__file_name, 'r') as f:
            customer_dict = json.load(f)
        with open(self.__file_name, 'w') as f:
            customer_dict[self.customer_id]['accounts'] = self.customer_account_dict
            json.dump(customer_dict, f, indent=2)

    def _load_customer(self):
        customers_dict = self._load_from_file()
        print(customers_dict.values())
        for customer_id, customer_object in customers_dict.items():
            print(customer_object)
            if self.__card_number == customer_object['card_number'] and self.__pin == customer_object['pin']:
                self.customer_id = customer_id
        if self.customer_id in customers_dict:
            self.customer_name = customers_dict[self.customer_id]['name']
            self.customer_account_dict = customers_dict[self.customer_id]['accounts']


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
    new_customer_model = CustomerModel('data/accounts.json', "1")
    new_customer_model._load_customer()
    new_customer_model._set_current_account('chequing')
    print(new_customer_model.current_account)
    new_customer_model.current_account.withdraw(500)
    new_customer_model._save_to_file()



