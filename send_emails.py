import pandas as pd
from dotenv import load_dotenv
import os
from utils import send_email

load_dotenv()
SENDER_EMAIL = os.getenv('EMAIL')
APP_PASSWORD = os.getenv('EMAIL_APP_PASSWORD')

contacts = pd.read_csv('contacts.csv')

def execute_send():
    for _, row in contacts.iterrows():
        try:
            job_title = row['job_title']
            if job_title == "Any Position":
                subject = "Job Application – Open Availability & Resume"
            else:
                subject = f"{job_title} Position – Application & Resume"

            print(f"Sending for: {row['email']}")

            send_email(
                to_email=row['email'],
                name=row['name'],
                custom_message=row['message'],
                subject_line=subject,
                sender_email=SENDER_EMAIL,
                app_password=APP_PASSWORD
            )
        except Exception as e:
            print(f"Failed to send to {row['email']}: {e}")

        print(f"Send for ")

if __name__ == "__main__":
    execute_send()