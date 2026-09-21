<div align="center">

# 🧬 GlycoTwin AI

### Explainable Digital Twin for Proactive Glucose Spike Risk Forecasting

<p>
  <strong>Transforming EHR + wearable data into an intelligent, continuously evolving patient Digital Twin.</strong>
</p>

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/shivamrajsr07/GlycoTwin-AI)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br/>

### 🏥 Digital Twin Challenge 2026
**Happiest Health × Unstop**

</div>

---

# 🚀 Overview

**GlycoTwin AI** is an explainable healthcare Digital Twin prototype designed to model a patient's evolving metabolic state by combining **static EHR information** with **dynamic wearable and IoT signals**.

The system creates a virtual representation of a patient's current physiological state and uses machine learning to forecast a potential **glucose spike approximately two hours ahead**.

Instead of simply displaying historical health data, GlycoTwin AI follows a continuous intelligence loop:

```text
Patient Data
     ↓
Data Fusion
     ↓
Feature Engineering
     ↓
Digital Twin State
     ↓
Prediction
     ↓
Explainable AI
     ↓
What-If Simulation
     ↓
Updated Patient Insight
🎯 Problem Statement

Patients with chronic metabolic conditions generate large amounts of health data from clinical records, wearable devices, activity trackers, sleep monitors, and glucose sensors.

However, these signals are often viewed independently.

Traditional workflow:

Periodic Measurements
        ↓
Clinical Review
        ↓
Reactive Decision

GlycoTwin AI explores a predictive approach:

Continuous Signals
        ↓
Patient Digital Twin
        ↓
Predictive Model
        ↓
Explainable Forecast
        ↓
Scenario Simulation

The prototype focuses on forecasting a localized adverse health event:

Potential glucose spike approximately two hours ahead.

💡 Core Innovation

GlycoTwin AI combines two types of patient information.

🧬 Static / Historical Data
Demographics
BMI
HbA1c
Fasting glucose
Blood pressure
Cholesterol
Diabetes duration
Family history
Medication information
⌚ Dynamic / Time-Series Data
Glucose
Heart rate
HRV
Steps
Sleep duration
Sleep quality
Activity level
Calories
Meal carbohydrates

These signals are fused to maintain a continuously updated Digital Twin state.

🧠 System Architecture
🔥 Key Features
Feature	Description
🧬 Digital Patient Twin	Continuously represents the patient's current physiological state
📈 Glucose Forecasting	Predicts potential glucose spikes approximately two hours ahead
⌚ Wearable Intelligence	Processes simulated wearable and IoT time-series signals
🔍 Explainable AI	Identifies important factors contributing to model predictions
🧪 What-If Simulation	Tests hypothetical changes to meals, activity, and sleep
🩺 Doctor Dashboard	Provides patient state, trends, forecasts, explanations, and scenarios
📊 Temporal Analytics	Uses historical, lagged, rolling, and time-based features
🔐 Privacy-First Prototype	Designed around synthetic/anonymized/open data
🧬 Digital Twin

The Digital Twin acts as the central intelligence layer.

                  PATIENT
                     │
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
   STATIC DATA              DYNAMIC DATA
        │                         │
        ▼                         ▼
      EHR                    WEARABLES
      Labs                    Glucose
      BMI                     HR / HRV
      History                 Sleep
      Medication             Activity
                              Meals
        │                         │
        └────────────┬────────────┘
                     ▼
              DATA FUSION
                     │
                     ▼
             FEATURE ENGINE
                     │
                     ▼
            🧬 DIGITAL TWIN
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   Prediction   Explanation   Simulation
        │            │            │
        └────────────┼────────────┘
                     ▼
             DOCTOR DASHBOARD
🤖 Machine Learning Pipeline
Feature Engineering

The model pipeline can incorporate:

Current glucose
Previous glucose values
Rolling glucose statistics
Heart-rate trends
HRV changes
Recent physical activity
Sleep duration
Sleep quality
Meal carbohydrates
Time of day
Activity level
Patient-specific characteristics
🔮 Prediction Engine

The prediction engine evaluates the current Digital Twin state and generates a forecast.

Example:

Current Patient State
─────────────────────────────
Glucose             142 mg/dL
Heart Rate          84 bpm
HRV                 42 ms
Sleep               5.8 hours
Steps               3,420
Meal Carbohydrates  65 g
─────────────────────────────
              ↓
       DIGITAL TWIN
              ↓
       ML PREDICTION
              ↓
       ~2 HOUR FORECAST

The system can expose model outputs through the backend API and visualize them through the clinician dashboard.

🔍 Explainable AI

A predictive healthcare system should provide more than a prediction.

GlycoTwin AI is designed to expose the factors contributing to a prediction.

Example:

Prediction Drivers
─────────────────────────────
↑ Recent glucose trend
↑ Meal carbohydrate intake
↓ Recent physical activity
↓ Sleep duration
↑ Post-meal physiological response

The explainability layer is designed around SHAP-based feature attribution, with a transparent fallback when trained model artifacts are unavailable.

🧪 What-If Simulation

The Digital Twin can be used to explore hypothetical scenarios.

Example baseline:

Meal Carbohydrates : 70g
Additional Steps   : 0
Sleep Duration     : 5.5h

Prediction
     ↓
Elevated Risk

Example scenario:

Meal Carbohydrates : -20g
Additional Steps   : +2,000
Sleep Duration     : +1h

The system then compares the baseline and simulated states.

             BASELINE
                 │
                 ▼
          Digital Twin
                 │
                 ▼
            Prediction
                 │
        ┌────────┴────────┐
        │                 │
        ▼                 ▼
     Scenario A       Scenario B
        │                 │
        ▼                 ▼
   Prediction        Prediction
        │                 │
        └────────┬────────┘
                 ▼
          Scenario Delta

This enables an interactive exploration of how changes in simulated inputs affect the model's output.

🩺 Doctor Dashboard

The conceptual dashboard is designed around four questions:

01 — What is happening?

Current physiological state.

02 — What could happen next?

Predicted glucose trajectory.

03 — Why?

Important model features and prediction drivers.

04 — What if the scenario changes?

Interactive Digital Twin simulation.

📊 Data Architecture
Static EHR
Field	Example
Patient ID	PT-001
Age	52
Sex	Female
BMI	28.4
HbA1c	7.2%
Fasting Glucose	132 mg/dL
Blood Pressure	138/86
Diabetes Duration	6 years
Family History	Yes
Medication	Simulated
Dynamic Signals
Signal	Purpose
Glucose	Current metabolic state
Heart Rate	Physiological response
HRV	Autonomic-state signal
Steps	Physical activity
Sleep	Recovery indicator
Activity	Movement pattern
Calories	Energy expenditure
Meal Carbs	Potential glucose driver
🖥️ Dashboard Preview

Add real screenshots/GIFs here once the frontend is running.

Main Dashboard

Digital Twin

Prediction Analytics

What-If Simulation

🛠️ Technology Stack
Frontend
React 19
TypeScript
Vite
Tailwind CSS
Recharts
Framer Motion
Lucide React
Axios
Backend
Python 3.11+
FastAPI
Pydantic
Pandas
NumPy
Scikit-learn
XGBoost
LightGBM
SHAP
Joblib
Infrastructure
Docker
Docker Compose
GitHub Actions
REST API
Synthetic Data Pipeline
📁 Project Structure
glycotwin-ai/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── patients.py
│   │   │   ├── predictions.py
│   │   │   ├── simulation.py
│   │   │   ├── dashboard.py
│   │   │   └── health.py
│   │   │
│   │   ├── core/
│   │   ├── models/
│   │   ├── services/
│   │   │   ├── digital_twin.py
│   │   │   ├── prediction.py
│   │   │   ├── feature_engineering.py
│   │   │   ├── explainability.py
│   │   │   └── simulation.py
│   │   └── utils/
│   │
│   ├── data/
│   │   ├── raw/
│   │   ├── processed/
│   │   └── generate_data.py
│   │
│   ├── models/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── hooks/
│   │   └── types/
│   │
│   ├── public/
│   └── package.json
│
├── docs/
│   ├── architecture.pdf
│   ├── presentation.pdf
│   └── assets/
│
├── .github/
│   └── workflows/
│
├── docker-compose.yml
├── LICENSE
└── README.md
🔌 API
Endpoint	Purpose
GET /api/health	Backend health
GET /api/patients	Patient list
GET /api/patients/{patient_id}	Patient profile
GET /api/patients/{patient_id}/timeline	Time-series data
GET /api/patients/{patient_id}/twin	Digital Twin state
GET /api/patients/{patient_id}/prediction	Prediction
GET /api/patients/{patient_id}/explanation	Explainability
POST /api/simulation	What-if simulation
GET /api/dashboard/summary	Dashboard summary
🚀 Getting Started
Prerequisites
Python 3.11+
Node.js 20+
npm
Git
Docker
Clone
git clone https://github.com/shivamrajsr07/GlycoTwin-AI.git
cd GlycoTwin-AI
Backend
cd backend

python -m venv .venv

.venv\Scripts\Activate.ps1

pip install -r requirements.txt

uvicorn app.main:app --reload

Backend:

http://localhost:8000

API documentation:

http://localhost:8000/docs
Frontend

Open another terminal:

cd frontend

npm install

npm run dev

Frontend:

http://localhost:5173
🐳 Docker

Run the complete application:

docker compose up --build

Stop:

docker compose down
🎬 Recommended Demo Flow
01 → Select Patient
        ↓
02 → View Synthetic EHR
        ↓
03 → Observe Wearable Stream
        ↓
04 → Open Digital Twin
        ↓
05 → Generate Glucose Forecast
        ↓
06 → Inspect AI Explanation
        ↓
07 → Modify Scenario
        ↓
08 → Run What-If Simulation
        ↓
09 → Compare Results
🏆 Digital Twin Challenge 2026 Alignment
Challenge Requirement	GlycoTwin AI
Static EHR Data	✅
Demographics	✅
Diagnoses	✅
Laboratory Measurements	✅
Dynamic Wearable Data	✅
IoT Time-Series	✅
Algorithmic Model	✅
Localized Health Event	✅
Digital Twin	✅
Explainable AI	✅
Doctor Dashboard	✅
What-If Simulation	✅
Synthetic / Anonymized Data	✅
🔐 Privacy & Data Ethics

GlycoTwin AI is designed as a research and hackathon prototype.

The prototype should use:

Synthetic data
Anonymized data
Open datasets where appropriate

No real patient-identifying information should be included in this repository.

⚠️ Medical Disclaimer

GlycoTwin AI is a research prototype created for the Digital Twin Challenge 2026. It is not a medical device and does not provide medical diagnosis or treatment. Predictions are model outputs and should not be used as a substitute for professional clinical judgment.

🌱 Future Roadmap
                    GlycoTwin AI
                         │
                         ▼
              Current Prototype
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
   Wearables        Explainability    Simulation
        │
        ▼
       FUTURE
        │
        ├── Real wearable integrations
        ├── Continuous glucose monitoring
        ├── Personalized model adaptation
        ├── Multimodal health signals
        ├── Longitudinal patient modeling
        ├── Temporal Transformer models
        ├── Uncertainty-aware prediction
        ├── Federated learning
        ├── Privacy-preserving AI
        └── Clinical workflow integration
📚 References
Happiest Health — Digital Twin Challenge 2026
Synthea — Synthetic Patient Data
MIMIC-IV — PhysioNet
FastAPI Documentation
React Documentation
Scikit-learn Documentation
SHAP Documentation

Add the exact source URLs and access dates used in the final implementation and submission.

👥 Team
Hacknetic Force

Project: GlycoTwin AI
Challenge: Digital Twin Challenge 2026
Institution: CMR Institute of Technology, Bengaluru

Member	Contribution
Shivam Raj	AI/ML • Full-Stack Development • Digital Twin Architecture
Team Member	—
Team Member	—
Team Member	—
📄 Deliverables
📦 GlycoTwin AI
│
├── 💻 Source Code
│   ├── Frontend
│   ├── Backend
│   ├── ML Pipeline
│   └── Data Generation
│
├── 📚 Documentation
│   ├── Architecture
│   ├── Presentation
│   ├── Demo Script
│   └── References
│
└── 🚀 Deployment
    ├── Docker
    └── CI/CD
<div align="center">
🧬 GlycoTwin AI
Data → Digital Twin → Prediction → Explanation → Simulation
<br/>

Built for Digital Twin Challenge 2026

<br/>

⭐ Star the repository if you find the project interesting

<br/>

</div> ```
