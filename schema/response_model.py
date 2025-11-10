from pydentic import Basemodel,Field
from fastapi import FastAPI
from typing import Dict

class prediction_model(Basemodel):

    predicted_catagory: str = Field(...,description="this is predcition your insurance stauts",example="high")

    confidence : float = Field(...,
                               description="this is provided confidence of prediction value ",
                               example= 0.0707
                               )
    class_probability:dict[str,float] = Field(
        ...,description="this is given return str and float ", example= "low : 0901"
    )




