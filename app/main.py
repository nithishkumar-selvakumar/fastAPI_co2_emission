from fastapi import FastAPI
from .core.database import  Base, engine
from app.routes.emission_route import router as emission_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(emission_router)

@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

# @app.post("/load-emission-data")
# def load_emission_data(db:Session = Depends(get_db)):
#     existing_count = db.query(CO2EmissionRating).count()

#     if existing_count > 0:
#         return {"message": "Data already loaded"}
    
#     try:
#         data_frame = pd.read_csv("data/CO2_Emissions_Canada_Clean.csv")

#         data_frame = data_frame.rename(columns={
#         "make": "brand",
#         "vehicleclass": "class_type",
#         "enginesize": "engine_size",
#         "hwyconsumption": "highwayconsumption",
#         "combconsumption": "combination_consumption",
#         "co2emission": "co2emissionrating"
#         })
        
#         records = data_frame.to_dict(orient="records")

#         db.bulk_insert_mappings(CO2EmissionRating,records)
#         db.commit()

#         return {
#             "success": True,
#             "records_inserted": len(records)
#         }
#     except Exception as e:
#         db.rollback()
#         return {
#             "success": False,
#             "error": str(e)
#         }

# @app.get("/brands")
# def get_brand(db:Session = Depends(get_db)):
#     result = db.query(CO2EmissionRating.brand).distinct().all()
#     return [row[0] for row in result]

# @app.get("/models/{brand}")
# def get_models_by_brand(brand:str,db:Session = Depends(get_db)):
#     result =  db.query(CO2EmissionRating.model).filter(CO2EmissionRating.brand == brand ).distinct().all()
#     return [row[0] for row in result]