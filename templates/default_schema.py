from pydantic import BaseModel

class %_name_%Base(BaseModel):
    # Define your fields here
    pass

class %_name_%(%_name_%Base):
    id: int

    class Config:
        orm_mode = True