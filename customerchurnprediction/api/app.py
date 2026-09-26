from flask import Flask, render_template, request
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "frontend")
)


@app.route("/")
def home():

    try:
        import pandas as pd
        import joblib

        model_path = os.path.join(
            BASE_DIR,
            "CustomerChurnPredictionModel.pkl"
        )

        print("BASE_DIR:", BASE_DIR)
        print("MODEL_PATH:", model_path)
        print("MODEL EXISTS:", os.path.exists(model_path))

        model = joblib.load(model_path)

        return """
        <h1>Customer Churn App</h1>
        <p>Flask is working.</p>
        <p>Model loaded successfully.</p>
        """

    except Exception as error:

        print("MODEL ERROR:", repr(error))

        return f"""
        <h1>Model Loading Error</h1>
        <pre>{repr(error)}</pre>
        """, 500