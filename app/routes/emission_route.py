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
