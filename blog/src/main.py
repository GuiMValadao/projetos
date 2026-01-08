from contextlib import asynccontextmanager
from blog.src.controllers import auth, post
from fastapi import FastAPI
from blog.src.database import database, metadata, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    from blog.src.models.post import posts

    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(auth.router)
app.include_router(post.router)
