from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.prediction import HouseInput, PredictionResponse
from app.services.ml_service import predict_price
from app.services.prediction_service import save_prediction
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/predict", response_model=PredictionResponse)
def predict(input_data: HouseInput, db: Session = Depends(get_db)):

    prediction = predict_price(input_data)

    save_prediction(db, input_data, prediction)

    return {"predicted_price": prediction}
