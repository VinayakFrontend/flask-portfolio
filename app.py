from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    message = request.form.get("message")

    with open('messages.txt', 'a') as f:
        f.write(f"Name: {name}, Email: {email},Phone: {phone}, Message: {message}\n")

    return render_template('thankyou.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)


