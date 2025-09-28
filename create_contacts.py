import pandas as pd
from utils import extract_name
import os
from messages import MESSAGES
from utils import read_csvs

df = read_csvs()

if df.empty:
    print("Invalid")
    exit()

df["category"] = df["category"].fillna("unknown").astype(str)

#df = pd.read_csv("csvs/emails_general2.csv")

df.columns = df.columns.str.strip().str.lower()

def get_job(category):
    job_title = str(category).strip().lower()

    if job_title == "cleaner":
        return "Cleaner"

    elif job_title in ["construction", "construção", "builder", "labour", "labor"]:
        return "Construction Worker"

    elif job_title in ["kitchen", "kitchen/restaurant", "restaurant"]:
        return "Kitchen Porter"

    elif job_title in ["retail", "retail/loja", "loja", "store"]:
        return "Retail Assistant"

    else:
        return "Any Position"

def get_message(category):
    category = str(category).strip().lower()
    key = str(category).strip().lower()

    if category == "cleaner":
        return MESSAGES["cleaner"]

    elif category in ["construction", "construção", "builder", "labour", "labor"]:
        return MESSAGES["construction"]

    elif category in ["kitchen", "kitchen/restaurant", "restaurant"]:
        return MESSAGES["kitchen"]

    elif category in ["retail", "retail/loja", "loja", "store"]:
        return MESSAGES["retail"]

    elif category in ["hotel", "hotel/hostel", "hostel"]:
        return MESSAGES["hotel"]

    else:
        return MESSAGES["default"]

df["name"] = df["email"].apply(extract_name)
df["message"] = df["category"].apply(get_message)
df["job_title"] = df["category"].apply(get_job)
df.rename(columns={"email": "email"}, inplace=True)

df_final = df[["name", "email", "message", "job_title"]]

if os.path.exists("../contacts.csv"):
    existing_df = pd.read_csv("../contacts.csv")

    for idx, row in df_final.iterrows():
        if row['email'].lower() in existing_df['email'].str.lower().values:
            existing_df.loc[
                existing_df['email'].str.lower() == row['email'].lower(), ['name', 'message', 'job_title']] = row[
                ['name', 'message', 'job_title']].values
        else:
            existing_df = pd.concat([existing_df, pd.DataFrame([row])], ignore_index=True)

    existing_df.to_csv("contacts.csv", index=False)
else:
    df_final.to_csv("contacts.csv", index=False)

print("contacts.csv created successfully.")
