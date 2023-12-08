from pydantic import BaseModel

class %_name_%Base(BaseModel):
    # Define your fields here
    name: str
    description: str

class %_name_%Create(%_name_%Base):
    pass

class %_name_%Update(%_name_%Base):
    pass

class %_name_%InDBBase(%_name_%Base):
    id: int

    class Config:
        orm_mode = True

# Schemas to be used for reading data
class %_name_%(%_name_%InDBBase):
    pass

# Schemas to be used for writing data
class %_name_%InDB(%_name_%InDBBase):
    pass