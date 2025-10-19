# 🧠 Insurance Premium Predictor

An interactive web application that predicts **insurance premium risk levels** (High, Medium, or Low) based on user inputs such as age, weight, height, income, city, occupation, and smoking habits.  

This project uses **React (frontend)** and **FastAPI (backend)** with a trained **Machine Learning model** (RandomForestClassifier with preprocessing pipeline).

---

## ⚙️ Tech Stack

- **Frontend:** React + Tailwind CSS  
- **Backend:** FastAPI (Python 3.10+)  
- **Model:** Scikit-learn Pipeline (Pickle format)  
- **Communication:** REST API (Axios)  

---

## 🧩 Project Structure

insurance-premium-predictor/
│
├── backend/
│ ├── app.py # FastAPI backend server
│ ├── insurance_model.pkl # Trained ML model
│ └── requirements.txt # Backend dependencies
│
├── frontend/
│ ├── src/
│ │ ├── App.js # Main React entry
│ │ ├── Form.jsx # Input form component
│ │ ├── Result.jsx # Output result display
│ │ ├── api.js # Axios-based API handler
│ │ └── index.css # Tailwind setup
│ ├── package.json
│ └── tailwind.config.js
│
└── README.md

yaml
Copy code

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/insurance-premium-predictor.git
cd insurance-premium-predictor
2️⃣ Backend Setup (FastAPI)
Go to the backend folder:

bash
Copy code
cd backend
Create a virtual environment and install dependencies:

bash
Copy code
python -m venv venv
venv\Scripts\activate   # (Windows)
# OR
source venv/bin/activate   # (Mac/Linux)

pip install -r requirements.txt
Run the FastAPI server:

bash
Copy code
uvicorn app:app --reload
Backend runs by default at:
👉 http://127.0.0.1:8000

Test the API docs:
📄 http://127.0.0.1:8000/docs

3️⃣ Frontend Setup (React)
Go to the frontend folder:

bash
Copy code
cd ../frontend
npm install
Start the React development server:

bash
Copy code
npm start
Frontend runs by default at:
👉 http://localhost:3000

🧠 Model Overview
The trained model (insurance_model.pkl) uses a ColumnTransformer pipeline:

Numerical features: ['bmi', 'income_lpa']

Categorical features: ['age_group', 'lifeStyle_risk', 'occupation', 'cities_tier']

Encoded using OneHotEncoder(handle_unknown='ignore')

Model: RandomForestClassifier(n_estimators=100, random_state=42)

📡 API Endpoint
POST /predict
Predicts insurance premium risk level.

Request Body:

json
Copy code
{
  "age": 40,
  "weight": 78,
  "height": 170,
  "income_lpa": 10,
  "smoker": true,
  "city": "Pune",
  "occupation": "private_job"
}
Response Example:

json
Copy code
{
  "predicted_category": "high_risk"
}
🧪 Example Run
Start FastAPI:

lua
Copy code
uvicorn app:app --reload
Start React app:

sql
Copy code
npm start
Open browser at:
👉 http://localhost:3000

Enter user details and click Predict
→ Get real-time prediction from the ML model!

🧰 Scripts
Frontend:
bash
Copy code
npm start       # Run development server
npm run build   # Create production build
npm test        # Run unit tests
Backend:
bash
Copy code
uvicorn app:app --reload   # Run API locally
🧾 License
This project is open-source and available under the MIT License.