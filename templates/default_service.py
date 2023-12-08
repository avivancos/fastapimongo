from .models import %_name_%
from odmantic import AIOEngine
from typing import List

class %_name_%Service:
    def __init__(self, engine: AIOEngine):
        self.engine = engine

    async def get_%_name_%s(self) -> List[%_name_%]:
        # Fetch all %_name_% records
        return await self.engine.find(%_name_%)

    async def get_%_name_%_by_id(self, %_name_%_id: int) -> %_name_%:
        # Fetch a single %_name_% record by ID
        return await self.engine.find_one(%_name_%, %_name_%.id == %_name_%_id)

    async def create_%_name_%(self, %_name_%_data: %_name_%) -> %_name_%:
        # Create a new %_name_% record
        %_name_% = %_name_%(**%_name_%_data.dict())
        await self.engine.save(%_name_%)
        return %_name_%

    async def update_%_name_%(self, %_name_%_id: int, %_name_%_data: %_name_%) -> %_name_%:
        # Update an existing %_name_% record
        %_name_% = await self.get_%_name_%_by_id(%_name_%_id)
        if %_name_%:
            %_name_%.update(%_name_%_data.dict())
            await self.engine.save(%_name_%)
        return %_name_%

    async def delete_%_name_%(self, %_name_%_id: int) -> bool:
        # Delete a %_name_% record
        %_name_% = await self.get_%_name_%_by_id(%_name_%_id)
        if %_name_%:
            await self.engine.delete(%_name_%)
            return True
        return False