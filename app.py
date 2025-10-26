import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Title
st.title("📚 Student Exam Score Predictor")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Load data
    df = pd.read_csv(uploaded_file)
    st.subheader("📄 Raw Data Preview")
    st.write(df.head())

    # Check for target column
    if 'exam_score' not in df.columns:
        st.error("❌ The dataset must contain an 'exam_score' column.")
        st.stop()

    # Preprocessing
    df = df.dropna()
    df = pd.get_dummies(df, drop_first=True)

    # Features and target
    X = df.drop('exam_score', axis=1)
    y = df['exam_score']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model training
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Results
    st.subheader("📊 Prediction Results")
    comparison_df = pd.DataFrame({
        'Actual Score': y_test.values,
        'Predicted Score': y_pred
    })
    st.write(comparison_df.head(10))

    st.metric("📉 Mean Squared Error", f"{mean_squared_error(y_test, y_pred):.2f}")
    st.metric("📈 R² Score", f"{r2_score(y_test, y_pred):.2f}")

    # Visualization
    st.subheader("📈 Actual vs Predicted Scores")
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred, color='blue', alpha=0.6)
    ax.set_xlabel("Actual Scores")
    ax.set_ylabel("Predicted Scores")
    ax.set_title("Student's Score Prediction")
    st.pyplot(fig)

else:
    st.info("📁 Please upload a CSV file to begin.")
