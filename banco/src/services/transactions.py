from src.database import database
from databases.interfaces import Record
from src.models.transactions import TransactionType, transactions
from src.models.accounts import accounts
from src.schemas.transactions import TransactionIn
from src.exceptions import AccountNotFoundError, TransactionError
import sqlalchemy as sa


class TransactionService:
    async def read_all(
        self, account_id: int, limit: int, skip: int = 0
    ) -> list[Record]:
        query = (
            transactions.select()
            .where(transactions.c.account_id == account_id)
            .limit(limit)
            .offset(skip)
        )
        return await database.fetch_all(query)

    @database.transaction()
    async def create(self, transaction: TransactionIn) -> int:
        query = accounts.select().where(accounts.c.account_id == transaction.account_id)
        account = await database.fetch_one(query)
        if not account:
            raise AccountNotFoundError
        if transaction.type == TransactionType.WITHDRAWAL:
            balance = float(account.balance) - transaction.amount
            if balance < 0:
                raise TransactionError("Operation aborted due insuficient balance.")
        else:
            balance = float(account.balance) + transaction.amount

        transaction_id = await self.__register_transaction(transaction)

        await self.__update_account_balance(transaction.account_id, balance)

        query = transactions.select().where(transactions.c.id == transaction_id)

        return await database.fetch_one(query)

    async def __update_account_balance(self, account_id: int, balance: float) -> None:
        command = (
            accounts.update()
            .where(accounts.c.account_id == account_id)
            .values(balance=balance)
        )
        await database.execute(command)

    async def __register_transaction(self, transaction: TransactionIn) -> int:
        command = transactions.insert().values(
            account_id=transaction.account_id,
            type=transaction.type,
            amount=transaction.amount,
            time_of_transaction=transaction.time_of_transaction,
        )
        return await database.execute(command)
