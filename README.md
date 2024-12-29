# Calories-Burn-Predictor
A Streamlit-based web application that predicts the number of calories burned during physical activities using user-provided health metrics. This project leverages machine learning for accurate predictions and features a user-friendly interface for real-time interaction.

## Key Features
* Interactive Web App: Built with Streamlit for seamless user interaction.
* Health Metrics Input: Users can provide details like gender, age, height, weight, activity duration, heart rate, and body temperature for prediction.
* Real-Time Predictions: Calculates the estimated calories burned based on the provided input.
* Model Accuracy Display: Displays the model's performance accuracy for transparency.
* Machine Learning Model: Utilizes a Random Forest Regressor for robust and efficient predictions.
* Preprocessing Pipeline: Data merging, encoding, and scaling to ensure consistent and accurate model input.

## Tech Stack
* Programming Language: Python
* Frameworks: Streamlit
* Machine Learning: Scikit-learn
* Data Handling: Pandas
* Deployment: Compatible with local deployment or cloud platforms (e.g., Heroku, AWS, or Streamlit Cloud).

## Usage
1. Clone the repository:
```
git clone https://github.com/AbdAziz1/Calories-Burn-Predictor.git
```
2. Navigate to the project directory:
```
cd Calories-Burn-Predictor
```
3. Install required dependencies:
```
pip install -r requirements.txt
```
4. Run the application:
```
streamlit run app.py
```
5. Access the app in your browser at http://localhost:8501.

## Dataset
This project uses two datasets:
* calories.csv: Contains information about user calorie burns.
* exercise.csv: Includes user-specific exercise metrics and demographics.

## Project Workflow
1. Preprocess the datasets to merge, clean, and encode the necessary information.
2. Train a machine learning model (Random Forest Regressor) to predict calories burned.
3. Integrate the trained model with a Streamlit interface for user interaction.
4. Provide real-time predictions based on user inputs.

## Future Enhancements
* Add support for custom data uploads.
* Integrate data visualization for insights on calorie burning trends.
* Implement additional machine learning models for comparison.
* Enhance explainability using SHAP or LIME.









