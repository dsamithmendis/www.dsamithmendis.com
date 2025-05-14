from flask import Flask, render_template, request, redirect, url_for
import smtplib
import os

app = Flask(__name__,
            template_folder='../../',
            static_folder='../../assets/frontend',
            static_url_path='/assets/frontend')


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/send", methods=["POST"])
def send():
    if request.method != "POST":
        return redirect(url_for('index'))
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    gmail_user = os.getenv("GMAIL_USER")
    gmail_password = os.getenv("GMAIL_APP_PASSWORD")

    if not gmail_user or not gmail_password:
        return "Error: Missing email credentials."

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_user, gmail_password)
            subject = f"Contact Form Message from {name}"
            body = f"From: {email}\n\n{message}"
            email_message = f"Subject: {subject}\n\n{body}"
            server.sendmail(gmail_user, gmail_user, email_message)

        return "Message sent successfully!"
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
