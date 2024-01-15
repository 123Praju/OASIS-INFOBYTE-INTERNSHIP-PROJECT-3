import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(receiver_email, subject, body):
    sender_email = "abc928244@gmail.com"  # Your Gmail address
    app_password = "sftf rtpl vtfa zgpe"  # Your Gmail password

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject


    receiver_email = receiver_email.replace(" ", "")
    receiver_email = receiver_email.replace("at","@")
    print(receiver_email)
    # Attach the body of the email
    message.attach(MIMEText(body, "plain"))

    # Connect to the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

