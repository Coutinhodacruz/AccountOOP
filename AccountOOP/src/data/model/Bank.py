from data.model.Address import Adrress


class Bank:
    def __init__(self):
        self._bank_name: str = ""
        self._bank_branch_location = Adrress()
        self._branch_sort_code: int = 0
        self._bank_swift_code: int = 0
        self._bank_address: str = ""
        self._bank_manager: str = ""
        self._bank_id: int = 0


    def set_bank_name(self, bank_name):
        self._bank_name = bank_name

    def get_bank_name(self):
        return self._bank_name

    def set_bank_branch_location(self, branch_bank_location):
        self._bank_branch_location = branch_bank_location

    def get_bank_branch_location(self):
        return self._bank_branch_location

    def set_branch_sort_code(self, branch_sort_code):
        self._branch_sort_code = branch_sort_code

    def get_branch_sort_code(self):
        return self._branch_sort_code

    def set_bank_swift_code(self, bank_swift_code):
        self._bank_swift_code = bank_swift_code

    def get_bank_swift_code(self):
        return self._bank_swift_code

    def set_bank_address(self, bank_address):
        self._bank_address = bank_address

    def get_bank_address(self):
        return self._bank_address

    def set_bank_manager(self, bank_manager):
        self._bank_manager = bank_manager

    def get_bank_manager(self):
        return self._bank_manager

    def set_bank_id(self, bank_id):
        self._bank_id = bank_id

    def get_bank_id(self):
        return self._bank_id



    def __repr__(self):
        return f"""  
                    Bank_id:{self._bank_id}
                    Bank_name: {self._bank_name},
                    Bank_branch_location: {self._bank_branch_location},
                    Branch_sort_code: {self._branch_sort_code},
                    bank_swift_code: {self._bank_swift_code},
                    bank_address: {self._bank_address},
                    bank_manager: {self._bank_manager},
                    
        """

    def __str__(self):
        return f"""
                    bank_id:{self._bank_id}
                    bank_name: {self._bank_name},
                    bank_branch_location: {self._bank_branch_location},
                    branch_sort_code: {self._branch_sort_code},
                    bank_swift_code: {self._bank_swift_code},
                    bank_address: {self._bank_address},
                    bank_manager: {self._bank_manager},

        """
