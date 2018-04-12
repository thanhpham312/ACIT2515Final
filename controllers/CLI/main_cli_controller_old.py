import json
from json import JSONEncoder
import hashlib
import sys
from models.customer_model import CustomerModelForCLI

class CLIModelController():
    __USERID = 1000
    def __init__(self, file_name):
        self._account_model = CustomerModelForCLI(file_name)
        self._account_model._load_from_file()

    def check_input(self):
        what_to_do = 0
        while what_to_do != "5":
            print("Welcome")
            print("1: Add new account")
            print("2: Change account holder name")
            print("3: View transaction log")
            print("4: Delete account")
            print("5: Exit")
            if what_to_do == "1":
                self._add_new_account()
            elif what_to_do == "2":
                id = input("Enter id of the user: ")
                new_name = input("Enter the new name of the user to change the holder name: ")
                self._change_account_holder_name(id, new_name)
            elif what_to_do == "3":
                id = input("Enter id of the user to view transactions: ")
                self._view_account_transaction_log(id)
            elif what_to_do == "4":
                id = input("Enter id of the user to delete it: ")
                self._delete_account(id)

    def _add_new_account(self):
        # id = str(len(self._account_model.account_list) + 1)
        id = CLIModelController.__USERID+1
        name = input('Type in a new account holder name:\n')
        password = input('Type in a new account password:\n')
        while 1:
            type = input('Set the account type\n\t1: chequing\n\t2: saving')
            if type == "1" or type == "2":
                break
            else:
                print('Invalid option!\n')
        while 1:
            try:
                balance = float(input('Input a balance:\n'))
                break
            except ValueError:
                print('Please input a float or int\n')

        new_id = {
            "id": id
        }
        new_account = {
            "name": name,
            "password": password
        }
        acc_type = ""
        if type == "1":
            acc_type = {
                type: 'chequing'
            }
        elif type == "2":
            acc_type = {
                type: 'saving'
            }
        trans_list = {
            "transaction_list": []
        }


        self._account_model.account_list['customers']= new_id
        self._account_model.account_list['customers'][new_id] = new_account
        self._account_model.account_list['customers'][new_id][new_account] = acc_type
        self._account_model.account_list['customers'][new_id][new_account][acc_type] = trans_list
        self._account_model._save_to_file()

    def _delete_account(self, account_id):
        try:
            self._account_model.account_list['customers'].pop(account_id)
            self._account_model._save_to_file()
        except:
            print('No account found')

    def _change_account_holder_name(self,id,new_holder_name):
        try:
            #print(self._account_model.account_list)
            print(self._account_model.account_list)
            # self._account_model.account_list['customers'][id]['username'] = new_holder_name
            # self._account_model._save_to_file()
        except:
            print('No account found')

    def _view_account_transaction_log(self,id):
        try:
            trans_list = self._account_model.account_list['account_list'][id]['transaction_list']
            for transaction in trans_list:
                print(transaction["time"]+' '+transaction["type"]+' '+transaction["balance_before"]+' '+transaction["balance_after"]+' '+transaction["status"]+' '+transaction["description"])
        except:
            print('No account found')

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
