import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load dataset
def load_data():
    df = pd.read_csv('ev_charging_data.csv')
    
    # Data Cleaning
    df['StartTime'] = pd.to_datetime(df['StartTime'], errors='coerce')
    df = df.dropna(subset=['StartTime', 'EnergyConsumption', 'ChargingDuration'])

    # Feature Engineering
    df['Hour'] = df['StartTime'].dt.hour
    df['Day'] = df['StartTime'].dt.day_name()
    return df

st.title("EV Charging Insights & Prediction")

# Load
with st.spinner('Loading data...'):
    df = load_data()

st.subheader("Dataset Preview")
st.write(df.head())

# Visualization
st.subheader("Energy Consumption Distribution")
fig, ax = plt.subplots()
ax.hist(df['EnergyConsumption'].dropna())
st.pyplot(fig)

# ML Prediction
X = df[['ChargingDuration', 'Hour']]
y = df['EnergyConsumption']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = LinearRegression()
model.fit(X_train, y_train)

st.subheader("Predict Energy Consumption")
duration = st.slider('Charging Duration (hrs)', 0.0, 10.0, 1.0)
hour = st.slider('Hour of Day', 0, 23, 10)

pred = model.predict([[duration, hour]])[0]
st.write(f"Predicted Energy Consumption: {pred:.2f} kWh")
