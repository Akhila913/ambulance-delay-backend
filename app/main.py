from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import DelayRequest, DelayResponse
from app.predictor import predict_delay
from app.geo import is_within_bengaluru
from app.recommender import recommend_hospital
from app.schemas import RecommendRequest, RecommendResponse


app = FastAPI(title="Ambulance Delay Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://ambulance-delay-frontend.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

@app.post("/recommend-hospital", response_model=RecommendResponse)
def recommend(req: RecommendRequest):

    if not is_within_bengaluru(req.lat, req.lon):
        return {
            "hospital_name": "N/A",
            "eta_minutes": -1,
            "predicted_delay": -1,
            "distance_km": -1
        }

    best, _ = recommend_hospital(
        req.lat,
        req.lon,
        req.hour,
        req.is_weekend
    )

    return {
        "hospital_name": best["hospital_name"],
        "eta_minutes": best["eta_minutes"],
        "predicted_delay": best["predicted_delay"],
        "distance_km": best["distance_km"]
    }
