from pydantic import BaseModel, AwareDatetime, NaiveDatetime, PositiveFloat


class AccountOut(BaseModel):
    account_id: int
    user_id: int
    name: str
    balance: float
    created_at: AwareDatetime | NaiveDatetime
    agency_number: int = 1


class TransactionOut(BaseModel):
    id: int
    account_id: int
    type: str
    amount: PositiveFloat
    time_of_transaction: AwareDatetime | NaiveDatetime
