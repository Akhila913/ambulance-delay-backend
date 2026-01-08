from pydantic import BaseModel

class DelayRequest(BaseModel):
    distance_km: float
    hour: int
    is_weekend: int


class DelayResponse(BaseModel):
    predicted_delay: float
