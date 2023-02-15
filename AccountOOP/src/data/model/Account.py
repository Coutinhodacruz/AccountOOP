from data.model.AccountType import AccountType
from data.model.Bank import Bank
from data.model.User import User


class Account(object):
    def __init__(self):
        self._account_id = 0
        self.pin = None
        self.card_number = None
        self.bank = Bank()
        self.account_type = AccountType
        self.account_number = None
        self._account_user = User()
        self._transfer_limit = None
        self.account_limit = None
        self.account_name: str = ""

    def set_user(self, user):
        self._account_user = user

    def get_user(self):
        return self._account_user

    def set_account_id(self, account_id):
        self._account_id = account_id

    def get_account_id(self):
        return self._account_id

    def set_transfer_limit(self, transfer_limit):
        self._transfer_limit = transfer_limit

    def get_transfer_limit(self):
        return self._transfer_limit

    def set_pin(self, pin) -> None:
        self.pin = pin

    def get_pin(self):
        return self._pin

    def set_card_number(self, card_number) -> None:
        self.card_number = card_number

    def get_card_number(self):
        return self.card_number

    def set_account_number(self, acc_number: str) -> None:
        self.account_number = acc_number

    def get_account_number(self):
        return self.account_number

    def set_account_user(self, account_user) -> None:
        self._account_user = account_user

    def get_account_user(self):
        return self._account_user

    def set_account_limit(self, account_limit) -> None:
        self.account_limit = account_limit

    def get_account_limit(self):
        return self.account_limit

    def set_account_name(self, account_name):
        self.account_name = account_name

    def get_account_name(self):
        return self.account_name

    def __repr__(self):
        return f"""User Account Id;{self._account_id}
        Account Name: {self.account_name}
        User Account pin: {self.pin},
        User Card: {self.card_number},
        User Bank: {self.bank},
        User Account Type: {self.account_type},
        User Account Number: {self.account_number},
        Account User: {self._account_user},
        User Transfer Limit: {self._transfer_limit},
        User Account limit: {self.account_limit}
        """

    def __str__(self):
        return f"""User Account Id;{self._account_id}
        Account Name: {self.account_name}
        User Account pin: {self.pin},
        User Card: {self.card_number},
        User Bank: {self._bank},
        User Account Type: {self.account_type},
        User Account Number: {self.account_number},
        Account User: {self._account_user},
        User Transfer Limit: {self._transfer_limit},
        User Account limit: {self.account_limit}
        """
