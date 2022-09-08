from fastapi import FastAPI
import uvicorn

from app.core.config import settings
from app.endpoints import router


app = FastAPI(title=settings.app_title)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, reload=True)
