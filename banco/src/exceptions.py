from http import HTTPStatus


class AccountNotFoundError(Exception):
    pass


class TransactionError(Exception):
    def __init__(
        self,
        message: str = "Error during transaction attempt",
        status_code: int = HTTPStatus.NOT_FOUND,
    ) -> None:
        self.message = message
        self.status_code = status_code
