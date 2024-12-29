import pandas as pd
from preprocess import preprocess
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import streamlit as st

calories = pd.read_csv('E:/MS DS/ML Project/calories.csv')
exercise = pd.read_csv('E:/MS DS/ML Project/exercise.csv')


x,y = preprocess(calories,exercise)

scaler = StandardScaler()

x_scaled = scaler.fit_transform(x)

x_train,x_test,y_train,y_test = train_test_split(x_scaled,y,test_size=0.2,random_state=42)

model = RandomForestRegressor()

model.fit(x_train,y_train)
accuracy = model.score(x_test,y_test)
accuracy = accuracy*100

"""------------------------------------------------------------------"""

# App title and description
st.title("Calories Burn Predictor")
st.markdown(
    """
    Welcome to the **Calories Burn Predictor**! Please enter your information below. 
    This app is designed to collect and process essential health data for analysis.
    """
)

# Sidebar with app information
st.sidebar.header("App Information")
st.sidebar.info(
    """
    - **Gender**: Select Male, Female.
    - **Age**: Enter your age in years.
    - **Height**: Provide your height in centimeters (cm).
    - **Weight**: Enter your weight in kilograms (kg).
    - **Duration**: Activity duration in minutes.
    - **Heart Rate**: Average heart rate in beats per minute (BPM).
    - **Body Temperature**: Current body temperature in Celsius (°C).
    """
)

# Input form
with st.form("health_form"):
        st.subheader("👥 Enter Your Details")

        gender = st.selectbox("Gender", ["Male", "Female"], index=0)
        age = st.number_input("Age (years)", min_value=0, max_value=120, value=25, step=1)
        height = st.number_input("Height (cm)", min_value=0.0, max_value=250.0, value=170.0, step=0.1)
        weight = st.number_input("Weight (kg)", min_value=0.0, max_value=300.0, value=70.0, step=0.1)
        duration = st.number_input("Activity Duration (minutes)", min_value=0, max_value=300, value=30, step=1)
        heart_rate = st.number_input("Heart Rate (BPM)", min_value=0, max_value=220, value=70, step=1)
        body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=36.5, step=0.1)

        submitted = st.form_submit_button("Predict")

if submitted:
    # Data preparation
        query = [gender,age,height,weight,duration,heart_rate,body_temp]
        query = pd.DataFrame([query], columns=["Gender","Age","Height","Weight","Duration","Heart_Rate","Body_Temp"])
        query = query.replace({'Gender':{'Male':0,'Female':1}})
        query =scaler.transform(query)
        prediction = model.predict(query)[0]


        st.success("Your data has been processed successfully!")
        st.write("## Calories Burned:",prediction)
        st.write("## Model Accuracy: ",round(accuracy,2))







