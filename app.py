from fastapi import FastAPI
import inference
from api.models.iris import PredictRequest, PredictResponse

app = FastAPI()
model = inference.load_model("iris_model.joblib")


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    data = [
        request.sepal_length,
        request.sepal_width,
        request.petal_length,
        request.petal_width,
    ]
    prediction = inference.predict(model, data)
    return PredictResponse(prediction=prediction)
