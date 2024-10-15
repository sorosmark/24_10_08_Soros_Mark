from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

products = []

@app.route('/', methods = ["GET"])
def index():
    return render_template("index.html")


@app.route('/submit_products', methods = ["POST"])
def submit_products():
    name = request.form.get("productname")
    products.append(name)
    return redirect(url_for('index'))




if __name__ == "__main__":
    app.run(debug = True)
