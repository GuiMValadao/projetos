<<<<<<< HEAD
from datetime import datetime
from typing import Annotated
from pydantic import UUID4, BaseModel, Field
from sqlalchemy import DateTime


class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"
        from_attributes = True


class OutMixin(BaseModel):
    id: Annotated[UUID4, Field(description="Identificador")]
    created_at: Annotated[datetime, Field(description="Data de criação")]
=======
from datetime import datetime
from typing import Annotated
from pydantic import UUID4, BaseModel, Field
from sqlalchemy import DateTime


class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"
        from_attributes = True


class OutMixin(BaseModel):
    id: Annotated[UUID4, Field(description="Identificador")]
    created_at: Annotated[datetime, Field(description="Data de criação")]
>>>>>>> 9e50be3a49701ce9c08b289a60135d291fc6a2fe
