from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/compare")
def compare():
    return render_template("compare.html")

@app.route("/observations")
def observations():
    return render_template("observations.html")

@app.route("/analysis")
def analysis():
    return render_template("analysis.html")

# ADD THIS PART
@app.route("/compare-result")
def compare_result():
    return render_template("compare_result.html")

if __name__ == "__main__":
    app.run(debug=True)