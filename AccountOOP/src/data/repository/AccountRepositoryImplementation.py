import random

from data.model.Account import Account
from data.model.User import User
from data.model.PersonalInformation import PersonalInformation
from data.repository.AccountRepositoryInterface import AccountRepositoryInterface


class AccountRepositoryImp(AccountRepositoryInterface):
    account_data_base = {}
    account_id_count: int = 0
    account = Account()
    personal_info = PersonalInformation()
    user = User()

    def create_new_account(self, first_name, last_name, mobile_number, age, gender, realship, lga, state, email,
                           country):
        self.account.set_account_id(self.account_id_count + 1)
        self.personal_info.set_first_name(first_name)
        self.personal_info.set_last_name(last_name)
        self.personal_info.set_email_address(email)
        self.personal_info.set_mobile_number(mobile_number)
        self.personal_info.set_local_govt(lga)
        self.personal_info.set_state_of_origin(state)
        self.personal_info.set_country_code(country)
        self.user.set_user_personal_information(self.personal_info)
        self.account.set_account_user(self.user)
        self.account.set_account_number(self._account_number_generator())
        self.account.set_account_name(self.user.get_user_personal_information().get_ful_name())

        self.account_data_base[self.account.get_account_id()] = self.account
        return self.account_data_base

    @staticmethod
    def _account_number_generator():
        value = [str(random.randint(0, 9)) for _ in range(8)]
        str_value = "02"
        for i in value:
            str_value = str_value + i
        return str_value

    def deposit(self, amount):
        pass

    def withdraw(self, amount, pin):
        pass

    def transfer(self, amount, account_name, account_number, bank_name, pin):
        pass

    def check_balance(self, account_number, pin):
        pass


if __name__ == '__main__':
    acc_impl = AccountRepositoryImp()
    print((acc_impl.create_new_account("Coutinho", "Dacruz", "08026091587", 56, "Male", "Single", "eko", "lagos",
                                       "coutinhodacruz@gmail.com", "Nigeria")))
