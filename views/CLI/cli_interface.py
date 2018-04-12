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


class AddUserInterface():
    def __init__(self):
        print('')