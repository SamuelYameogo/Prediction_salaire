import joblib
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Chargement du modèle entraîné
model = joblib.load("static/best_Ridge_model.pkl")

# Route pour la page d'accueil
@app.route('/')
def home():
    return render_template("home.html")

# Route pour la page de prédiction
@app.route('/predict_page')
def predict_page():
    return render_template('prediction.html')

# Route pour la prédiction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupération des données JSON de la requête
        data = request.get_json()
        print("Données reçues :", data)

        # Préparation des données d'entrée avec les variables spécifiques de votre modèle
        input_data = pd.DataFrame([{
            "Age": float(data.get('Age', 0.0)),
            "Gender": data.get('Gender', 'Male'),
            "Education Level": data.get('Education Level', 'Bachelor'),
            "Years of Experience": float(data.get('Years of Experience', 0.0))
        }])

        # Affichage du DataFrame pour débogage
        print("DataFrame d'entrée :", input_data)

        # Chargement du modèle sauvegardé
        pickled_model = pickle.load(open('best_Ridge_model.pkl', 'rb'))

        # Prédiction avec le modèle chargé
        prediction = pickled_model.predict(input_data)

        # Renvoi de la prédiction sous forme JSON
        return jsonify({"prediction": prediction[0]})

    except Exception as e:
        print("Erreur pendant la prédiction :", str(e))
        return jsonify({"error": str(e)}), 400

# Route de santé pour vérifier si le service fonctionne
@app.route('/health')
def health_check():
    try:
        # Si le modèle est chargé et le service est en état de fonctionner, renvoie OK
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        # Si une erreur se produit lors de la vérification, renvoie une erreur
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)  # debug=True
