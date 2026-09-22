<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0B1220&height=210&section=header&text=GlycoTwin%20AI&fontSize=58&fontColor=FFFFFF&animation=fadeIn&fontAlignY=36&desc=An%20Explainable%20Healthcare%20Digital%20Twin%20for%20Proactive%20Glucose%20Risk%20Forecasting&descAlignY=61&descSize=17" width="100%"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=500&size=19&pause=1800&color=0EA5E9&center=true&vCenter=true&width=850&lines=EHR+%2B+Wearables+%E2%86%92+Digital+Twin+%E2%86%92+Prediction+%E2%86%92+Explanation;From+Reactive+Monitoring+to+Predictive+Patient+Intelligence;Built+for+the+Happiest+Health+Digital+Twin+Challenge+2026" />

<br/><br/>

<a href="https://github.com/shivamrajsr07/GlycoTwin-AI">
<img src="https://img.shields.io/badge/Source%20Code-GitHub-111827?style=for-the-badge&logo=github"/>
</a>
<img src="https://img.shields.io/badge/Stage-Prototype%20%2F%20PoC-0EA5E9?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Healthcare-AI-0F766E?style=for-the-badge"/>
<img src="https://img.shields.io/badge/License-MIT-16A34A?style=for-the-badge"/>

<br/><br/>

**Digital Twin Challenge 2026 · Happiest Health × Unstop**

**Team Hacknetic Force · CMR Institute of Technology, Bengaluru**

</div>

---

# 01 — Executive Summary

**GlycoTwin AI** is a healthcare Digital Twin proof-of-concept that combines **static/historical patient information** with **dynamic wearable and IoT time-series data** to maintain a continuously updated representation of a patient's metabolic state.

The prototype focuses on one specific and measurable healthcare outcome:

> **Forecasting a potential glucose spike approximately two hours ahead.**

The system is designed around a complete intelligence loop:

