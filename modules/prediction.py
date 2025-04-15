import joblib

def load_model(path):
    return joblib.load(path)

def predict(model, data):
    # Transformation des données pour correspondre au modèle
    features = [[
        data['age'],
        data['sex']  ,
        data['bmi'],
        data['children'],
        data['smoker'] ,
        data['region']  # Remplacer par un code numérique si nécessaire
    ]]
    return model.predict(features)[0]