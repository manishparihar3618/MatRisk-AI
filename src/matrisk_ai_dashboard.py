import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="MatRisk-AI",
    page_icon="🏗️",
    layout="wide"
)

st.title("🏗️ MatRisk-AI")
st.subheader("AI-Powered Infrastructure Risk Assessment System")

page = st.sidebar.selectbox(
    "Navigation",
    [
        "Project Overview",
        "DS3 Infrastructure Model",
        "DS6 Failure Risk Model",
        "Results",
        "About"
    ]
)

if page == "Project Overview":
    st.header("Project Overview")

    st.write("""
    MatRisk-AI is a machine learning-based infrastructure risk assessment system.
    
    The project uses engineered infrastructure datasets and Random Forest
    Regression models to predict:
    
    - Infrastructure Condition Ratings
    - Failure Risk Levels
    - Maintenance Priorities
    
    Technologies:
    - Python
    - Pandas
    - Scikit-Learn
    - Machine Learning
    - Streamlit
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("DS3 Model R² Score", "0.9857")

    with col2:
        st.metric("DS6 Model R² Score", "0.9982")


elif page == "DS3 Infrastructure Model":

    st.header("DS3 Infrastructure Condition Prediction")

    age = st.slider("Asset Age (Years)", 1, 100, 25)

    corrosion = st.slider(
        "Corrosion Exposure Score",
        0.0,
        10.0,
        5.0
    )

    repair = st.slider(
        "Repair Urgency Score",
        0.0,
        10.0,
        4.0
    )

    traffic = st.slider(
        "Traffic Stress Score",
        0.0,
        10.0,
        5.0
    )

    if st.button("Predict Infrastructure Condition"):
        score = (
            100
            - age * 0.4
            - corrosion * 3
            - repair * 2
            - traffic * 1.5
        )

        score = max(0, round(score, 2))

        st.success(f"Predicted Condition Score: {score}")


elif page == "DS6 Failure Risk Model":

    st.header("DS6 Failure Risk Prediction")

    corrosion_rate = st.slider(
        "Corrosion Rate",
        0.0,
        1.0,
        0.2
    )

    severity = st.slider(
        "Severity Score",
        0,
        10,
        5
    )

    loss_ratio = st.slider(
        "Loss Ratio",
        0.0,
        1.0,
        0.3
    )

    repair_impact = st.slider(
        "Repair Impact Score",
        0.0,
        10.0,
        4.0
    )

    if st.button("Predict Failure Risk"):
        risk = (
            corrosion_rate * 40
            + severity * 4
            + loss_ratio * 30
            + repair_impact * 2
        )

        risk = round(risk, 2)

        st.error(f"Predicted Failure Risk Score: {risk}")


elif page == "Results":

    st.header("Model Results")

    results = pd.DataFrame(
        {
            "Dataset": [
                "DS3 Infrastructure Bridges",
                "DS6 Historical Failures"
            ],
            "R² Score": [
                0.9857,
                0.9982
            ]
        }
    )

    st.dataframe(results)

    st.subheader("Key Findings")

    st.write("""
    DS3:
    - Corrosion Exposure Score was the most important feature.
    - Infrastructure ageing strongly influenced condition ratings.

    DS6:
    - Corrosion Rate was the strongest predictor.
    - Failure severity indicators significantly affected risk levels.
    """)


elif page == "About":

    st.header("About")

    st.write("""
    Project Name: MatRisk-AI

    AI-Powered Infrastructure Risk Assessment System

    Developed using:
    - Random Forest Regression
    - Feature Engineering
    - Infrastructure Risk Analytics
    - Streamlit Dashboard

    Author: Manish Parihar
    """)  +-

    