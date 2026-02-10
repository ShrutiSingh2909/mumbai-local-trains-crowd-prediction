import streamlit as st
import pandas as pd
import os
import joblib

# -----------------------------
# App Config
# -----------------------------
st.set_page_config(
    page_title="Mumbai Local Crowd Predictor",
    layout="centered"
)

st.title("🚆 Mumbai Local Train Crowd Predictor")

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR, "data", "processed", "engineered_features.csv"
)

MODEL_PATH = os.path.join(
    BASE_DIR, "outputs", "models", "random_forest_model.pkl"
)

# -----------------------------
# Load Data & Model
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

df = load_data()
model = load_model()

# -----------------------------
# Label Mapping
# -----------------------------
label_map = {
    0: "Low",
    1: "High",
    2: "Medium",
    3: "Extreme"
}

# -----------------------------
# Sidebar Inputs
# -----------------------------
st.sidebar.header("🎛 Travel Details")

station = st.sidebar.selectbox(
    "Select Station", sorted(df["station"].unique())
)

day = st.sidebar.selectbox(
    "Select Day", df["day_of_week"].unique()
)

hour = st.sidebar.slider(
    "Select Hour (24-hour format)", 0, 23, 9
)

# -----------------------------
# Feature Engineering
# -----------------------------
is_weekend = 1 if day in ["Saturday", "Sunday"] else 0
is_peak_hour = 1 if hour in list(range(8, 11)) + list(range(18, 22)) else 0
is_morning = 1 if 8 <= hour <= 11 else 0
is_evening = 1 if 18 <= hour <= 22 else 0
is_office_hour = 1 if 9 <= hour <= 18 else 0

station_enc = df[df["station"] == station]["station_enc"].iloc[0]
line_enc = df[df["station"] == station]["line_enc"].iloc[0]
day_enc = df[df["day_of_week"] == day]["day_enc"].iloc[0]

input_df = pd.DataFrame([{
    "hour": hour,
    "is_weekend": is_weekend,
    "is_peak_hour": is_peak_hour,
    "is_morning": is_morning,
    "is_evening": is_evening,
    "is_office_hour": is_office_hour,
    "station_enc": station_enc,
    "line_enc": line_enc,
    "day_enc": day_enc
}])

# -----------------------------
# Prediction
# -----------------------------
prediction = model.predict(input_df)[0]
crowd = label_map[prediction]

# -----------------------------
# Output Section
# -----------------------------
st.subheader("🔎 Prediction Result")

if crowd == "Extreme":
    st.error("🚨 Crowd Level: EXTREME")
    st.warning("⚠️ Recommendation: Avoid travel during peak hours (8–11 AM, 6–9 PM)")

elif crowd == "High":
    st.warning("⚠️ Crowd Level: HIGH")
    st.info("💡 Consider traveling slightly earlier or later")

elif crowd == "Medium":
    st.info("ℹ️ Crowd Level: MEDIUM")
    st.success("👍 Travel is manageable")

else:
    st.success("✅ Crowd Level: LOW")
    st.info("🎉 Best time to travel!")

st.markdown("---")
st.caption("Powered by Machine Learning • Mumbai Local Train Crowd Analysis")
