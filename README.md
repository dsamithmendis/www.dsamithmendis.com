
# Portfolio Website

A personal portfolio website built with Flask, HTML, CSS (Tailwind + custom), showcasing skills, projects, and contact information.

## 🚀 Features

- Responsive layout using Tailwind CSS
- Dynamic sections: About, Skills, Projects, Certifications
- Contact form with email integration
- Social media links
- Clean and professional design

## 📁 Project Structure

```
portfolio/
├── assets/
│   ├── backend/
│   │   └── main.py        # Flask server
│   └── frontend/
│       └── main.css       # Custom styles
├── index.html             # Main portfolio page
└── README.md             # Project documentation
```

## 🛠️ Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML, Tailwind CSS, Custom CSS
- **Email**: SMTP integration for contact form

## 💻 Development

1. Make sure Python 3.12+ is installed
2. Install dependencies:
   ```
   pip install flask
   ```
3. Run the Flask server:
   ```
   python assets/backend/main.py
   ```
4. Visit `http://localhost:5000` in your browser

## 📧 Contact Form Setup

To enable the contact form:
1. Set up environment variables:
   - GMAIL_USER
   - GMAIL_APP_PASSWORD

## 📜 License

This project is licensed under the MIT License

---
© 2025 Samith Mendis
