import streamlit as st
import joblib

# Load the pre-trained machine learning model
model = joblib.load('phishing_detection_model.pkl')

# Define the Streamlit app
def main():
    # Set title and description
    st.title('Phishing Domain Detection')
    st.write('Enter a domain URL to check if it is phishing or not.')

    # Add input field for domain URL
    domain_url = st.text_input('https://www.geeksforgeeks.org/', 'example.com')

    # Add button to make prediction
    if st.button('Check Phishing'):
        # Make prediction
        prediction = model.predict([domain_url])[0]
        if prediction == 1:
            st.error('Warning: Phishing Domain Detected!')
        else:
            st.success('Domain is Safe.')

# Run the Streamlit app
if _name_ == "_main_":
    main()