```text
┌──────────────────┐
│  Static EHR Data │
│ Demographics     │
│ Labs             │
│ History          │
└────────┬─────────┘
         │
         │
         ▼
┌────────────────────────┐       ┌──────────────────────────┐
│ Dynamic Wearable Data  │       │ Meal / Activity Signals  │
│ Glucose • HR • HRV     │       │ Carbohydrates • Activity │
│ Sleep • Steps          │       │                          │
└────────────┬───────────┘       └────────────┬─────────────┘
             │                                │
             └───────────────┬────────────────┘
                             ▼
                  ┌──────────────────────┐
                  │    DATA FUSION        │
                  └──────────┬───────────┘
                             ▼
                  ┌──────────────────────┐
                  │ FEATURE ENGINEERING   │
                  └──────────┬───────────┘
                             ▼
                  ┌──────────────────────┐
                  │   PATIENT DIGITAL     │
                  │        TWIN           │
                  └──────────┬───────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
       ┌────────────┐ ┌────────────┐ ┌────────────┐
       │ Prediction │ │ Explain AI │ │ What-If    │
       │   Engine   │ │   / SHAP   │ │ Simulation │
       └─────┬──────┘ └─────┬──────┘ └─────┬──────┘
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                 ┌─────────────────────┐
                 │ Healthcare Dashboard│
                 │ State • Forecast    │
                 │ Drivers • Scenarios │
                 └─────────────────────┘
02 — The Healthcare Problem

Healthcare data is increasingly generated from multiple sources:

Electronic Health Records
Laboratory measurements
Continuous glucose monitoring
Smartwatches and wearable sensors
Sleep trackers
Activity trackers
Patient-reported information
Meal and lifestyle data

The challenge is not simply collecting these signals.

The challenge is connecting them into a continuously updated patient state that can support predictive analysis.

Conventional workflow
Measurement
     ↓
Storage
     ↓
Periodic Review
     ↓
Reactive Interpretation
GlycoTwin AI approach
Continuous Data
      ↓
Data Fusion
      ↓
Digital Twin
      ↓
Predictive Model
      ↓
Explainable Forecast
      ↓
What-If Simulation

This prototype therefore treats the Digital Twin as the central patient-state layer, rather than as another visualization.

03 — Healthcare Use Case
Type 2 Diabetes — Near-Term Glucose Risk Forecasting

For the proof-of-concept, GlycoTwin AI focuses on a localized outcome:

Potential glucose spike approximately two hours ahead

The model receives information representing:

Data category	Signals
Patient profile	Age, sex, BMI
Clinical history	HbA1c, fasting glucose, diabetes duration
Clinical measurements	Blood pressure, cholesterol
Wearable signals	Heart rate, HRV, steps
Recovery	Sleep duration, sleep quality
Lifestyle	Activity level, calories
Meal context	Carbohydrate intake
Temporal context	Time of day, historical trends

The goal is not to build a whole-body Digital Twin within a short prototype cycle.

Instead, GlycoTwin AI deliberately focuses the Digital Twin on one specific physiological outcome, consistent with the challenge's requirement for a localized health event.

04 — Why a Digital Twin?

A conventional ML prediction can answer:

"What is likely to happen?"

A Digital Twin architecture can additionally maintain:

"What is the patient's current modeled state?"

and enable:

"How does the modeled state change under a hypothetical scenario?"

That creates three connected capabilities:

                    DIGITAL TWIN
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
       OBSERVE        PREDICT        SIMULATE
          │              │              │
      Current State   Future State   What-If State

This is the core architectural principle of GlycoTwin AI.

05 — What We Built
5.1 Patient Digital Twin

The Digital Twin combines:

Static patient attributes
Historical clinical context
Current sensor state
Recent time-series history
Temporal features
Model predictions

The resulting state becomes the common input to prediction, explainability, and simulation.

5.2 Dynamic Wearable Stream

The prototype models a continuous stream containing:

Timestamp
Glucose
Heart Rate
HRV
Steps
Sleep Duration
Sleep Quality
Activity Level
Calories
Meal Carbohydrates

This enables the system to represent the patient as a changing time-series rather than as a static record.

5.3 Temporal Feature Engineering

The prediction pipeline can derive:

Lagged glucose values
Rolling glucose statistics
Recent activity trends
Heart-rate trends
HRV changes
Sleep patterns
Meal carbohydrate context
Time-of-day features
Patient-specific features

The objective is to preserve both:

patient context + temporal context

within the prediction pipeline.

06 — AI / ML Architecture
07 — Model Strategy

The prototype is designed around a supervised learning pipeline for near-term glucose forecasting.

Model layer
Scikit-learn
XGBoost
LightGBM
Joblib model persistence
Explainability layer
SHAP-based feature attribution
Transparent fallback when model artifacts are unavailable
Validation principles

To reduce temporal/patient leakage, the intended evaluation strategy uses patient-level separation between training, validation, and test data where applicable.

Evaluation

The project is structured to report appropriate regression metrics such as:

MAE
RMSE
R²

If a classification formulation is used for spike-risk detection, the evaluation can include:

Precision
Recall
F1
ROC-AUC

Final numerical results should be reported here only after the final trained model and evaluation pipeline have been executed.

08 — Explainable AI

A healthcare prediction should not stop at:

Risk = High

The system is designed to expose which modeled signals contributed to the prediction.

Example explanation interface:

Prediction Drivers
────────────────────────────────────

↑ Recent glucose trend
↑ Meal carbohydrate context
↓ Recent physical activity
↓ Sleep duration
↑ Post-meal physiological response

The explainability layer connects the ML prediction to the Digital Twin state so that the dashboard can show:

Patient State
     ↓
Prediction
     ↓
Feature Contribution
     ↓
Human-Readable Explanation
09 — What-If Simulation

The Digital Twin can be modified without changing the original patient record.

Example scenario:

BASELINE
────────────────────────
Meal carbohydrates : 70 g
Additional activity: 0
Sleep duration     : 5.5 h

Simulated scenario:

SCENARIO
────────────────────────
Meal carbohydrates : 50 g
Additional activity: +2,000 steps
Sleep duration     : 6.5 h

The simulation engine creates a modified state:

Baseline Patient
       ↓
Current Digital Twin
       ↓
Baseline Prediction

              +

Scenario Parameters
       ↓
Modified Digital Twin
       ↓
Scenario Prediction

              ↓

     Comparative Output

The important distinction is that this is a simulation of model behavior, not a clinical treatment recommendation.

10 — Clinician Dashboard

The dashboard is designed around four questions:

01 — What is the patient's current modeled state?

Current glucose, heart rate, HRV, activity, sleep, and relevant clinical context.

02 — What could happen next?

Near-term glucose forecast and model output.

03 — Why did the model produce this output?

Feature contribution and explainability.

04 — How does the modeled outcome change under a scenario?

Interactive Digital Twin simulation.

11 — Product Workflow
┌─────────────────────────────────────────────────────────┐
│                    CLINICIAN WORKFLOW                   │
└─────────────────────────────────────────────────────────┘

       Select Patient
             │
             ▼
     Review Patient Profile
             │
             ▼
     Inspect Live / Recent Signals
             │
             ▼
       Open Digital Twin
             │
             ▼
      Generate Forecast
             │
             ▼
      Inspect AI Drivers
             │
             ▼
       Run What-If Scenario
             │
             ▼
       Compare Twin States
12 — Data Strategy & Privacy

The challenge requires teams to use anonymized, open-source, or synthetic datasets because real patient data is restricted by privacy requirements. The challenge specifically identifies sources such as Synthea and MIMIC-IV for EHR-related data and permits simulated/open wearable time-series data.

GlycoTwin AI therefore follows a privacy-first prototype approach:

                 DATA SOURCES
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
   Synthetic       Open Data     Anonymized
       │              │              │
       └──────────────┼──────────────┘
                      ▼
              MODEL DEVELOPMENT
                      │
                      ▼
              DIGITAL TWIN PoC

No real patient-identifying information is required for the prototype.

13 — Technical Stack
Layer	Technology
Frontend	React 19, TypeScript, Vite
UI	Tailwind CSS, Framer Motion, Lucide React
Visualization	Recharts
Backend	Python, FastAPI, Pydantic
Data Processing	Pandas, NumPy
Machine Learning	Scikit-learn, XGBoost, LightGBM
Explainability	SHAP
Model Persistence	Joblib
API	REST
Containerization	Docker, Docker Compose
CI/CD	GitHub Actions
Data	Synthetic / Anonymized / Open
14 — System Components
backend/
│
├── API Layer
│   ├── Patient APIs
│   ├── Prediction APIs
│   ├── Simulation APIs
│   ├── Dashboard APIs
│   └── Health API
│
├── Digital Twin Layer
│   └── Patient state construction
│
├── ML Layer
│   ├── Feature engineering
│   ├── Prediction
│   └── Model artifacts
│
├── Explainability Layer
│   └── SHAP / fallback explanations
│
└── Simulation Layer
    └── What-if scenarios
frontend/
│
├── Dashboard
├── Patients
├── Digital Twin
├── Predictions
├── Simulation
├── API Services
├── Shared Components
└── Type Definitions
15 — API Surface
Method	Endpoint	Description
GET	/api/health	Backend health
GET	/api/patients	Retrieve patient list
GET	/api/patients/{id}	Retrieve patient profile
GET	/api/patients/{id}/timeline	Retrieve time-series history
GET	/api/patients/{id}/twin	Retrieve Digital Twin state
GET	/api/patients/{id}/prediction	Generate/retrieve prediction
GET	/api/patients/{id}/explanation	Retrieve prediction explanation
POST	/api/simulation	Run what-if scenario
GET	/api/dashboard/summary	Dashboard-level summary
16 — Repository Structure
glycotwin-ai/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── services/
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
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── pages/
│   │   ├── services/
│   │   └── types/
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
├── .gitignore
└── README.md
17 — Demo
🎥 Prototype Demonstration

2–5 minute demonstration video required for the challenge submission.

▶️ Watch the Demo

[ADD YOUR YOUTUBE / VIDEO LINK HERE]

Recommended demonstration sequence:

00:00  Problem & use case
00:20  Patient selection
00:35  EHR + historical context
00:55  Dynamic wearable signals
01:15  Digital Twin state
01:40  Glucose prediction
02:05  Explainable AI
02:30  What-if simulation
03:00  Architecture & technology
03:30  Healthcare impact
18 — Application Screenshots

Replace these placeholders with screenshots from the actual running application.

Dashboard	Digital Twin
docs/assets/dashboard.png	docs/assets/digital-twin.png
Prediction	Simulation
docs/assets/prediction.png	docs/assets/simulation.png
19 — Architecture Documentation
📐 Architecture PDF

View Architecture Document

The architecture document covers:

Data sources
Data fusion
Feature engineering
Digital Twin state
ML pipeline
Explainability
Simulation
Frontend/backend architecture
📑 Presentation

View Project Presentation

20 — Quick Start
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

Open a second terminal:

cd frontend

npm install

npm run dev

Frontend:

http://localhost:5173
Docker
docker compose up --build

Stop:

docker compose down
21 — Reproducibility

A reviewer should be able to understand the complete path from data to prediction:

Synthetic / Open Data
        ↓
Data Generation / Loading
        ↓
Preprocessing
        ↓
Feature Engineering
        ↓
Train / Validation / Test
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Model Artifact
        ↓
FastAPI Prediction Service
        ↓
React Dashboard

The repository is structured so that the ML, backend, and frontend layers can be developed and evaluated independently.

22 — Challenge Requirement Mapping

The official challenge requires the prototype to demonstrate the fusion of static/historical EHR data and dynamic/real-time wearable or IoT time-series data, produce an algorithmic prediction of a localized adverse health event, and present a conceptual doctor-facing dashboard.

Challenge Requirement	GlycoTwin AI Implementation
Static / historical data	Synthetic EHR
Demographics	Patient profile
Historical clinical data	Diagnosis, labs, history
Dynamic data	Wearable / IoT time series
HRV	Dynamic sensor feature
Glucose	Dynamic metabolic signal
Sleep	Dynamic recovery signal
Steps	Dynamic activity signal
Localized outcome	Near-term glucose spike forecasting
Algorithmic model	ML prediction pipeline
Digital Twin	Patient-state engine
Explainability	SHAP-based attribution
Doctor dashboard	React healthcare dashboard
Scenario simulation	What-if Digital Twin engine
Privacy	Synthetic / anonymized / open data
23 — Expected Prototype Outcome

The completed prototype demonstrates a complete technical path:

                 PATIENT
                    │
                    ▼
          ┌───────────────────┐
          │ Static EHR        │
          │ +                 │
          │ Dynamic Wearables │
          └─────────┬─────────┘
                    │
                    ▼
             DATA FUSION
                    │
                    ▼
           DIGITAL TWIN STATE
                    │
             ┌──────┼──────┐
             ▼      ▼      ▼
          PREDICT EXPLAIN SIMULATE
             │      │      │
             └──────┼──────┘
                    ▼
          CLINICIAN DASHBOARD

The intended result is not merely a prediction model.

It is a working Digital Twin workflow connecting patient state, forecasting, explainability, and simulation in one system.

24 — Responsible AI & Medical Safety

GlycoTwin AI is a research and hackathon proof-of-concept.

It is not a medical device.

It does not provide diagnosis, treatment, or individualized medical advice.

Model outputs are predictions generated from simulated/open/anonymized data and should not be interpreted as clinical recommendations.

Any future clinical deployment would require appropriate:

Clinical validation
External validation
Safety evaluation
Bias assessment
Data governance
Privacy controls
Regulatory review
Human oversight
25 — Limitations

The current prototype has several deliberate limitations:

The primary data environment is synthetic, anonymized, or open rather than real-time clinical infrastructure.
Wearable signals are simulated/open-source rather than connected to production medical devices.
The glucose forecasting problem represents a focused Digital Twin use case rather than a complete physiological replica.
Model performance depends on the quality and representativeness of the underlying dataset.
What-if simulation represents model-based scenario analysis and is not a clinical intervention simulator.

These limitations define the boundary between the current proof-of-concept and future clinical research.

26 — Future Development
CURRENT PoC
     │
     ├── EHR + Wearable Fusion
     ├── Digital Twin State
     ├── Glucose Forecasting
     ├── Explainable AI
     └── What-If Simulation
              │
              ▼
NEXT STAGE
     │
     ├── Real wearable integrations
     ├── Continuous glucose monitoring
     ├── Personalized model adaptation
     ├── Longer longitudinal histories
     ├── Uncertainty-aware prediction
     └── Improved temporal models
              │
              ▼
RESEARCH DIRECTION
     │
     ├── Multimodal physiological modeling
     ├── Temporal Transformers
     ├── Federated learning
     ├── Privacy-preserving learning
     ├── Causal inference
     └── Clinical validation
27 — Team
Hacknetic Force

Institution: CMR Institute of Technology, Bengaluru
Challenge: Digital Twin Challenge 2026
Project: GlycoTwin AI

Member	Responsibility
Shivam Raj	Digital Twin Architecture · AI/ML · Full-Stack Development
28 — Open Source

This project is released under the MIT License.

See LICENSE for details.

29 — References
Challenge
Happiest Health — Digital Twin Challenge 2026
Unstop — Digital Twin Challenge 2026
Data / Healthcare
Synthea — Synthetic Patient Data
MIMIC-IV — PhysioNet
Engineering
FastAPI
React
Scikit-learn
XGBoost
LightGBM
SHAP

Exact dataset versions, source URLs, and access dates should be added when they are used in the final implementation.
GlycoTwin AI
Observe → Model → Predict → Explain → Simulate
A focused Digital Twin proof-of-concept for proactive healthcare intelligence.
