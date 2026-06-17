from pydantic import BaseModel
from typing import List

class EmissionData(BaseModel):
    brand: str
    model: str
    class_type: str
    engine_size: int
    cylinders: int
    transmission: str
    fueltype: str
    cityconsumption: int
    highwayconsumption: int
    combination_consumption: int
    combmpg: int
    co2emissionrating: str


class CreateEmissionData(BaseModel):
    items:List[EmissionData]

class responseEmissionData(EmissionData):
    id: int

    class Config:
        orm_mode = True