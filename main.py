from flask import Flask, render_template
from flask import request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/portfolio")

def portfolio_details():
    return render_template("portfolio-details.html")

@app.route("/service")
def service_details():
    return render_template("service-details.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")

    # فعلاً فقط تست
    print(name, email, subject, message)

    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run(debug=True)
