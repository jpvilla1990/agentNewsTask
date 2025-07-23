import smtplib
from email.mime.text import MIMEText

class EmailService:
    """
    EmailService class to handle sending emails.
    This example uses a local SMTP server (like MailHog) for testing purposes.
    """

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the EmailService with the SMTP server and port.
        """
        self.smtp_server : str = smtp_server
        self.smtp_port : str = smtp_port
        self.username : str = username
        self.password : str = password

    def send_email(self, subject: str, html: str, from_addr: str, to_addr: str):
        """
        Send an email with the specified subject and body.
        """
        msg = MIMEText(html, "html")
        msg["Subject"] = subject
        msg["From"] = from_addr
        msg["To"] = to_addr

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.set_debuglevel(1)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.username, self.password)
            server.send_message(msg)
