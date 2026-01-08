<<<<<<< HEAD
from fastapi import FastAPI
from fastapi_pagination import add_pagination
from workout_api.routers import api_router


app = FastAPI(title="WorkoutApi")
add_pagination(app)
app.include_router(api_router)
=======
from fastapi import FastAPI
from fastapi_pagination import add_pagination
from workout_api.routers import api_router


app = FastAPI(title="WorkoutApi")
add_pagination(app)
app.include_router(api_router)
>>>>>>> 9e50be3a49701ce9c08b289a60135d291fc6a2fe
