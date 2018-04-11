from models.account_model import AccountModel
from models.account import ChequingAccount, SavingsAccount
from models.customer_model import CustomerModel

class CustomerModelForClient(CustomerModel):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.__current_account = None

    def _set_current_account(self, account_type):
        customer_list = self._load_from_file()
        if account_type in self.


        # for id, account_object in self.account_list["account_list"].items():
        #     if account_object['user_id'] == user_id:
        #         current_user_account_list[account_object['type']] = {
        #             "account_id": id,
        #             "account_object": account_object
        #         }
        # if type == 'chequing' and type in current_user_account_list:
        #     account_id = current_user_account_list['chequing']['account_id']
        #     current_account = current_user_account_list['chequing']['account_object']
        #     self.__current_account = ChequingAccount(account_id, current_account['name'], current_account['type'], current_account['balance'],
        #                                                current_account['transaction_list'])
        # elif type == 'saving' and type in current_user_account_list:
        #     account_id = current_user_account_list['saving']['account_id']
        #     current_account = current_user_account_list['saving']['account_object']
        #     self.__current_account = SavingAccount(account_id, current_account['name'], current_account['type'], current_account['balance'],
        #                                                current_account['transaction_list'])

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
    account_model = CustomerModelForClient('data/accounts.json')
    account_model._load_from_file()
    account_model._set_current_account(1,"saving")
    account_model.current_account.withdraw(500)
    account_model._update_current_account()