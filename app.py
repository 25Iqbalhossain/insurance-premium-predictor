from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pandas as pd
import pickle

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

# ----------------------------------------------------------
# Load trained model
# ----------------------------------------------------------
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# ----------------------------------------------------------
# City tiers
# ----------------------------------------------------------
tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Surat", "Pune"]
tier_2_cities = [
    "Ahmedabad", "Jaipur", "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane", "Bhopal",
    "Visakhapatnam", "Pimpri-Chinchwad", "Patna", "Vadodara", "Ghaziabad", "Ludhiana",
    "Agra", "Nashik", "Faridabad", "Meerut", "Rajkot", "Kalyan-Dombivli",
    "Vasai-Virar", "Varanasi", "Srinagar"
]

# ----------------------------------------------------------
# Pydantic Model for Input Validation
# ----------------------------------------------------------
class Userinput(BaseModel):
    age: Annotated[int, Field(..., ge=0, le=120, description="Age of the person in years")]
    weight: Annotated[float, Field(..., ge=0, le=500, description="Weight of the person in kgs")]
    height: Annotated[float, Field(..., ge=0, le=300, description="Height of the person in cms")]
    income_lpa: Annotated[float, Field(..., ge=0, le=1000, description="Income in lakhs per annum")]
    smoker: Annotated[bool, Field(..., description="Whether the person is a smoker or not")]
    city: Annotated[str, Field(..., description="City of the person")]
    occupation: Annotated[
        Literal[
            "retired", "freelancer", "student", "government_job",
            "business_owner", "unemployed", "private_job"
        ],
        Field(..., description="Occupation of the person")
    ]

    @computed_field
    def bmi(self) -> float:
        # ✅ Correct BMI formula (height converted to meters)
        return self.weight / ((self.height / 100) ** 2)

    @computed_field
    def lifeStyle_risk(self) -> str:
        # ✅ Ensure values match the model’s trained categories
        if self.smoker and self.bmi > 30:
            return "high_risk"
        elif self.smoker or self.bmi > 27:
            return "medium_risk"
        else:
            return "low_risk"

    @computed_field
    def age_group(self) -> str:
        if self.age < 18:
            return "child"
        elif 18 <= self.age < 65:
            return "adult"
        else:
            return "senior"

    @computed_field
    def cities_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3

# ----------------------------------------------------------
# Prediction Endpoint
# ----------------------------------------------------------
@app.post("/predict")
def predict_insurance_premium(user_input: Userinput):
    try:
        input_df = pd.DataFrame([{
            "bmi": user_input.bmi,
            "income_lpa": user_input.income_lpa,
            "age_group": user_input.age_group,
            "lifeStyle_risk": user_input.lifeStyle_risk,
            "occupation": user_input.occupation,
            "cities_tier": user_input.cities_tier
        }])  # ✅ Same order as training

        prediction = model.predict(input_df)[0]

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
