from enum import Enum
from pydantic import AwareDatetime, BaseModel, NaiveDatetime, PositiveFloat


class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"


class TransactionIn(BaseModel):
    account_id: int
    type: TransactionType
    amount: PositiveFloat
    time_of_transaction: AwareDatetime | NaiveDatetime

    class Config:
        use_enum_values = True
