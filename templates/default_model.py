from odmantic import Model, Field

class %_name_%(Model):
    id: int = Field(..., primary_field=True)
    name: str = Field(...)
    description: str = Field(...)
    # Aquí podrías agregar más campos si los necesitas