from flask import Flask, render_template

app = Flask(name)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/items")
def items():
    return render_template("items.html")

if name == "main":
    app.run(debug=True)