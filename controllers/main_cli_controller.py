import json
from json import JSONEncoder
import hashlib
from models.account_model_for_cli import AccountModel

class CLIModelController():
    def __init__(self, file_name):
        self._account_model = AccountModel(file_name)
        self._account_model._load_from_file()

    def _add_new_account(self, user_id):
        id = str(len(self._account_model.account_list) + 1)
        name = input('Type in a new account holder name:\n')
        while 1:
            type = input('Set the account type\n\t1: chequing\n\t2: saving')
            if type == "1" or type == "2":
                break
        balance = input('Input a balance:\n')

        new_account = {
            "user_id": str(user_id),
            "name": name,
            "type": 'normal',
            "balance": balance,
            "transaction_list": []
        }

        if type == "1":
            new_account['type'] = 'chequing'
        elif type == "2":
            new_account['type'] = 'saving'


        self._account_model.account_list[id] = new_account
        self._account_model._save_to_file()

    def _delete_account(self, account_id):
        pass

    def _change_account_holder_name(self):
        pass

    def _view_account_transaction_log(self):
        pass

if __name__ == '__main__':
    pass
        # userlist = user.split('\n')
        # userObj =
        # for i in userlist:


        # user_cred = {user_name+','+user_id+','+user_acc_type}
        # with open(path, 'r') as outfile:
        #     userlist = json.load(outfile)
        # userlist2=userlist['account_list'].append(user)
        # print(userlist2)

        # with open(path, 'w') as outfile2:
        #     outfile2.seek(0)
        #     json.dump(userlist2, outfile2)
        #     #print(userlist['account_list'])
            # json.dump(user, outfile)




# def admin_login():
#     admin = Admin_Functions()
#     # username = input('Type your username: ')
#     # password = input('Type your password: ')
#     f = open("list_of_admins.csv", 'r')
#     reader = csv.reader(f)
#     for admin_acc in reader:
#         if(==admin_acc):
#             print('Login success')
#         else:
#             print('Not matched')
#     f.close()


# def hash_and_store_data():
#     admin = Admin_Functions()
#     hashed_admin_login = str(hash(admin._admin_name))
#     # print()
#     f =open("list_of_admins.csv",'a')
#     f.write(hashed_admin_login+'\n')
#     f.close()

# if __name__ == "__main__":
#     admin = Admin_Functions()
#     if admin._function=='acc_create':
#         admin.add_new_user()
    #admin_login()
    # hash_and_store_data()

# import sys
#
# class Admin_Functions():
#     def __init__(self):
#         self._admin_name = input('Enter admin name: ')
#         self._admin_pass = input('Enter admin password: ')
