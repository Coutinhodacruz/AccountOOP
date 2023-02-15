from data.model import PersonalInformation, Address
from data.model.NextOfKinRelation import NextOfKinRelation
from data.model.PersonalInformation import PersonalInformation


class NextOfKin:
    def __init__(self):
        self._next_of_kin_address = Address
        self._next_of_kin_real_ship = NextOfKinRelation
        self._personal_information = PersonalInformation()

    def set_next_of_kin_address(self, next_of_kin_address):
        self._next_of_kin_address = next_of_kin_address

    def get_next_of_kin_address(self):
        return self._next_of_kin_address

    def set_next_of_kin_real_ship(self, next_of_kin_real_ship):
        self._next_of_kin_real_ship = next_of_kin_real_ship

    def get_next_of_kin_real_ship(self):
        return self._next_of_kin_real_ship

    def set_personal_information(self, personal_information):
        self._personal_information = personal_information

    def get_personal_information(self):
        return self._personal_information

    def __repr__(self):
        return f"""
                  Next_of_kin_address{self._next_of_kin_address},
                  Next_of_kin_real_ship{self._next_of_kin_real_ship},
                  Personal_information{self._personal_information}
        """

    def __str__(self):
        return f"""
                  Next_of_kin_address{self._next_of_kin_address},
                  Next_of_kin_real_ship{self._next_of_kin_real_ship},
                  Personal_information{self._personal_information}
        """
