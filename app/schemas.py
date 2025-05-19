from pydantic import BaseModel

class TodoCreate(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

class TodoResponse(TodoCreate):
    id: int

    class Config:
        from_attributes = True  # Работает с ORM (бывшее orm_mode)