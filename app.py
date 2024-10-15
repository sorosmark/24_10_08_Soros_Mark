from flask import Flask, render_template, request

app = Flask(__name__)

products = []

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("productname")
        products.append(name)
    return render_template("index.html", products_ = products)

if __name__ == "__main__":
    app.run(debug = True)
