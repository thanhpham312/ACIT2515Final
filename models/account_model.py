import json
from models.data.account import Account, ChequingAccount, SavingAccount

class AccountModel():
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__account_list = {}
        self.__current_account = None

    def _load_from_file(self):
        with open(self.__file_name, 'r') as f:
            self.__account_list = json.load(f)

    def _save_to_file(self):
        with open(self.__file_name, 'w') as f:
            print(self.__account_list)
            json.dump(self.__account_list, f, indent=4)

    @property
    def current_account(self):
        return self.__current_account

    def _set_current_account(self, account_id):
        account_id = str(account_id)
        if account_id in self.__account_list["account_list"]:
            current_account = self.__account_list["account_list"][account_id]
            if current_account['type'] == 'chequing':
                self.__current_account = ChequingAccount(account_id, current_account['name'], current_account['type'], current_account['balance'],
                                                       current_account['transaction_list'])
                print(self.current_account)
            elif current_account['type'] == 'saving':
                self.__current_account = SavingAccount(account_id, current_account['name'], current_account['type'], current_account['balance'],
                                                       current_account['transaction_list'])

    def _update_current_account(self):
        self.__account_list["account_list"][str(self.__current_account.id)] = {
            "user_id": self.__current_account.id,
            "name": self.__current_account.name,
            "type": self.__current_account.type,
            "balance": self.__current_account.balance,
            "transaction_list": self.__current_account.transaction_list
        }
        self._save_to_file()


if __name__ == '__main__':
    account_model = AccountModel('data/accounts.json')
    account_model._load_from_file()
    account_model._set_current_account(1)
    account_model.current_account.withdraw(500)
    account_model._update_current_account()


