# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15JiLBqADVUfZMobdyWmKYPME2-mLBpq5
"""

import streamlit as st
import pickle

# Load model and feature extractor
model = pickle.load(open('spam_model1.pkl', 'rb'))
feature_extraction = pickle.load(open('feature_extraction1.pkl', 'rb'))

# Streamlit UI
st.title(" Spam Email Classifier")
st.write("Enter a message to check if it's **Spam or Ham**")

# Input from user
input_msg = st.text_area("Enter your email message here:")

if st.button("Predict"):
    if input_msg.strip() == "":
        st.warning(" Please enter a message.")
    else:
        # Transform input and predict
        input_data = feature_extraction.transform([input_msg])
        prediction = model.predict(input_data)[0]

        if prediction == 0:
            st.error(" Spam Email Detected!")
        else:
            st.success(" This is a Ham (Not Spam) Email.")