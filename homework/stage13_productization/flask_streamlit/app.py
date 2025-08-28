from flask import Flask, request, jsonify, render_template_string
import joblib
import matplotlib.pyplot as plt
import io, base64

# ---- Load your model ----
model = joblib.load('model/model.pkl')
app = Flask(__name__)

# ---- Helper function ----
def predict(features):
    pred = model.predict([features])[0]
    return pred

# ---- Home Page ----
@app.route('/')
def home():
    html = """
    <html>
        <body style="font-family: Arial; padding:20px;">
            <h1>Welcome to the Flask Model API</h1>
            <p>Try these routes:</p>
            <ul>
                <li><a href="/predict/5">/predict/5</a> → Predict with one input</li>
                <li><a href="/predict/5/10">/predict/5/10</a> → Predict with two inputs</li>
                <li><a href="/plot">/plot</a> → Show demo plot</li>
            </ul>
        </body>
    </html>
    """
    return render_template_string(html)

# ---- JSON Prediction (POST) ----
@app.route('/predict', methods=['POST'])
def predict_default():
    data = request.get_json()
    features = data.get('features')
    return jsonify({'prediction': float(predict(features))})

# ---- Path-based Prediction ----

@app.route('/predict/<string:input1>')
@app.route('/predict/<string:input1>/<string:input2>')
def predict_path(input1, input2="none"):
    try:
        # convert inputs
        features = [float(input1.strip())]
        if input2 and input2.lower() != "none":
            features.append(float(input2.strip()))
    except Exception as e:
        return jsonify({'error': f'Conversion failed: {input1}, {input2}. Error: {str(e)}'}), 400

    try:
        # call model
        result = float(predict(features))
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': f'Model prediction failed for features={features}. Error: {str(e)}'}), 400


# ---- Plot Route ----
@app.route('/plot')
def plot_page():
    fig, ax = plt.subplots()
    ax.plot([0, 1, 2, 3], [10, 20, 15, 30])
    ax.set_title("Demo Plot")

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    html = f"""
    <html>
        <body style="font-family: Arial; padding:20px;">
            <h1>Model Output Plot</h1>
            <img src="data:image/png;base64,{img_base64}">
            <p><a href='/'>Back Home</a></p>
        </body>
    </html>
    """
    return render_template_string(html)

# ---- Run the app ----
if __name__ == '__main__':
    app.run(debug=True, port=5000)

