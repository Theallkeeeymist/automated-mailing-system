import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

data=pd.read_csv("have_credit_card.csv")

# excel ke columns
data.columns=['customer_id', 'customer_name', 'email_id', 'credit_card', 'flag']

#sender details
app_password = "app-password"
sender_email = "allkeeeymist@gmail.com"
subject = "New Credit Card offers, come to bank."

for i,j in data.iterrows():
    receiver_email = j['email_id']
    name = j['customer_name']
    body = (f"Dear {name}, \n\n"
            "There are new credit card offers specifically for you, come to our bank for further more details. \n\n"
            "Thanks and regards \n"
            "Allkeeey")

    # Setup MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)
    finally:
        server.quit()
