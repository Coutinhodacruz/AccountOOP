from enum import Enum


class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHERS = 3


    def __repr__(self):
        return f"""
                Male{self.MALE}
                Female{self.FEMALE}
                Others{self.OTHERS}
        """

    def __str__(self):
        return f"""
                   Male{self.MALE}
                   Female{self.FEMALE}
                   Others{self.OTHERS}
           """
