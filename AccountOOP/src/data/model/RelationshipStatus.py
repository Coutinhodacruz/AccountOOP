from enum import Enum



class RelationshipStatus(Enum):
    SINGLE = "SINGLE"
    MARRIED = "MARRIED"
    IN_A_RELATIONSHIP = "IN_A_RELATIONSHIP"
    DIVORCED = "DIVORCED"
    SEPERATED = "SEPERATED"

    def __str__(self):
        return f"""
               SINGLE = {self.SINGLE},
               MARRIED = {self.MARRIED},
               IN_A_RELATIONSHIP = {self.IN_A_RELATIONSHIP},
               DIVORCED = {self.DIVORCED},
               SEPERATED ={self.SEPERATED}
        """


    def __repr__(self):
        return f"""
                      SINGLE = {self.SINGLE},
                      MARRIED = {self.MARRIED},
                      IN_A_RELATIONSHIP = {self.IN_A_RELATIONSHIP},
                      DIVORCED = {self.DIVORCED},
                      SEPERATED ={self.SEPERATED}
               """
