from enum import Enum


class NextOfKinRelation(Enum):
    MOTHER = "MOTHER"
    FATHER = "FATHER"
    BROTHER = "BROTHER"
    SISTER = "SISTER"
    SON = "SON"
    DAUGHTER = "DAUGHTER"
    COUSIN = "COUSIN"
    UNCLE = "UNCLE"
    AUNTY = "AUNTY"

    def __repr__(self):
        return f"""
                    MOTHER: {self.MOTHER},
                    FATHER: {self.FATHER},
                    BROTHER: {self.BROTHER},
                    SISTER: {self.SISTER},
                    SON: {self.SON},
                    DAUGHTER: {self.DAUGHTER},
                    COUSIN: {self.COUSIN},
                    UNCLE: {self.UNCLE},
                    AUNTY: {self.AUNTY}
                    """

    def __str__(self):
        return f"""
                    MOTHER: {self.MOTHER},
                    FATHER: {self.FATHER},
                    BROTHER: {self.BROTHER},
                    SISTER: {self.SISTER},
                    SON: {self.SON},
                    DAUGHTER: {self.DAUGHTER},
                    COUSIN: {self.COUSIN},
                    UNCLE: {self.UNCLE},
                    AUNTY: {self.AUNTY}
                    """
