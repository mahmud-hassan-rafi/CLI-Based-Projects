import os
from datetime import datetime

print("----------------- Job Application Inputs -----------------")
# Variables
sender_address =       input("Please enter your house address                                    : ")
sender_city =          input("Which city do you live in?                                         : ")
date = datetime.today().strftime("%d %B, %Y")
receiver_designation = input("Enter the recipient’s designation (e.g. The Manager)               : ")
receiver_company =     input("Enter the company name you are applying to                         : ")
receiver_location =    input("Enter the company’s location                                       : ")
job_position =         input("Which position are you applying for?                               : ")
reference_source =     input("Where did you see the job advertisement? (e.g. The New York Times) : ")
reference_date =       input("What was the date of the advertisement?                            : ")
applicant_name =       input("Enter your full name                                               : ")
enclosure =            input("What document are you attaching? (e.g. Resume, Biodata)            : ")

# Generate the letter
letter = f"""
{sender_address}
{sender_city}

{date}

{receiver_designation}
{receiver_company}
{receiver_location}

Subject: Application for the post of {job_position}

Sir,
    In response to your advertisement in {reference_source} dated {reference_date} for the post of {job_position}, your advertisement seems appealing. I hereby offer my candidature for the same.

I possess requisite qualifications and experience. I want to join your company to fully utilize my potential.

You may call me for an interview on any date as per your convenience. I shall be able to join my duties at one month's notice if appointed. I am enclosing my resume for your perusal.

Yours truly,  
{applicant_name}

Enclosure: {enclosure}
"""
print("\n------------ Ready Made Application Letter ---------------")
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "letter.txt")

with open(desktop_path, "w") as file:
    file.write(letter)

with open(desktop_path, 'r') as file:
    print(file.read())

print("Your application letter has been saved as 'letter.txt' on your Desktop. Please check it.")
