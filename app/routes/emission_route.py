from  fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core.database  import get_db
from app.services.emission_service import EmissionService

router = APIRouter(
    prefix="/emission",
   tags=["Emission"]
)

@router.post("/load-data")
def load_emission_data(db:Session = Depends(get_db)):
    return EmissionService.load_emission_data(db=db)

@router.get("/brands",response_model=list[str])
def get_brands(db:Session = Depends(get_db)):
    return EmissionService.get_all_brands(db=db)

@router.get("/models-by-brand/{brand}",response_model=list[str])
def get_models_by_brand(brand:str,db:Session = Depends(get_db)):
    return EmissionService.get_all_models_by_brand(brand=brand,db=db)