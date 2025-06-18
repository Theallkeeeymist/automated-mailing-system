import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

app_password = "dfsp rxbx gzmv nsvf"
sender_email = "allkeeeymist@gmail.com"


data=pd.read_csv("credit_card_details.csv")
data.columns=['customer_name', 'email_id', 'credit_card_number', 'flag']

for i,j in data.iterrows():
    if(j['flag']=="Y"):
        name=j['customer_name']
        receiver_email=j['email_id']
        card_number=j['credit_card_number']
        subject="Offers on your credit card!"
        body=(f"Dear {name},\n\n"
                f"Card Number: {card_number}\n\n"
                "We are pleased to inform you that a host of exclusive new offers and benefits are now available on your credit card. "
                "We invite you to explore these offers and make the most of your card privileges.\n\n"
                "For more details, please visit your nearest branch or contact our customer service.\n\n"
                "Thank you for banking with us.\n"
                "Kind regards,\n"
                "Allkeeey"
              )

        message=MIMEMultipart()
        message['From']=sender_email
        message['To']=receiver_email
        message['Subject']=subject
        message.attach(MIMEText(body, "plain"))

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()  # connection established
            server.login(sender_email, app_password)
            server.sendmail(sender_email ,receiver_email, message.as_string())
            print("Mail sent successfully")
        except Exception as e:
            print("An error as occurred", e)
        finally:
            server.quit()
    else:
        name = j['customer_name']
        receiver_email = j['email_id']
        subject = "Get our credit cards NOW!"
        body = (f"Dear {name},\n\n"
                "We value your relationship with our bank and are pleased to offer you the opportunity to apply for our exclusive Credit Card, designed to complement your banking experience.\n\n"
                "Enjoy a range of benefits including reward points, exclusive offers, and enhanced spending power.\n\n"
                "To know more or to apply, please visit your nearest branch or contact our customer service.\n\n"
                "Thank you for banking with us.\n"
                "Kind regards,\n"
                "Allkeeey"
                )

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, "plain"))

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()  # connection established
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Mail sent successfully")
        except Exception as e:
            print("An error as occurred", e)
        finally:

            server.quit()