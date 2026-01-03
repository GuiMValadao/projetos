from datetime import datetime
from typing import Annotated, Optional
from pydantic import BaseModel, Field, PositiveFloat, UUID4
from uuid import uuid4
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta
from workout_api.categoria.schemas import CategoriaIn
from workout_api.contrib.schemas import (
    BaseSchema,
    OutMixin,
)


class Atleta(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome do atleta", example="João", max_length=50)
    ]
    cpf: Annotated[
        str, Field(description="CPF do atleta", example="1234567890", max_length=11)
    ]
    idade: Annotated[int, Field(description="Idade do atleta", example="24")]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", example=70.5)]
    altura: Annotated[
        PositiveFloat, Field(description="Altura do atleta", example=1.75)
    ]
    sexo: Annotated[str, Field(description="Sexo do atleta", example="M", max_lengt=1)]
    categoria: Annotated[CategoriaIn, Field(description="Categoria do atleta")]
    centro_treinamento: Annotated[
        CentroTreinamentoAtleta, Field(description="Centro de treinamento do atleta")
    ]


class AtletaIn(Atleta):
    pass


class AtletaOut(Atleta, OutMixin):
    pass


class AtletaResponse(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome do atleta", example="João", max_length=50)
    ]
    categoria: Annotated[CategoriaIn, Field(description="Categoria do atleta")]
    centro_treinamento: Annotated[
        CentroTreinamentoAtleta, Field(description="Centro de treinamento do atleta")
    ]
    id: UUID4
    created_at: Annotated[
        datetime,
        Field(
            description="Data de criação", example="01/01/2026, 10:00:00", max_lenght=20
        ),
    ]


class AtletaUpdate(BaseSchema):
    nome: Annotated[
        Optional[str],
        Field(None, description="Nome do atleta", example="João", max_length=50),
    ]
    idade: Annotated[
        Optional[int], Field(None, description="Idade do atleta", example="24")
    ]
