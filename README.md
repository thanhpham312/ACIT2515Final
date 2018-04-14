# ACIT 2515 Final Project - ATM Simulator

## Students Information
Ivan Shalagin

Thanh Pham

Viktor Sheverdin

## Project Description
This is the simulator of the ATM machine, designed for both customers and admins.

Admin part:
Admin part consists from the Command Line Interface(CLI later).
The functions available for admin are:
    >Create new profile for customer
    >Delete new profile for customer
    >Create new account for customer, both checking and saving
    >Delete account for specific customer
    >View transaction log for specific customer
    >Print transaction log for specific customer

To create new profile:
    1. Start the application from the command line. Type <python banking_manager.py>
    2. Login as administrator. (for test purpose, type <a> for admin name and <a> for password.
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


Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam quis nibh orci. Phasellus imperdiet interdum eros, eget semper purus pharetra non. Nulla imperdiet felis bibendum tortor posuere venenatis. Ut sem massa, ornare eu tincidunt ac, laoreet sed orci. Maecenas pharetra erat nibh, eget tempus velit consectetur nec. Nullam vel est congue sem vulputate commodo eget non turpis. Integer sollicitudin erat nibh, id interdum neque commodo in. Nunc ipsum elit, sodales eu tempor nec, accumsan in diam. In et faucibus urna. Maecenas et tellus eu risus consequat volutpat. Nulla sed vehicula orci. Donec a nulla dolor. Aenean quis ipsum eu dolor pellentesque aliquam eu eget ipsum. Integer nulla quam, dictum aliquam cursus nec, tristique sit amet velit. Maecenas mollis ipsum vel mi luctus viverra.