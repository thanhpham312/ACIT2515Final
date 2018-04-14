# ACIT 2515 Final Project - ATM Simulator

##################################### Students Information ################################################
Ivan Shalagin

Thanh Pham

Viktor Sheverdin (A01018756)

##################################### Project Description ##################################################
Overview:
    This is the simulator of the ATM machine, designed for both customers and admins.
    Program is designed using MVC model, and is disigned in such a waay for both admin and customer side.
    All data are stored in the JSON format, and all log reports are created in the TXT format.


Administrative side:
    From the admin side, it is possible to create, manage, and delete accounts.
    All modification for the accounts are done, based on the card number.
    PINs and hashed and that is why secured. They are stored in the json formatted document and checked if matched with
    passing PIN when login.

Customer side:
    From the customer side, the program has classical designe and basic working interface.
    The process is done so after the transaction completion it is possible to either continue operations, or
    to quit and allow other customer to use it.

####################################### HOW TO START ########################################################

A compiled version of the programs can be found in the dist directory.

For the GUI:
    1. Open cmd in the same directory as the atm_simulator.py file
    2. Run with python

For the CLI:
    1. Open cmd in the same directory as the banking_manager.py file
    2. Run with python
    WARNING: THe CLI profram won't work with pycharm's run function.

####################################### LOGIN INFOMATION ####################################################

For the GUI:
    Card number: 4856673772575768
    PIN: 1234

For the CLI:
    username: admin
    password: password

More customer profiles can be found in the json files located in /models/data

####################################### INSTRUCTIONS ########################################################


Admin part:
Admin part consists from the Command Line Interface(CLI later).
The functions available for admin are:
    >Create new profile for customer
    >Delete new profile for customer
    >Create new account for customer, both checking and saving
    >Delete account for specific customer
    >View transaction log for specific customer
    >Print transaction log for specific customer
    >Exit in non-main menu screen and return to main menu screen, by typing <:q>
    >Asks for the PIN confirmation from the user. For test purpose, type <1234>

To create new profile:
    1. Start the application from the command line. Type <python banking_manager.py>
    2. Login as administrator. (for test purpose, type <admin> for admin name and <password> for password.
        Note: password will not be displayed.
    3. Type <1> to create account.
    4. Enter the name for new customer and press ENTER.
    5. Type PIN and press ENTER.
        Note: PIN is hashed.
    6. Press ENTER to return to main menu.

To create new account for a customer:
    1. Type <3> and press ENTER.
    2. Type customer's ID you want to create new account.
    3. Type <1> for chequing account, or <2> for saving account.
    4. Press any key to continue.

To view transaction log:
    1. Type <5> and press ENTER.
    2. Type account number and press ENTER.

To print transaction log:
    1. Type <6> and press ENTER.
    2. Type account number and press ENTER.

To delete account:
    1. Type <4> and press ENTER.
    2. Type account number and press ENTER.
    3. Type account type and press ENTER.

To delete profile:
    1. Type <2> and press ENTER.
    2. Type account number and press ENTER.

For user in the GUI:
    1. To start application from the command line, open the atm_simulator file.
    2. In the appeared window enter the card number and PIN. For test: card number is 4856673772575768 and
        PIN is 1234.
        Note: PIN is numbers only.
    3. To clear all fields, click CANCEL

Functions available for user in GUI:
    1. Quick cash - withdraws $40 from the selected account.
    2. Withdraw.
    3. Deposit.
    4. Check balance.
    5. Change PIN
    6. Exit - returns to the login page

To withdraw:
    1. Login, using card number and PIN
    2. Click withdraw.
    3. Click account type.
    4. Click on the sum you want to withdraw. Alternatively click on OTHER and type amount.

To deposit:
    1. Login, using card number and PIN
    2. Click deposit.
    3. Click account type.
    4. Type the amount to deposit.

To check balance:
    1. Login, using card number and PIN
    2. Click check balance.

To change PIN:
    1. Login, using card number and PIN
    2. Click change PIN.
    3. Type new PIN.