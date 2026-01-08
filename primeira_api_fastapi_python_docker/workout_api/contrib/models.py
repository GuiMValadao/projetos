<<<<<<< HEAD
from uuid import uuid4
from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID


class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), default=uuid4, nullable=False
    )
=======
from uuid import uuid4
from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as PG_UUID


class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), default=uuid4, nullable=False
    )
>>>>>>> 9e50be3a49701ce9c08b289a60135d291fc6a2fe
