class LoginInterface():
    def __init__(self):
        print('\n' + '-' * 50)
        print('Welcome to Vithiv Banking Management System!')
        print('Please log into the system to continue:\n')
        print('-' * 50 + '\n')

class MainMenuInterface():
    def __init__(self, username):
        print('\n' + '-' * 50)
        print('Welcome, {}! Please choose one of the following action to proceed:\n'.format(username))

        print('\nManage Customer profile:')
        print('1. Create new customer profile')
        print('2. Delete a customer profile')
        print('\nManage customer accounts:')
        print('3. Create a new customer account')
        print('4. Delete a customer account')
        print('5. View transaction log for a customer account')
        print('6. Print transaction log for a customer account')
        print('7. Log out')
        print('-' * 50 + '\n')

class CustomerCreationInterface():
    def __init__(self):
        print('\n' + '-' * 50)
        print('Please enter the following information to create a new customer profile:')
        print('Enter :q to go back to the main menu')
        print('-' * 50 + '\n')

class CustomerDeletionInterface():
    def __init__(self):
        print('\n' + '-' * 50)
        print('Please enter the customer ID to continue:')
        print('Enter :q to go back to the main menu')
        print('-' * 50 + '\n')

class AccountCreationInterface():
    def __init__(self):
        print('\n' + '-' * 50)
        print('Please enter the customer ID to continue:')
        print('Enter :q to go back to the main menu')
        print('-' * 50 + '\n')

class AccountDeletionInterface():
    def __init__(self):
        print('\n' + '-' * 50)
        print('Please enter the following information to delete an user account:')
        print('Enter :q to go back to the main menu')
        print('-' * 50 + '\n')

class ViewTransactionInterface():
    def __init__(self):
        print('\n' + '-' * 50)
        print('Please enter the following information to view transactions for an user account:')
        print('Enter :q to go back to the main menu')
        print('-' * 50 + '\n')

class PrintTransactionInterface():
    def __init__(self):
        print('\n' + '-' * 50)
        print('Please enter the following information to print transactions for an user account:')
        print('Enter :q to go back to the main menu')
        print('-' * 50 + '\n')

class ChooseCustomerProfileInterface():
    def __init__(self):
        print('\n' + '-' * 50)
        print('Enter customer information to continue:')
        print('Enter :q to go back to the main menu')
        print('-' * 50 + '\n')