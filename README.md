# MedRoute - Backend API

This repository contains the backend service for **MedRoute**, an ML-driven emergency ETA advisory system that estimates ambulance travel delay and recommends the fastest reachable hospital under varying traffic conditions.

The backend is built using **FastAPI** and integrates a trained machine learning regression model with geospatial distance computation and regional validation logic.

This project demonstrates ETA-based emergency routing concepts using **simulated traffic conditions**.

---

## Live Demo

 **Frontend Application:**  
https://medroute-beryl.vercel.app

> The frontend provides an interactive map-based interface for selecting emergency locations, visualizing hospital routes, and interpreting ETA predictions.

---

## System Overview

The backend is responsible for:

- Predicting **traffic-induced delay** using a trained ML regression model  
- Computing **ideal travel time** based on geospatial distance  
- Calculating **Estimated Time of Arrival (ETA)** as:  
  **ETA = Ideal Travel Time + Predicted Delay**
- Recommending the hospital with the **minimum ETA**
- Enforcing **regional validation** (Bengaluru-only support)

All predictions are **simulated estimates** and do not rely on real-time traffic APIs.

---

##  Tech Stack

- Python  
- FastAPI  
- Scikit-learn  
- Pandas  
- NumPy  
- Joblib  
- Geospatial distance computation (Haversine)

---

## API Endpoints

### POST `/recommend-hospital`

Returns the recommended hospital and ETA for a given emergency location.

**Request Body**
```json
{
  "lat": 12.9716,
  "lon": 77.5946,
  "hour": 14,
  "is_weekend": 0
}
```

### GET /hospitals

Returns a list of emergency-capable hospitals used by the system.

---

## Design Considerations

- This system is advisory, not autonomous

- No real-time traffic data is used

- All outputs are explainable and deterministic

- ML is used only to model traffic-induced delay, not routing

- Regional constraints prevent misuse outside supported areas

---

## Limitations & Future Work

- Integrate real-time traffic APIs (Google Maps / OSRM)

- Extend support beyond Bengaluru

- Add historical traffic datasets for improved realism

- Explore reinforcement learning for adaptive routing

---

## Related Repositories

### Frontend Repository:
https://github.com/Akhila913/ambulance-delay-frontend
