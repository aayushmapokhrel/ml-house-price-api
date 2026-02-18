from pydantic import BaseModel


class HouseInput(BaseModel):
    median_income: float
    house_age: float
    rooms: float
    population: float


class PredictionResponse(BaseModel):
    predicted_price: float
