import os
from datetime import datetime
from email.message import EmailMessage
import smtplib
import pandas as pd
import glob

def read_csvs():
    csv_files = glob.glob("csvs/*.csv")
    dfs = []

    for file in csv_files:
        try:
            df = pd.read_csv(file, encoding="utf-8", on_bad_lines='skip')
            df.columns = [col.strip().lower() for col in df.columns]

            if "email" in df.columns:
                df = df[df["email"] != "email"]
                df["email"] = df["email"].str.strip().str.lower()  # normaliza os e-mails

            df = df.loc[:, ~df.columns.duplicated()]

            if not df.empty:
                dfs.append(df)
            else:
                print(f"{file} ignored")

        except Exception as e:
            print(f"Error in {file}: {e}")

    if dfs:
        merged = pd.concat(dfs, ignore_index=True)

        merged = merged.drop_duplicates(subset="email", keep="first")

        return merged
    else:
        return pd.DataFrame()


def extract_name(email):
    try:
        domain = email.split('@')[1].split('.')[0]
        return domain.capitalize() + " Team"
    except:
        return "Hiring Team"

def validate_resume(path='CV Lithierry.pdf'):
    if not os.path.exists(path):
        raise FileNotFoundError("Resume file not found.")

def log_sent(email, name, success=True):
    status = "SENT" if success else "FAILED"
    with open("log.txt", "a") as f:
        f.write(f"{datetime.now()} | {status} | {name} <{email}>\n")

def send_email(to_email, name, custom_message, subject_line, sender_email, app_password, resume_path='CV Lithierry.pdf'):
    msg = EmailMessage()
    msg['Subject'] = subject_line
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Reply-To'] = sender_email
    msg.set_content(custom_message)

    with open(resume_path, 'rb') as f:
        msg.add_attachment(
            f.read(),
            maintype='application',
            subtype='pdf',
            filename='CV Lithierry.pdf'
        )

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)