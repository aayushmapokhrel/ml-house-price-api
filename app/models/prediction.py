from sqlalchemy import Column, Integer, Float
from app.core.database import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    median_income = Column(Float)
    house_age = Column(Float)
    rooms = Column(Float)
    population = Column(Float)
    prediction = Column(Float)
