from pydantic import BaseModel


class EventCreate(BaseModel):
    id: int
    name: str
    danger_lvl: int
