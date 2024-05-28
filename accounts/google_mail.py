import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading


class EmailByGoogle:
    def __init__(self, account, password):
        self.google_account = account
        self.google_password = password

    def send_email(self, subject, body, to_email):
        try:
            from_email = self.google_account
            app_password = self.google_password

            # Create message object
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = subject

            # Email body
            msg.attach(MIMEText(body, 'plain'))

            # Connection settings
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_email, app_password)

            # Send mail
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)

            server.quit()

            print("Email was send successfully")
        except Exception as e:
            print(f"Error when sending email: {e}")

    def send_in_thread(self, subject, body, to_email):
        email_thread = threading.Thread(
            target=self.send_email,
            args=(subject, body, to_email)
        )
        email_thread.start()
