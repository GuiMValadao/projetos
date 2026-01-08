<<<<<<< HEAD
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from workout_api.configs.database import get_session

DatabaseDependency = Annotated[AsyncSession, Depends(get_session)]
=======
from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from workout_api.configs.database import get_session

DatabaseDependency = Annotated[AsyncSession, Depends(get_session)]
>>>>>>> 9e50be3a49701ce9c08b289a60135d291fc6a2fe
