# ----------------------------------------------------------
# Pydantic Model for Input Validation
# --------------------------------------
from pydantic import BaseModel, Field, computed_field,field_validator
from typing import Literal, Annotated, Any
import pandas as pd
from config.citi_tiers import tier_1_cities,tier_2_cities



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
    @field_validator('city', mode='before')
    @classmethod
    def normalize_city(cls, v: Any) -> str:
        if v is None:
            raise ValueError('city is required')
        if not isinstance(v, str):
            v = str(v)
        v = v.strip()
        if not v:
            raise ValueError('city cannot be empty')
        return v.title()

    @field_validator('smoker', mode='before')
    @classmethod
    def coerce_smoker(cls, v: Any) -> bool:
        if isinstance(v, bool):
            return v
        if v is None:
            raise ValueError('smoker is required')
        if isinstance(v, (int, float)):
            return bool(v)
        s = str(v).strip().lower()
        if s in {"true", "1", "yes", "y", "on"}:
            return True
        if s in {"false", "0", "no", "n", "off"}:
            return False
        raise ValueError("smoker must be a boolean (true/false)")
