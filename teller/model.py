from enum import Enum

class AccountType(Enum):
    AMEX = 'AMEX'
    TD = 'TD'
    MFC = 'MFC'
    RBC = 'RBC'
    BMO = 'BMO'
    
class Transaction():
    def __init__(self, account_type, date, description, amount):
        self.account_type = account_type
        self.date = date
        self.description = description
        self.amount = amount

    def __hash__(self):
        return hash((self.description,
                     self.amount, 
                     self.date, 
                     self.account_type))
    
    def __eq__(self, other):
        return isinstance(other, Transaction) and \
               self.account_type == other.account_type and \
               self.date == other.date and \
               self.description == other.description and \
               self.amount == other.amount

    def __repr__(self):
        return (f"({self.amount}, "
                f"{self.date}, "
                f"{self.account_type.value}, "
                f"{self.description})")


