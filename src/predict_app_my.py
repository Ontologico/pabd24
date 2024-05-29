"""House price prediction service"""
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, request, session, url_for
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth
from joblib import load

from utils import (predict_cpu_bounded, predict_cpu_multithread,
                   predict_io_bounded)

MODEL_SAVE_PATH = 'models/linear_regression_v01.joblib'

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Необходимо для работы сессий
CORS(app)

# Load environment variables
load_dotenv(".env")
app_token = os.getenv('APP_TOKEN')
if not app_token:
    raise ValueError("APP_TOKEN not found in .env file")

auth = HTTPTokenAuth(scheme='Bearer')

tokens = {
    app_token: "user1",
}

model = load(MODEL_SAVE_PATH)


@auth.verify_token
def verify_token(token):
    print(f"Received token: {token}")
    if token in tokens:
        return tokens[token]
    else:
        print("Token verification failed")
        return None

def predict(in_data: dict) -> int:
    """ Predict house price from input data parameters.
    :param in_data: house parameters.
    :raise Error: If something goes wrong.
    :return: House price, RUB.
    :rtype: int
    """
    area = float(in_data['area'])
    price = model.predict([[area]])
    return int(price)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        token = request.form.get('token')
        if token == app_token:
            session['token'] = token
            return redirect(url_for('predict_page'))
        else:
            return "Invalid token", 401
    
    return """
    <!DOCTYPE html>
    <html>
    <head>
    <title>Token Authentication</title>
    </head>
    <body>
    <h1>Enter Token</h1>
    <form method="post">
        <label for="token">Token:</label>
        <input type="text" id="token" name="token" required><br>
        <button type="submit">Submit</button>
    </form>
    </body>
    </html>
    """

@app.route("/predict", methods=['GET', 'POST'])
def predict_page():
    if 'token' not in session or session['token'] != app_token:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        in_data = request.form.to_dict()
        price = predict(in_data)
        return jsonify({'price': price})
    
    return """
    <!DOCTYPE html>
    <html>
    <head>
    <link rel="shortcut icon" type='image/vnd.microsoft.icon' href="/favicon.ico">
    <script>
    async function handleSubmit(event) {{
        event.preventDefault();
        const area = document.getElementById('area').value;
        const response = await fetch('/predict', {{
            method: 'POST',
            headers: {{
                'Content-Type': 'application/x-www-form-urlencoded',
            }},
            body: new URLSearchParams({{
                'area': area
            }})
        }});
        if (response.ok) {{
            const result = await response.json();
            document.getElementById('result').innerText = 'Predicted Price: ' + result.price + ' RUB';
        }} else {{
            document.getElementById('result').innerText = 'Authorization failed or error occurred.';
        }}
    }}
    </script>
    </head>
    <body>
    <h1>Housing price service.</h1>
    <form method="post" onsubmit="handleSubmit(event)">
        <label for="area">Area:</label>
        <input type="text" id="area" name="area" required><br>
        <button type="submit">Обработать</button>
    </form>
    <p id="result"></p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0')