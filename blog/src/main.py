from contextlib import asynccontextmanager

from fastapi.responses import JSONResponse
from src.exceptions import NotFoundPostError
from src.controllers import auth, post
from fastapi import FastAPI, Request
from src.database import database, metadata, engine
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    from src.models.post import posts

    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()


tags_metadata = [
    {
        "name": "auth",
        "description": "Authentication operations",
    },
    {
        "name": "post",
        "description": "Post maintenance operations",
        "externalDocs": {
            "description": "External documentation for Posts.api",
            "url": "http://post-api.com.",
        },
    },
]

servers = [
    {"url": "http://localhost:8000", "description": "Staging environment"},
    {
        "url": "https://projetos-vfgz.onrender.com",
        "description": "Production environment",
    },
]

app = FastAPI(
    title="Blog DIO API",  # Change page title
    version="1.0.2",
    summary="API para blog pessoal",
    description="""
Blog DIO API
## Posts
Você poderá:

* **Criar posts**
* **Recuperar posts**
* **Recuperar posts por ID**
* **Atualizar posts**
* **Excluir posts**
* **Limitar quantidade de posts diários** (_not implemented_).

""",
    openapi_tags=tags_metadata,
    servers=servers,
    redoc_url=None,
    # openapi_url=None,   # disable docs
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
app.include_router(post.router, tags=["post"])


@app.exception_handler(NotFoundPostError)
async def not_found_post_exception_handler(request: Request, exc: NotFoundPostError):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})
