# backend/main.py
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import smtplib

app = FastAPI()

# Allow your frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in production, restrict to your domain
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/contact")
async def contact(
    email: str = Form(...),
    message: str = Form(...)
):
    # Simple SMTP email sending (example with Gmail)
    sender_email = "your@gmail.com"
    sender_password = "your_app_password"
    receiver_email = "your@email.com"

    subject = "New Portfolio Contact Form Message"
    body = f"From: {email}\n\nMessage:\n{message}"
    email_text = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, email_text)
        server.quit()
        return {"status": "success", "message": "Email sent!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
