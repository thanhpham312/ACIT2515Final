from models.account_model import AccountModel


class AccountModelForCLI(AccountModel):
    def __init__(self, file_name):
        super().__init__(file_name)


if __name__ == '__main__':
    pass


