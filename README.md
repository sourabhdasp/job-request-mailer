

This project automates the process of sending personalized job request emails to multiple recipients using SMTP. The tool is designed to streamline communication with potential candidates for a job position, such as a Cyber Security Analyst, and includes the ability to attach a resume to each email. It reads email addresses from a text file (email.txt), allowing users to send bulk emails efficiently, with customizable templates and secure connections.
Features

    Bulk Email Sending: Easily send job request emails to multiple recipients.
    Email Template: Customizable plain-text email body for job invitations.
    Resume Attachment: Attach a resume (or any file) to the emails.
    SMTP Integration: Works with any SMTP server (example shown for Gmail).
    Rate Limiting: A delay between email sends to avoid being flagged as spam.
    Error Handling: Handles errors related to email sending and file attachments.

Requirements

    Python 3.x: Make sure you have Python 3 installed on your system.
    SMTP Account: You'll need an email account (e.g., Gmail) to send emails. For Gmail, you may need to generate an App Password if 2-Step Verification is enabled.

Installation
Step 1: Clone the repository

git clone https://github.com/yourusername/job-request-mailer.git

Step 2: Install Dependencies

The project uses Python's built-in libraries, so there is no need for additional packages. However, ensure you have Python installed.

python --version  # Check if Python 3.x is installed

Step 3: Edit Email Configuration

Open the main.py file and update the following SMTP credentials:

    smtp_user: Your email address (e.g., your_email@gmail.com).
    smtp_password: Your email account password or App Password (for Gmail users with 2FA enabled).

smtp_user = 'your_email@gmail.com'
smtp_password = 'your_app_password'  # Generate an App Password from your email provider if needed

Step 4: Prepare the Email List

Create a text file named email.txt in the project directory. List all the recipient email addresses, one per line:

email1@example.com
email2@example.com
email3@example.com

Step 5: Attach Your Resume

If you want to attach a resume (or any file), make sure the resume.pdf file is available in the project directory or update the path to the actual file in the script:

resume_path = 'resume.pdf'  # Update this path with the actual location of your resume file

Step 6: Run the Script

Once you've configured the email settings and added the recipients and resume, run the script:

python main.py

This will send the job request emails with the attached resume to all the recipients listed in the email.txt file.
Customization

    Email Subject & Body: Modify the subject and body variables in the script to change the content of the email.
    Resume Path: Change the path to the resume file in the script if needed, or pass None if you don't wish to attach a file.

resume_path = None  # If you don't want to attach a resume

Delay Between Emails

To prevent your email account from being flagged as a spammer, the script includes a 5-second delay between sending each email. You can modify the delay time by changing the argument in the time.sleep(5) function:

time.sleep(5)  # Delay in seconds (adjust as needed)

Example Email Body

Here is a sample of what the email body will look like when the script runs:

Subject: Opportunity for Cyber Security Analyst Position at [Company Name]

Dear [Name],

I hope this message finds you well. My name is [Your Name], and I am a [Your Job Title] at [Company Name]. We are currently looking for a talented Cyber Security Analyst to join our team, and after reviewing your profile, I believe you could be a great fit for this role.

At [Company Name], we are committed to safeguarding our digital infrastructure and ensuring the security of our systems and data. As a Cyber Security Analyst, you would play a pivotal role in protecting our network, analyzing security incidents, and implementing effective security measures.

Feel free to customize this template to fit your company's job description or role details.
Troubleshooting

    SMTP Authentication Error: If you're using Gmail, make sure to enable "Less secure app access" or generate an App Password.
    File Attachment Error: If the resume file is not found, check the path or ensure the file exists in the directory.
    Rate Limiting: If emails aren't sending, increase the delay (e.g., time.sleep(10)) to avoid being flagged for spamming.

Contributing

Feel free to fork the repository and create pull requests for improvements or bug fixes. If you encounter any issues or have feature requests, open an issue on GitHub.
License

This project is licensed under the MIT License - see the LICENSE file for details.