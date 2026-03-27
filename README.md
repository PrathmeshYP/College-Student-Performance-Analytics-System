# 🎓 Student Performance Analytics System

A complete end-to-end Data Analytics & Machine Learning project that analyzes student data, predicts academic performance, and identifies at-risk students.

---

## 🚀 Project Overview

Educational institutions collect large amounts of student data but often fail to utilize it effectively.
This project solves that problem by:

* 📊 Analyzing student performance
* 🤖 Predicting pass/fail outcomes using Machine Learning
* ⚠️ Identifying at-risk students
* 📈 Providing insights for better decision-making

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas & NumPy
* Scikit-learn
* Streamlit (for web app)
* Power BI (for dashboard)

---

## 📁 Project Structure

```
student-performance-analytics
│
├── data
│   └── student_performance_1000.csv
│
├── scripts
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── model_training.py
│
├── models
│   └── student_model.pkl
│
├── app
│   └── app.py
│
├── train_pipeline.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Features

* ✔ Data Cleaning & Preprocessing
* ✔ Feature Engineering (Total Score, Study Efficiency)
* ✔ Risk Level Detection (High, Medium, Low)
* ✔ Machine Learning Model (Random Forest)
* ✔ Model Evaluation
* ✔ Interactive Prediction App using Streamlit

---

## 🧠 Machine Learning

* Algorithm: Random Forest Classifier
* Task: Classification (Pass / Fail)

### Input Features:

* Study Hours
* Attendance
* Internal Marks
* Assignment Score

---

## 📊 Sample Output

The system predicts whether a student will:

* ✅ PASS
* ❌ FAIL

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/student-performance-analytics.git
cd student-performance-analytics
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Train the model

```
python train_pipeline.py
```

This will:

* Train the model
* Save it in `models/student_model.pkl`

---

### 4️⃣ Run the application

```
cd app
streamlit run app.py
```

---

## 📈 Dashboard

A Power BI dashboard is included to visualize:

* Student performance trends
* Risk distribution
* Study hours vs marks

---

## 🔍 Future Improvements

* Add more features (Previous Grades, Final Marks)
* Improve model accuracy
* Deploy application online
* Add real-time data input
* Integrate database (MySQL)

---

## 👨‍💻 Author

**Prathmesh YadavPatil**

📧 [prathmeshyadavpatil9495@gmail.com](prathmeshyadavpatil9495@gmail.com)

---

## ⭐ Contribute

Feel free to fork this repository and improve it!

---

## 📌 Conclusion

This project demonstrates a complete data analytics pipeline from raw data to deployment, making it ideal for showcasing skills in Data Science, Machine Learning, and Data Visualization.
