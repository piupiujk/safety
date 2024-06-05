from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.events.models import event
from src.events.schemas import EventCreate

router = APIRouter(
    prefix='/events',
    tags=['Event']
)


@router.get('/')
async def get_events(danger_lvl: int, session: AsyncSession = Depends(get_async_session)):
    query = select(event).where(event.c.danger_lvl == danger_lvl)
    result = await session.execute(query)
    return result.mappings().all()


@router.post('/')
async def add_events(new_event: EventCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(event).values(**new_event.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': "success"}
