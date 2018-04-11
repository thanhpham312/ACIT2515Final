import json
from models.customer_model import CustomerModel




if __name__ == '__main__':
    new_customer_model = CustomerModelForClient('data/customers.json', "1")
    new_customer_model._load_customer()
    new_customer_model._set_current_account('chequing')
    print(new_customer_model.current_account)
    new_customer_model.current_account.withdraw(500)
    new_customer_model._save_to_file()