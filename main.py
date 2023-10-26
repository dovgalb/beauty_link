from fastapi import FastAPI
import uvicorn
from src.endpoints.users import users_router
from src.endpoints.services import services_router

app = FastAPI(
    title="BeautyLink"
)


app.include_router(users_router, prefix='/users', tags=['Users'],)
app.include_router(services_router, prefix="/services", tags=["Services"],)

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
