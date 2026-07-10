# 🏡 House Price Prediction

An end-to-end Machine Learning project that predicts house prices based on various property features. This project covers the complete ML workflow, from data analysis and model training to deploying a Flask web application.

---

## 📌 Project Overview

The goal of this project is to predict the selling price of a house using machine learning regression models. Multiple algorithms were trained and compared to select the best-performing model.

---

## 🚀 Features

- Exploratory Data Analysis (EDA)
- Data Cleaning
- Data Preprocessing
- Feature Engineering
- Multiple Regression Models
- Hyperparameter Tuning (GridSearchCV)
- Model Evaluation
- Flask Web Application
- Responsive User Interface
- Docker Support
- Azure Deployment Ready

---

## 📊 Dataset

**Target Variable**

- `price`

**Features**

- Area
- Bedrooms
- Bathrooms
- Stories
- Main Road
- Guest Room
- Basement
- Hot Water Heating
- Air Conditioning
- Parking
- Preferred Area
- Furnishing Status

---

## 🧠 Machine Learning Workflow

```
Dataset
    │
    ▼
EDA
    │
    ▼
Data Cleaning
    │
    ▼
Data Preprocessing
    │
    ▼
Model Training
    │
    ▼
Hyperparameter Tuning
    │
    ▼
Model Evaluation
    │
    ▼
Model Serialization (.pkl)
    │
    ▼
Flask Web App
    │
    ▼
Docker
    │
    ▼
Azure Deployment
```

---

## 🤖 Models Used

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

---

## 📈 Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## 🛠 Tech Stack

### Programming Language
- Python

### Machine Learning
- NumPy
- Pandas
- Scikit-learn
- XGBoost

### Data Visualization
- Matplotlib
- Seaborn

### Web Development
- Flask
- HTML
- CSS

### Deployment
- Docker
- Microsoft Azure

---

## 📂 Project Structure

```text
House_Price_Prediction/
│
├── artifacts/
│   ├── best_model.pkl
│   ├── best_model_lr.pkl
│   └── preprocessor.pkl
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── house_price_prediction.ipynb
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/House_Price_Prediction.git
```

Navigate to the project:

```bash
cd House_Price_Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 📷 Screenshots

### Home Page

![Home page](image.png)

### Prediction Result

_Add screenshot here_

![Predicttion result](image.png)

## 👨‍💻 Author

**Dakshesh Bijawar**

- GitHub: https://github.com/Dakshesh29
- LinkedIn: *(Add your LinkedIn profile here)*
