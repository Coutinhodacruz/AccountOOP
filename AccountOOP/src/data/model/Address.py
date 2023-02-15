from typing import Type

from data.model.Country import Country
from data.model.State import State


class Adrress:
    def __init__(self):
        self._street_name: str = ""
        self._street_number: str = ""
        self._postal_code: int = 0
        self._lga: str = ""
        self._state = State
        self._country = Country
        self.address_id: int = 0

    def set_street_name(self, street_name):
        self._street_name = street_name

    def get_street_name(self):
        return self._street_name

    def set_street_number(self, street_number):
        self._street_number = street_number

    def get_street_number(self):
        return self._street_number

    def set_postal_code(self, postal_code):
        self._postal_code = postal_code

    def get_postal_code(self):
        return self._postal_code

    def set_lga(self, lga):
        self._lga = lga

    def get_lga(self):
        return self._lga

    def set_state(self, state: State) -> None:
        self._state = state

    def get_state(self) -> Type[State]:
        return self._state

    def set_country(self, country: Country) -> None:
        self._country = country

    def get_country(self) -> Type[Country]:
        return self._country

    def set_address_id(self, address_id):
        self.address_id = address_id

    def get_address_id(self):
        return self.address_id

    def __repr__(self):
        return f"""
                  Address_id{self.address_id},
                  Street_name{self._street_name},
                  Street_number{self._street_number},
                  Postal_code{self._postal_code},
                  Lga{self._lga},
                  State{self._state},
                  Country{self._country}
        
        """

    def __str__(self):
        return f"""
                   Address_id{self.address_id},
                  Street_name{self._street_name},
                  Street_number{self._street_number},
                  Postal_code{self._postal_code},
                  Lga{self._lga},
                  State{self._state},
                  Country{self._country}

        """
