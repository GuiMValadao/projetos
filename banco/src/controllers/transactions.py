from fastapi import APIRouter, status, Depends
from src.schemas.transactions import TransactionIn
from src.security import login_required
from src.views.accounts import TransactionOut
from src.services.transactions import TransactionService

router = APIRouter(prefix="/transactions", dependencies=[Depends(login_required)])

service = TransactionService()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TransactionOut)
async def create_transaction(transaction: TransactionIn):
    return await service.create(transaction)
