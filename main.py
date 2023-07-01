from smtplib import SMTP
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.utils import formataddr
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

send_to = "community_"
subject = "Congratulations on Being Selected as a Data Fellow"


def send_email():
    host = "smtp.gmail.com"
    port = 587

    from_mail = os.getenv("email")

    email_content =""

    with open(f"templates/{send_to}.html", 'r') as file:
        email_content = file.read()



    with SMTP(host, port) as smtp:
        smtp.starttls()
        smtp.login(from_mail, os.getenv("password"))
        
        df = pd.read_csv(f"data/{send_to}.csv")

        total = len(df.index)

        for index,row in df.iterrows():
            
            # replace text
            content = email_content.replace("{name}", row["name"].title())

            msg = MIMEMultipart()

            msgText = MIMEText(content, 'html')
            msg.attach(msgText)

            # # attach image
            # with open(f"{send_to}/{row['name'].lower().replace(' ', '_')}.png", "rb") as image:
            #     img = MIMEImage(image.read())
            #     img.add_header('Content-Disposition', 'attachment', filename="invite.png")
            #     msg.attach(img)

            # with open("attachments/event_schedule.pdf", "rb") as pdf:

            #     p = MIMEApplication(pdf.read())
            #     p.add_header('Content-Disposition', 'attachment', filename="event_schedule.pdf")
            #     msg.attach(p)

            # with open("judging_criteria.pdf", "rb") as pdf:
            #     p = MIMEApplication(pdf.read())
            #     p.add_header('Content-Disposition', 'attachment', filename="judging_criteria.pdf")
            #     msg.attach(p)


            msg['Subject'] = subject

            msg['From'] = formataddr(("Prayatna Mishra", from_mail))
            msg['To'] = formataddr((row["email_name"], row["email"]))

            

            smtp.sendmail(from_mail, row["email"], msg.as_string())

            print(f"Mail sent to {row['email']}. ({index+1}/{total})")




if __name__ == "__main__":
    send_email()
