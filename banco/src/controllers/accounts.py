from fastapi import APIRouter, status, Depends
from src.schemas.accounts import AccountIn
from src.security import login_required
from src.views.accounts import AccountOut, TransactionOut
from src.services.accounts import AccountService
from src.services.transactions import TransactionService


router = APIRouter(prefix="/accounts", dependencies=[Depends(login_required)])

service = AccountService()
tx_service = TransactionService()


@router.get("/", response_model=list[AccountOut])
async def read_accounts(limit: int, skip: int = 0):
    return await service.read_all(limit=limit, skip=skip)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=AccountOut)
async def create_account(account: AccountIn):
    return await service.create_account(account)


@router.get("/{id}", response_model=list[TransactionOut])
async def read_account_transactions(id: int, limit: int, skip: int = 0):
    return await tx_service.read_all(account_id=id, limit=limit, skip=skip)
