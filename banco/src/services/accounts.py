from src.database import database
from databases.interfaces import Record
from src.models.accounts import accounts
from src.schemas.accounts import AccountIn


class AccountService:
    async def read_all(self, limit: int, skip: int = 0) -> list[Record]:
        query = accounts.select().where().limit(limit).offset(skip)
        return await database.fetch_all(query)

    async def create_account(self, account: AccountIn) -> int:
        command = accounts.insert().values(
            user_id=account.user_id,
            name=account.name,
            created_at=account.created_at,
            agency_number=account.agency_number,
            balance=account.balance,
        )

        account_id = await database.execute(command)

        query = accounts.select().where(accounts.c.account_id == account_id)
        return await database.fetch_one(query)
