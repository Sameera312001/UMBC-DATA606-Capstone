# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import AdaBoostClassifier
import warnings
warnings.filterwarnings('ignore')

# Load the dataset
df = pd.read_csv("C:/Users/koppa/OneDrive/Documents/GitHub/UMBC-DATA606-Capstone/data/Telecom_Customer_Churn_Prediction.csv")

# Define function to preprocess data
def preprocess_data(df):
    # Handle missing values
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.fillna(df["TotalCharges"].mean(), inplace=True)
    
    # Encode categorical variables
    df = df.apply(lambda x: LabelEncoder().fit_transform(x) if x.dtype == 'object' else x)
    
    return df

# Preprocess the data
df = preprocess_data(df)

# Split data into features and target
X = df.drop(columns=['Churn'])
y = df['Churn']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=40, stratify=y)

# Define function to train and evaluate models
def train_and_evaluate_model(model, X_train, X_test, y_train, y_test):
    # Train the model
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    # Generate classification report
    report = classification_report(y_test, y_pred)
    
    # Generate confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    
    return accuracy, report, cm

# Define Streamlit app
def main():
    st.title("Telecom Customer Churn Prediction")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Data Exploration", "Model Training"))

    if page == "Data Exploration":
        st.header("Data Exploration")
        st.write("Explore your data here.")

        # Example: Display first few rows of the dataset
        st.subheader("First few rows of data")
        st.write(df.head())

        # Example: Display dataframe info
        st.subheader("Dataframe info")
        st.write(df.info())


    elif page == "Model Training":
        st.header("Model Training")
        st.write("Train your models here.")

        # Example: Train AdaBoostClassifier
        st.subheader("AdaBoostClassifier")
        ada_model = AdaBoostClassifier()
        ada_accuracy, ada_report, ada_cm = train_and_evaluate_model(ada_model, X_train, X_test, y_train, y_test)
        st.write("Accuracy:", ada_accuracy)
        st.write("Classification Report:")
        st.write(ada_report)
        st.write("Confusion Matrix:")
        st.write(ada_cm)

        
# Run the app
if __name__ == "__main__":
    main()
