from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')  # Your single-page application template


@app.route('/form', methods=["POST"])
def brain():
    try:
        Nitrogen = float(request.form['Nitrogen'])
        Phosphorus = float(request.form['Phosphorus'])
        Potassium = float(request.form['Potassium'])
        Temperature = float(request.form['Temperature'])
        Humidity = float(request.form['Humidity'])
        Ph = float(request.form['ph'])
        Rainfall = float(request.form['Rainfall'])

        values = [Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall]

        if Ph > 0 and Ph <= 14 and Temperature < 100 and Humidity > 0:
            # Load the model
            model = joblib.load('Pickle_RL_Model.pkl')  # Adjust the filename if necessary

            # Predict using the model
            arr = [values]
            acc = model.predict(arr)

            # Return prediction as JSON
            return jsonify({'prediction': str(acc[0])})
        else:
            return jsonify({'error': 'Error in entered values in the form. Please check the values and fill it again.'})

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'})


if __name__ == '__main__':
    app.run(debug=True)
