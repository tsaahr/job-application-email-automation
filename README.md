# Job Application Email Automation

Automates sending personalized job applications via email, bulk outreach without depending on job boards.
Built from a real need when moving to Ireland with limited English skills.

---

# Background #
When I first arrived in Ireland, getting a job was a struggle, especially with my English still at a basic level.
I needed a fast, organized, and scalable way to apply for as many jobs as possible without being slowed down by platform limits.
This tool helped me secure my current job as a Cleaner by massively increasing the number of applications I could send each day.

## What does the program do?

* Reads multiple CSVs containing employer emails and job categories 
* Cleans, normalizes, and merges data into a single contacts.csv
* Generates a single `contacts.csv` file with unique emails and personalized messages based on job category  
* Sends emails automatically with:  
  * Subject line based on job title  
  * Customized message for each recipient  
  * Attached PDF résumé  
* Displays in the terminal each email successfully sent  

---

## Technologies used

* Python 3  
* Pandas for data manipulation  
* SMTP (Gmail) for sending emails  
* `dotenv` for environment variable management  
* `EmailMessage` for composing messages  
* CSV handling and file I/O  

## Setup

* Clone this repo and create a virtual environment.
* Install dependencies.
* Add your .env.
* Enable Gmail 2FA and generate an App Password.
* Place your resume as CV Lithierry.pdf in the root folder.
* Create you csvs folder
* Put your CSV files in csvs/.

---

## Usage

#### Generate contacts
* python create_contacts.py

#### Send applications
* python send_emails.py

## Status

Completed — used successfully for job hunting in Ireland.

---

## Notes

* The `.env` file must contain:  
  ```
  EMAIL=your_email@gmail.com
  EMAIL_APP_PASSWORD=your_app_password
  ```
* Always test with a few emails before running large batches  
