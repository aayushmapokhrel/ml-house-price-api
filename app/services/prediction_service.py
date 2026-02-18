from app.models.prediction import Prediction

def save_prediction(db, input_data, prediction):
    db_obj = Prediction(
        median_income=input_data.median_income,
        house_age=input_data.house_age,
        rooms=input_data.rooms,
        population=input_data.population,
        prediction=prediction
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
