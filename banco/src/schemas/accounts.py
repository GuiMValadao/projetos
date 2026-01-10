from pydantic import BaseModel, PositiveFloat, AwareDatetime, NaiveDatetime


class AccountIn(BaseModel):
    user_id: int
    name: str
    agency_number: int = 1
    balance: PositiveFloat
    created_at: AwareDatetime | NaiveDatetime
