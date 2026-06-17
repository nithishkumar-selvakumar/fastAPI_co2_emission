from sqlalchemy import Column, Integer, String
from .database import Base

class CO2EmissionRating(Base):
    __tablename__ = "co2_emission_rating"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String, index=True) #make
    model = Column(String, index=True)
    class_type = Column(String, index=True) # vehicleclass
    engine_size = Column(Integer, index=True) # enginesize
    cylinders = Column(Integer, index=True)
    transmission = Column(String, index=True)
    fueltype = Column(String, index=True)
    cityconsumption = Column(Integer, index=True)
    highwayconsumption = Column(Integer, index=True) # hwyconsumption
    combination_consumption = Column(Integer, index=True) # combconsumption
    combmpg = Column(Integer, index=True)
    co2emissionrating = Column(String, index=True) # co2emission
    

