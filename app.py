from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, computed_field,field_validator
from typing import Literal, Annotated
from model.predict import predict_output
from schema.user_input import Userinput
# ----------------------------------------------------------
# Initialize FastAPI app
# ----------------------------------------------------------
app = FastAPI(title="Insurance Premium Predictor API")

# ----------------------------------------------------------
# Enable CORS for frontend connection (React)
# ----------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict")
def predict_insurance_premium(user_input: Userinput):
    try:
        user_input = {
            "bmi": user_input.bmi,
            "income_lpa": user_input.income_lpa,
            "age_group": user_input.age_group,
            "lifeStyle_risk": user_input.lifeStyle_risk,
            "occupation": user_input.occupation,
            "cities_tier": user_input.cities_tier
          }  

        prediction = predict_output([user_input])

        return JSONResponse(status_code=200, content={
            "predicted_insurance_premium": str(prediction)
        })

    except ValueError as e:
        return JSONResponse(status_code=400, content={"error": str(e)})


# ----------------------------------------------------------
# Health Check Root Route
# ----------------------------------------------------------
@app.get("/")
def root():
    return {"message": "Insurance Premium Predictor API is running!"}

@app.get("/health")
def health():
    return{
        'status':'OK'
    }