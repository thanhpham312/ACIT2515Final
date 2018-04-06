import json
from models.account import Account

class AccountModel():
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__account_list = []
        self.__current_account = None

    def _load_from_file(self):
        with open(self.__file_name, 'r') as f:
            self.__account_list = json.load(f)['account_list']

    def _save_to_file(self):
        with open(self.__file_name, 'w') as f:
            json.dump(self.__account_list, f)

    @property
    def current_account(self):
        return self.__current_account

    def _set_current_account(self, account_id):
        for account in self.__account_list: 
            if account_id == account['account_id']:
                self.__current_account = Account(account['account_id'], account['name'], account['balance'], account['transaction_list'])
                break

if __name__ == '__main__':
    account_model = AccountModel('data/account.json')
    account_model._load_from_file()
    account_model._set_current_account(1)
    print(account_model.current_account)



