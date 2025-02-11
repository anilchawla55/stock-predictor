from flask import Flask, render_template, request

app = Flask("main")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    stock_name = request.form['stock_name']
    prediction = f"Prediction for {stock_name}: ₹{round(1000 + (500 * 0.5), 2)}"  
    return render_template('result.html', prediction=prediction)

if "main" == "main":
    app.run(debug=True)