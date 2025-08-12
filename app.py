from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # For now, just print to console (in real life, send email or save to DB)
        print(f"New message from {name} ({email}): {message}")

        return render_template("success.html", name=name)
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
