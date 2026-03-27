import streamlit as st
import pickle
import numpy as np
import os

# ✅ Correct path handling
model_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "student_model.pkl"
)

model = pickle.load(open(model_path, "rb"))

st.title("Student Performance Prediction System")

st.write("Enter student details")

study_hours = st.number_input("Study Hours", 0.0, 10.0)
attendance = st.number_input("Attendance (%)", 0, 100)
internal_marks = st.number_input("Internal Marks", 0, 100)
assignment_score = st.number_input("Assignment Score", 0, 100)

if st.button("Predict"):

    input_data = np.array([
        [study_hours, attendance, internal_marks, assignment_score]
    ])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Prediction: PASS")
    else:
        st.error("Prediction: FAIL")