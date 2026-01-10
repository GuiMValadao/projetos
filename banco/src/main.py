from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
from src.exceptions import TransactionError, AccountNotFoundError
from src.controllers import auth, transactions, accounts
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from src.database import database


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


tags_metadata = [
    {
        "name": "auth",
        "description": "Authentication operations",
    },
    {"name": "account", "description": "Account consult operations"},
    {
        "name": "transactions",
        "description": "Transaction consult operations",
    },
]

servers = [
    {"url": "http://localhost:8000", "description": "Staging environment"},
]

app = FastAPI(
    title="Transactions API",
    version="1.0",
    summary="API for account creation, transaction execution and consult",
    description="""
Transactions API
## Account
You will be able to:

* **Create accounts**
* **List all accounts**
* **List account transactions by account ID**

## Transaction
* **Create transactions**
""",
    openapi_tags=tags_metadata,
    servers=servers,
    redoc_url=None,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth.router, tags=["auth"])
app.include_router(accounts.router, tags=["account"])
app.include_router(transactions.router, tags=["transaction"])


@app.exception_handler(AccountNotFoundError)
async def account_not_found_exception_handler(
    request: Request, exc: AccountNotFoundError
):
    return JSONResponse(
        status_code=exc.status_code, content={"detail": "Acc not found"}
    )


@app.exception_handler(TransactionError)
async def not_found_transaction_exception_handler(
    request: Request, exc: TransactionError
):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT, content={"detail": str(exc.message)}
    )
