import streamlit as st
from sklearn.preprocessing import StandardScaler
import joblib
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

st.success('Sreesai Sameera Koppana')
# Define min-max values for tenure and total_charges
tenure_min, tenure_max = 0, 72
total_charges_min, total_charges_max = 18, 9000

# Convert tenure and total_charges to standardized scalar values
scaler = StandardScaler()
scaler.fit([[tenure_min], [tenure_max]])
def scale_tenure(tenure):
    return scaler.transform([[tenure]])[0][0]

scaler.fit([[total_charges_min], [total_charges_max]])
def scale_total_charges(total_charges):
    return scaler.transform([[total_charges]])[0][0]
model=joblib.load(open('app/model.pkl','rb'))

# Define Streamlit app
def main():
        st.title("Telecom Customer Churn Prediction")
        st.header("Enter customer details")
        # Example: Train AdaBoostClassifier
        st.subheader("AdaBoostClassifier")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            contract_options = ['Month-to-month', 'One year', 'Two year']
            contract_index = st.selectbox('Contract', contract_options)

        # Update code for user input and prediction
        with col2:
            tenure_ = st.slider('Tenure', min_value=tenure_min, max_value=tenure_max, step=1, value=36)
            tenure = scale_tenure(tenure_)
            
        with col4:
            total_charges_ = st.slider('Total Charges', min_value=total_charges_min, max_value=total_charges_max, step=1, value=4500)
            total_charges = scale_total_charges(total_charges_)
            
        with col3:
            online_security_options = ['No', 'Yes', 'No internet service']
            online_security_index = st.selectbox('Online Security', online_security_options)
            
        contract_mapping = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}
        online_security_mapping = {'No': 0, 'Yes': 1, 'No internet service': 2}
        # Convert selected options to numerical values
        contract = contract_mapping[contract_index]
        online_security = online_security_mapping[online_security_index]
    #    st.success("flag 1 execution")\
    #    st.write(contract, tenure, online_security, total_charges)
        st.write(f"contract: '{contract}'", f"tenure: '{tenure_}'", f"online_security: '{online_security}'", f"total_charges: '{total_charges_}'")

    # Pass the user inputs to the model for prediction
        prediction = model.predict([[contract, tenure, online_security, total_charges]])
   #     st.write('flag 2')
        st.write(prediction)
   
        if prediction[0] == 1:
            output = 'The person is in the list of churn'
        else:
            output = 'The person is not in list of churn'
        st.success(output)
      #  st.write('flag 3')
        
# Run the app
if __name__ == "__main__":
    main()
