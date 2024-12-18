from fastapi import HTTPException
from fastapi.responses import JSONResponse

from sqlalchemy import insert, select, func, delete, update
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError
from app.database import async_session_maker


class BaseService:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none_relations(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).options(selectinload('*'))
            query = query.filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).options(selectinload('*'))
            query = query.filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def add_one(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def add_one_return_id(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            try:
                result = await session.execute(query)
                await session.commit()
                created_id = result.lastrowid
                return {"status": True, "detail": f"success add record id: {created_id}"}
            except IntegrityError as e:
                await session.rollback()
                return JSONResponse(status_code=500, content={"status": False, "detail": f"{e}"})

    @classmethod
    async def delete_one(cls, model_id: int):
        async with async_session_maker() as session:
            existing_record = await session.execute(
                select(cls.model).where(cls.model.id == model_id)
            )
            existing_record = existing_record.scalar_one_or_none()
            if existing_record is None:
                return JSONResponse(status_code=404,
                                    content={"status": False, "detail": f"Record with id {model_id} not found."})

            query = delete(cls.model).where(cls.model.id == model_id)
            await session.execute(query)
            await session.commit()
            return {"status": True, "detail": f"success delete record id: {model_id}"}

    @classmethod
    async def update_one(cls, **update_data):
        model_id: int = update_data['id']
        async with async_session_maker() as session:
            existing_record = await session.execute(
                select(cls.model).where(cls.model.id == model_id)
            )
            existing_record = existing_record.scalar_one_or_none()
            if existing_record is None:
                return JSONResponse(status_code=404, content={"status": False, "detail": "record not found"})
            query = update(cls.model).where(cls.model.id == model_id).values(**update_data)
            await session.execute(query)
            await session.commit()
            return {"status": True, "detail": "record successfully updated"}

    @classmethod
    async def count(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(func.count()).select_from(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one()
