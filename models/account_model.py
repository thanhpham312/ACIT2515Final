import json


class AccountModel():
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__account_list = {}

    @property
    def account_list(self):
        return self.__account_list

    def _load_from_file(self):
        with open(self.__file_name, 'r') as f:
            return json.load(f)

    def _save_to_file(self):
        with open(self.__file_name, 'w') as f:
            json.dump(self.__account_list, f, indent=2)


if __name__ == '__main__':
    pass


