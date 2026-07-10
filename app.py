from flask import Flask, render_template, request
import pandas as pd
import pickle
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "artifacts", "best_model_lr.pkl")
preprocessor_path = os.path.join(BASE_DIR, "artifacts", "preprocessor.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(preprocessor_path, "rb") as f:
    preprocessor = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = {
        "area": [float(request.form["area"])],
        "bedrooms": [int(request.form["bedrooms"])],
        "bathrooms": [int(request.form["bathrooms"])],
        "stories": [int(request.form["stories"])],
        "mainroad": [request.form["mainroad"]],
        "guestroom": [request.form["guestroom"]],
        "basement": [request.form["basement"]],
        "hotwaterheating": [request.form["hotwaterheating"]],
        "airconditioning": [request.form["airconditioning"]],
        "parking": [int(request.form["parking"])],
        "prefarea": [request.form["prefarea"]],
        "furnishingstatus": [request.form["furnishingstatus"]]
    }

    input_df = pd.DataFrame(input_data)
    transformed_input = preprocessor.transform(input_df)
    prediction = model.predict(transformed_input)
    return render_template('index.html', prediction_text=f'Predicted House Price: ${prediction[0]:,.2f}')   

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)