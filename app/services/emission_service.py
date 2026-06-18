from sqlalchemy.orm import Session
from app.models.emission_model import EmissionModel
import pandas as pd


class EmissionService:

    @staticmethod
    def load_emission_data(db:Session):
        existing_count = db.query(EmissionModel).count()

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

            db.bulk_insert_mappings(EmissionModel,records)
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

    @staticmethod
    def get_all_brands(db:Session):
        result = db.query(EmissionModel.brand).distinct().all()
        return [row[0] for row in result]

    @staticmethod
    def get_all_models_by_brand(brand:str,db:Session):
        result = db.query(EmissionModel.model).filter(EmissionModel.brand == brand).distinct().all()
        return [row[0] for row in result]