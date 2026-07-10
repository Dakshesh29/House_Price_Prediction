from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model

with open('D:\\End to end ML projects\\House_Price_Prediction\\artifacts\\best_model_lr.pkl', 'rb') as f:
    model = pickle.load(f)

with open("D:\\End to end ML projects\\House_Price_Prediction\\artifacts\\preprocessor.pkl", "rb") as f:
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

if __name__ == '__main__':
    app.run(debug=True)