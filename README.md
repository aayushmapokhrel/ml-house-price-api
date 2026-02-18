# ML House Price Prediction API

A FastAPI-based REST API for predicting house prices using a trained Random Forest Regressor.  

## Features

- Predict house prices based on features:
  - `median_income`
  - `house_age`
  - `rooms`
  - `population`
- Store predictions in a PostgreSQL database
- Simple, RESTful API powered by **FastAPI**
- Uses **Random Forest** for regression
- Easy to extend with more features or models

---

## Project Structure

  house-price-prediction/
  │
  ├─ app/
  │ ├─ api/
  │ │ └─ routes.py 
  │ ├─ core/
  │ │ └─ database.py 
  │ ├─ ml/
  │ │ └─ model.pkl 
  │ ├─ models/
  │ │ └─ prediction.py
  │ └─ services/
  │ └─ ml_service.py 
  │
  ├─ main.py 
  ├─ requirements.txt 
  ├─ Dockerfile 
  ├─ docker-compose.yml 
  └─ .env 

## Installation

# Clone the repository:

git clone https://github.com/<your-username>/ml-house-price-api.git

## Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate      # Windows
# or
source venv/bin/activate   # Mac/Linux

## Install dependencies:
pip install -r requirements.txt

## Set up .env:
DATABASE_URL=postgresql://postgres:password@db:5432/house_db
SECRET_KEY=your-secret-key

## Running with Docker
docker-compose up --build

API will be available at: http://127.0.0.1:8000/docs

## Request body example:
  {
    "median_income": 8.32,
    "house_age": 41,
    "rooms": 6.98,
    "population": 322
  }

## Response:
  {
    "predicted_price": 4.21
  }
  
#Note: The predicted_price is in hundreds of thousands of dollars.


