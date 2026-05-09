# =========================================
# FLASK + TRADUCCIÓN AUTOMÁTICA
# =========================================

from flask import Flask, request, render_template
import joblib

from deep_translator import GoogleTranslator

# cargar modelo

model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")


app = Flask(__name__)

# ==============================
# HOME
# ==============================
@app.route('/')
def home():
    return render_template('index.html')

# ==============================
# PREDICCIÓN
# ==============================
@app.route('/predict', methods=['POST'])
def predict():

    texto_original = request.form['texto']

    if texto_original:

        texto_traducido = GoogleTranslator(
            source='auto',
            target='en'
        ).translate(texto_original)

        # vectorizar
        X = vectorizer.transform([texto_traducido])

        # predecir
        pred = model.predict(X)[0]

        return render_template(
            'index.html',
            prediction=pred,
            original=texto_original,
            traducido=texto_traducido
        )

    return render_template('index.html', prediction="Ingrese texto")

# ==============================
# RUN
# ==============================
if __name__ == "__main__":
    app.run(debug=True)