from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime, timezone
from app.database import Base

class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key=True, index=True)
    lat = Column(Float)
    lon = Column(Float)
    hour = Column(Integer)
    is_weekend = Column(Integer)
    predicted_delay = Column(Float)
    eta_minutes = Column(Float)
    hospital_name = Column(String)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))