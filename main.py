import asyncio

from fastapi import FastAPI, Header, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.city.router import router as city_router
from app.employment_rate.router import router as employment_rate_router
from app.users.service import UserService
from app.vacancy_title.router import router as vacancy_title_router
from app.work_experience.router import router as work_experience_router
from app.vacancy.router import router as vacancy_router

import uvicorn


async def verify_auth_header(x_auth: str = Header(...)):
    if not x_auth:
        raise HTTPException(status_code=403, detail="Invalid or missing Authorization header")
    if not await UserService().find_one_or_none(**{"token": x_auth}):
        raise HTTPException(status_code=403, detail="Invalid token")


# app = FastAPI(dependencies=[Depends(verify_auth_header)])
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(city_router)
app.include_router(employment_rate_router)
app.include_router(vacancy_title_router)
app.include_router(work_experience_router)
app.include_router(vacancy_router)


async def main():
    config = uvicorn.Config(app, host="0.0.0.0", port=8004, reload=True)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
