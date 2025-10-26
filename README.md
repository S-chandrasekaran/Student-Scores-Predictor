📚 Student Exam Score Predictor
This Streamlit app allows users to upload a student dataset and predict exam scores using a linear regression model. It’s designed for educators, data scientists, and students interested in understanding how study-related factors influence academic performance.

🚀 Features
- 📁 Upload your own CSV file containing student data
- 🧹 Automatic data cleaning and preprocessing
- 🔍 One-click training of a linear regression model
- 📊 Display of actual vs predicted scores
- 📈 Interactive scatter plot visualization
- 📉 Performance metrics: Mean Squared Error (MSE) and R² Scor

📦 Requirements
Make sure the following Python packages are listed in your requirements.txt:
streamlit
pandas
matplotlib
scikit-learn

📄 Expected CSV Format
Your uploaded CSV should include a column named exam_score as the target variable. All other columns will be treated as features. Categorical features will be automatically encoded.

▶️ How to Run Locally
- Clone the repository:
git clone https://github.com/your-username/student-score-predictor.git
cd student-score-predictor
- Install dependencies:
pip install -r requirements.txt
- Run the app:
streamlit run app.py

🌐 Deploy on Streamlit Cloud
- Push your code to a public GitHub repository
- Go to streamlit.io/cloud
- Click “New app”, select your repo, and deploy!

💡 Future Improvements
- Add support for model selection (e.g., decision trees, random forest)
- Allow manual input for prediction without uploading a file
- Add feature importance visualization
- Enable download of prediction results





