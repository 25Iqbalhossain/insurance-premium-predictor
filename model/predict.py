import pandas as pd
import pickle
from pathlib import Path

# Load the model relative to this file's directory to avoid CWD issues
MODEL_PATH = Path(__file__).resolve().parent / "model.pkl"
with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

def predict_output(user_input:dict):
    input_df = pd.DataFrame(user_input)
    output = model.predict(input_df)[0]
    return output

MODEL_VESRION = "1.0.0" 
