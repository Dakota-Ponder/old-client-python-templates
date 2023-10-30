import smtplib
from email.message import EmailMessage


def send_email(subject, body, to_email, smtp_server, smtp_port, smtp_user, smtp_pass):
    """Send an email using the provided SMTP server details."""

    # Create an EmailMessage object and set its attributes
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = smtp_user
    msg['To'] = to_email

    # Establish a connection to the SMTP server and send the email
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)
        print(f"Email sent to {to_email}")


if __name__ == "__main__":
    # SMTP server details (adjust if not using Gmail)
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 465

    # SMTP user credentials
    SMTP_USER = "youremail@gmail.com"
    SMTP_PASS = "yourpassword"

    # Email details
    SUBJECT = "Test Email"
    BODY = "This is a test email sent from a Python script."
    TO_EMAIL = "recipient@example.com"

    send_email(SUBJECT, BODY, TO_EMAIL, SMTP_SERVER,
               SMTP_PORT, SMTP_USER, SMTP_PASS)
