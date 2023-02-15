from enum import Enum



class AccountType(Enum):
    CURRENT = 1
    SAVINGS = 2
    COOPERATE = 3

    def __repr__(self):
        return f"""
                CURRENT {self.CURRENT}
                SAVINGS {self.SAVINGS}
                COOPERATE {self.COOPERATE}
        """

    def __str__(self):
        return f"""
                CURRENT {self.CURRENT}
                SAVINGS {self.SAVINGS}
                COOPERATE {self.COOPERATE}
        """
