import json
import hashlib
from datetime import datetime
from models.account import ChequingAccount, SavingsAccount

class CustomerModel():
    def __init__(self, file_name='./models/data/customers.json'):
        self.__file_name = file_name

    @property
    def file_name(self):
        return self.__file_name

    def _load_from_file(self):
        with open(self.__file_name, 'r') as f:
            return json.load(f)

    def _save_to_file(self):
        customer_dict = {}
        with open(self.__file_name, 'r') as f:
            customer_dict = json.load(f)
        with open(self.__file_name, 'w') as f:
            json.dump(customer_dict, f, indent=2)

class CustomerModelForClient(CustomerModel):
    def __init__(self, file_name, card_number, pin):
        super().__init__(file_name)
        self.__card_number = card_number
        self.__pin = pin
        self.__customer_id = None
        self.__customer_name = None
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
    def current_account(self):
        return self.__current_account

    @current_account.setter
    def current_account(self, account):
        self.__current_account = account

    def _save_to_file(self):
        customer_dict = {}
        self.customer_account_dict[self.current_account.type] = self.current_account._to_dict()
        with open(self.file_name, 'r') as f:
            customer_dict = json.load(f)
        with open(self.file_name, 'w') as f:
            customer_dict[self.customer_id]['accounts'] = self.customer_account_dict
            json.dump(customer_dict, f, indent=2)

    def _load_customer(self):
        customers_dict = self._load_from_file()
        input_hash = hashlib.sha256(str.encode(self.__pin)).hexdigest()
        for customer_id, customer_object in customers_dict.items():
            if self.__card_number == customer_object['card_number'] and input_hash == customer_object['pin']:
                self.customer_id = customer_id
                self.customer_name = customers_dict[self.customer_id]['name']
                self.customer_account_dict = customers_dict[self.customer_id]['accounts']
                break


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

class CustomerModelForCLI(CustomerModel):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.__customers_dict = self._load_from_file()
        self.__current_customer_profile = None

    @property
    def customers_dict(self):
        return self.__customers_dict

    @customers_dict.setter
    def customers_dict(self, dict):
        self.__customers_dict = dict

    @property
    def current_customer_profile(self):
        return self.__current_customer_profile

    @current_customer_profile.setter
    def current_customer_profile(self, dict):
        self.__current_customer_profile = dict

    def _save_to_file(self):
        with open(self.file_name, 'w') as f:
            json.dump(self.customers_dict, f, indent=2)

    def make_pin_hash(self, pin):
        return hashlib.sha256(str.encode(pin)).hexdigest()


    def create_customer(self, name, pin):
        self.customers_dict = self._load_from_file()
        new_card_number = datetime.now().strftime('%Y%m%d%H%M%S')
        hash_pin = self.make_pin_hash(pin)
        new_customer_object = {
            "card_number": new_card_number,
            "card_type": "VISA",
            "pin": hash_pin,
            "name": name,
            "accounts": {}
        }
        new_customer_id = str(max([int(id) for id in self.customers_dict.keys()]) + 1)
        self.customers_dict[new_customer_id] = new_customer_object
        self._save_to_file()

    def delete_customer(self, customer_id):
        try:
            self.customers_dict = self._load_from_file()
            del self.customers_dict[customer_id]
            self._save_to_file()
            return True
        except:
            return False

    def delete_customer_account(self,customer_id,account_type):
        account_type_word = ''
        if account_type == "1":
            account_type_word = "chequing"
        elif account_type_word == "2":
            account_type_word = "saving"
        self.customers_dict = self._load_from_file()
        if self.customers_dict[customer_id]["accounts"]:
            del self.customers_dict[customer_id]["accounts"][account_type_word]
        self._save_to_file()

    def view_customer_transactions(self,account_id, account_type):
        account_type_word = ''
        if account_type == "1":
            account_type_word = "chequing"
        elif account_type_word == "2":
            account_type_word = "saving"
        print("Listing customer transactions:")
        self.customers_dict = self._load_from_file()
        number = 0
        for transaction in self.customers_dict[account_id]["accounts"][account_type_word]["transactions"]:
            print(transaction["time"] +" "+ transaction["type"]+" "+str(transaction["balance_before"])+" "+str(transaction["balance_after"])+" "+transaction["status"]+" "+transaction["description"])

    def print_customer_transactions(self,account_id, account_type):
        account_type_word = ''
        if account_type == "1":
            account_type_word = "chequing"
        elif account_type_word == "2":
            account_type_word = "saving"
        print("Listing customer transactions:")
        self.customers_dict = self._load_from_file()
        number = 0
        f = open("models/data/report_file.txt","w")
        for transaction in self.customers_dict[account_id]["accounts"][account_type_word]["transactions"]:
            f.write(transaction["time"] + " " + transaction["type"] + " " + str(transaction["balance_before"]) + " " + str(transaction["balance_after"]) + " " + transaction["status"] + " " + transaction["description"]+"\n")
        f.close()

    def create_account(self,customer_id,account_type):
        self.customers_dict = self._load_from_file()
        account_type_word = ''
        if account_type == "1":
            account_type_word = "chequing"
        elif account_type_word == "2":
            account_type_word = "saving"

        if not self.customers_dict[customer_id]["accounts"]:
            new_account = {
                "balance": 0,
                "transactions": []
            }
            self.customers_dict[customer_id]["accounts"][account_type_word]=new_account
            self._save_to_file()
        else:
            print("Account already exists")



if __name__ == '__main__':
    pass



