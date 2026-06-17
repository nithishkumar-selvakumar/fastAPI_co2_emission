from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import pandas as pd
from .database import get_db, Base, engine
from .models import CO2EmissionRating

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

@app.post("/emissiondata")
def load_emission_data(db:Session = Depends(get_db)):
    existing_count = db.query(CO2EmissionRating).count()

    if existing_count > 0:
        return {"message": "Data already loaded"}
    
    try:
        data_frame = pd.read_csv("data/CO2_Emissions_Canada_Clean.csv")

        data_frame = data_frame.rename(columns={
        "make": "brand",
        "vehicleclass": "class_type",
        "enginesize": "engine_size",
        "hwyconsumption": "highwayconsumption",
        "combconsumption": "combination_consumption",
        "co2emission": "co2emissionrating"
        })
        
        records = data_frame.to_dict(orient="records")

        db.bulk_insert_mappings(CO2EmissionRating,records)
        db.commit()

        return {
            "success": True,
            "records_inserted": len(records)
        }
    except Exception as e:
        db.rollback()
        return {
            "success": False,
            "error": str(e)
        }