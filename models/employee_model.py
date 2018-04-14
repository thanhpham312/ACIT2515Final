import json
import hashlib

class EmployeeModel():
    '''
        Model for a employee profile

        Attributes:
            __file_name: location of the employee data
            __username: The current employee's username
            __password: The current employee's password
            __employee_id: The current employee's id
        Methods:
            _load_from_file: load employee data from database
            _save_to_file: save employee data to database
            _load_employee: populate the class' attribute with employee data from the database
    '''
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
