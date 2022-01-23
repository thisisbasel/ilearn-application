from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/climatechange")
def climatechange():
    return render_template("climatechange.html")

@app.route("/personalfinance")
def personalfinance():
    return render_template("personalfinance.html")

@app.route("/machinelearning")
def machinelearning():
    return render_template("machinelearning.html")

@app.route("/ai")
def ai():
    return render_template("ai.html")

@app.route("/mlnew")
def mlnew():
    return render_template("mlnew.html")

if __name__ == "__main__":
    app.run(debug=True)