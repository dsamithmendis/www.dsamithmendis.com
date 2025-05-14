# Import necessary modules from Flask and Python standard libraries
from flask import Flask, render_template, request
import smtplib  # Used to send emails using SMTP
import os       # Used to access environment variables (for secure credentials)

# Initialize the Flask app
app = Flask(__name__)

# Route for displaying the contact form
@app.route("/")
def index():
    return render_template("index.html")  # Render the HTML

# Route to handle form submission (POST request from the form)
@app.route("/send", methods=["POST"])
def send():
    # Get form data submitted by the user
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    # Get Gmail credentials securely from environment variables
    gmail_user = os.getenv("GMAIL_USER")
    gmail_password = os.getenv("GMAIL_APP_PASSWORD")

    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Start TLS encryption
            server.login(gmail_user, gmail_password)  # Log in to Gmail with app password

            # Prepare email content
            subject = f"Contact Form Message from {name}"
            body = f"From: {email}\n\n{message}"
            email_message = f"Subject: {subject}\n\n{body}"

            # Send the email to yourself (from and to are both your Gmail address)
            server.sendmail(gmail_user, gmail_user, email_message)

        return "Message sent successfully!"  # Success message to the user
    except Exception as e:
        return f"Error: {e}"  # Return error message if something goes wrong

# Run the Flask app on host 0.0.0.0 and port 81 (required by Replit)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
