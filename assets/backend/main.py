from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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
    
    try:
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()
        
        if not all([name, email, message]):
            return "Error: All fields are required.", 400

        gmail_user = os.getenv("GMAIL_USER")
        gmail_password = os.getenv("GMAIL_APP_PASSWORD")

        if not gmail_user or not gmail_password:
            return "Error: Email configuration is missing.", 500

        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = gmail_user
        msg['Subject'] = f"Contact Form Message from {name}"

        body = f"""
        Name: {name}
        Email: {email}
        
        Message:
        {message}
        """
        
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_user, gmail_password)
            server.send_message(msg)

        return "Message sent successfully!", 200
        
    except Exception as e:
        return f"Error sending message: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
