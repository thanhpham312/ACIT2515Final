import json
from models.account_model import AccountModel
from models.data.account import ChequingAccount, SavingAccount

class AccountModelForClient(AccountModel):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.__current_account = None

    @property
    def current_account(self):
        return self.__current_account

    def _set_current_account(self, user_id):
        account_id = "0"
        for id, account_object in self.account_list["account_list"].items():
            if account_object['user_id'] == user_id:
                account_id = str(id)
                break
        if account_id != "0" and account_id in self.account_list["account_list"]:
            print('sadffg')
            current_account = self.account_list["account_list"][account_id]
            if current_account['type'] == 'chequing':
                self.__current_account = ChequingAccount(account_id, current_account['name'], current_account['type'], current_account['balance'],
                                                       current_account['transaction_list'])
                print(self.current_account)
            elif current_account['type'] == 'saving':
                self.__current_account = SavingAccount(account_id, current_account['name'], current_account['type'], current_account['balance'],
                                                       current_account['transaction_list'])

    def _update_current_account(self):
        self.account_list["account_list"][str(self.__current_account.id)] = {
            "user_id": self.__current_account.id,
            "name": self.__current_account.name,
            "type": self.__current_account.type,
            "balance": self.__current_account.balance,
            "transaction_list": self.__current_account.transaction_list
        }
        self._save_to_file()

if __name__ == '__main__':
    account_model = AccountModelForClient('data/accounts.json')
    account_model._load_from_file()
    account_model._set_current_account(1)
    account_model.current_account.withdraw(500)
    account_model._update_current_account()