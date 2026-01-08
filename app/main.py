from fastapi import FastAPI
from app.schemas import DelayRequest, DelayResponse
from app.predictor import predict_delay

app = FastAPI(title="Ambulance Delay Prediction API")


@app.get("/")
def health_check():
    return {"status": "API is running"}


@app.post("/predict-delay", response_model=DelayResponse)
def predict(request: DelayRequest):
    delay = predict_delay(
        distance_km=request.distance_km,
        hour=request.hour,
        is_weekend=request.is_weekend
    )
    return {"predicted_delay": delay}
