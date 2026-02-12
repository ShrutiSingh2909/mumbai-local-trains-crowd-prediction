Mumbai Local Train Crowd Density Prediction System

A production-ready Machine Learning + Streamlit dashboard that predicts crowd density across major Mumbai local train stations and provides intelligent travel-time recommendations.

App Structure

This dashboard provides:

1. Crowd Prediction Panel – Select station, day, and hour to generate real-time ML-based crowd predictions. Displays crowd levels (Low / Medium / High / Extreme) with color-coded indicators and smart travel recommendations.
2. Risk Flagging System – Automatically detects High and Extreme crowd conditions, highlights peak-risk hours, and provides safety-aware recommendations for better travel planning.
3. Data Insights – Interactive visual analysis including crowd distribution, station-wise comparisons, peak-hour trends, and weekend
4. Model Performance – Evaluation metrics including accuracy, precision, recall, F1-score, confusion matrix, and detailed classification report.
5. Feature Importance – Displays top contributing features using Random Forest importance scores for model interpretability.

All visualizations use Plotly and Seaborn for interactive, production-grade insights.

Setup & Installation
Prerequisites

Python 3.8 or higher
pip package manager

Installation Steps

Install dependencies
   pip install -r requirements.txt

Run the Streamlit application
   streamlit run app/app.py

Access the dashboard
The app will automatically open in your browser.
Default URL: http://localhost:8501

Features
Data Creation
Synthetic dataset simulating Mumbai local train crowd behavior

Includes: Station / Line / Hour / Day of week / Peak hour flag / Weekend flag 

Feature Engineering 
Engineered features include:
Peak hour flag
Weekend flag
Office hour flag
Morning vs Evening flag
Encoded station, line, and day features

Model
Algorithm: Random Forest Classifier
Hyperparameters:
n_estimators = 150
max_depth = 8
min_samples_leaf = 5
class_weight = "balanced"

Validation: Train-test split with stratification

Performance Metrics: Accuracy, Precision, Recall, F1-score, Confusion Matrix, Classification Report

Model Comparison:
Logistic Regression
Random Forest Classifier
Final Selection: Random Forest (higher accuracy, better recall for Extreme class, improved stability on encoded features)

Risk Alert System
Binary Risk Flag:
1 → High / Extreme crowd
0 → Low / Medium crowd
Enables:
Early warning system
Peak-hour risk identification
Safety-focused travel suggestions

Travel Recommendation Engine
Provides:
Best low-crowd hours
Off-peak alternatives
Safer travel windows

Interactive Elements
Station, day, and hour selection panel
Real-time crowd prediction
Color-coded crowd level display
Dynamic risk alerts
Interactive Plotly visualizations
Responsive dashboard layout

Usage
Navigation
1. Sidebar: Select station, day, and hour
2. Prediction Panel: View crowd level & recommendation
3. Insights Section: Analyze crowd distribution & comparisons
4. Model Performance: Evaluate classification metrics
5. Feature Importance: Understand key crowd drivers

Making Predictions
1. Select station
2. Select day of week
3. Select hour
4. Click "Predict Crowd Level"
5. View crowd class, risk alert, and travel recommendation

Technical Details
Pipeline: End-to-end ML workflow (Data → Feature Engineering → Training → Deployment)
Visualization: Plotly + Seaborn
Deployment: Streamlit-based real-time dashboard
Model Saving: joblib
Version Control: Git-managed project

File Structure
mumbai-local-train-crowd-density-prediction/
│
├── README.md
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_data_creation_and_assumptions.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training_and_evaluation.ipynb
│   └── 04_insights_and_recommendations.ipynb
├── app/
│   └── app.py
├── src/
│   ├── feature_engineering.py
│   ├── train_model.py
│   └── evaluate_model.py
├── outputs/
│   ├── plots/
│   └── reports/
├── requirements.txt
└── .gitignore

Dependencies
Key packages:
streamlit → Dashboard framework
pandas → Data manipulation
numpy → Numerical processing
scikit-learn → Machine learning
seaborn / matplotlib → Visualization
plotly → Interactive charts
joblib → Model persistence

Notes
Model is trained locally
Synthetic dataset based on realistic assumptions
No external APIs required
Fully reproducible project
Production-ready structure

Use Cases
Public transport planning
Crowd risk monitoring
Smart city research
Travel-time optimization
Crowd simulation analysis

