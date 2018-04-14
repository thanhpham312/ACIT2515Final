import json
import hashlib

class EmployeeModel():
    def __init__(self, file_name, username, password):
        self.__file_name = file_name
        self.__username = username
        self.__password = password
        self.__employee_id = None

    @property
    def username(self):
        return self.__username

    @property
    def file_name(self):
        return self.__file_name

    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, id):
        self.__employee_id = id

    def _load_from_file(self):
        with open(self.file_name, 'r') as f:
            return json.load(f)

    def _save_to_file(self, data):
        with open(self.file_name, 'w') as f:
            json.dump(data, f, indent=4)

    def _load_employee(self):
        employees_dict = self._load_from_file()
        for employee_id, employee_object in employees_dict.items():
            if self.__username == employee_object['username'] and self.__password == employee_object['password']:
                self.employee_id = employee_id



# class EmployeeModelForClient(EmployeeModel):
#     def __init__(self, file_name, username, password):
#         super().__init__(file_name)
#         self.__username = username
#         self.__password = password
#         self.__current_user_id = None
#         self._set_current_user_id()
#
#     @property
#     def current_user_id(self):
#         return self.__current_user_id
#
#     def _set_current_user_id(self):
#         for id, user_object in self.user_list['user_list'].items():
#             if self.__username == user_object['username'] and self.__password == user_object['password']:
#                 self.__current_user_id = id
#                 break