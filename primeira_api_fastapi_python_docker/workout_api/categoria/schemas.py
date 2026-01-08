<<<<<<< HEAD
from typing import Annotated
from pydantic import UUID4, BaseModel, Field, PositiveFloat

from workout_api.contrib.schemas import (
    BaseSchema,
)


class CategoriaIn(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome da categoria", example="Scale", max_length=10)
    ]


class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description="Identificador de Categoria")]
=======
from typing import Annotated
from pydantic import UUID4, BaseModel, Field, PositiveFloat

from workout_api.contrib.schemas import (
    BaseSchema,
)


class CategoriaIn(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome da categoria", example="Scale", max_length=10)
    ]


class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description="Identificador de Categoria")]
>>>>>>> 9e50be3a49701ce9c08b289a60135d291fc6a2fe
