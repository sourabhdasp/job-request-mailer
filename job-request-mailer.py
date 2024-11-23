import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import time  
def send_email(subject, body, to_emails, smtp_server, smtp_port, smtp_user, smtp_password, resume_path=None):
    
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))  
    if resume_path:
        try:
            with open(resume_path, 'rb') as resume_file:
                part = MIMEApplication(resume_file.read(), Name='resume.pdf') 
                part['Content-Disposition'] = f'attachment; filename="resume.pdf"'
                msg.attach(part)
        except Exception as e:
            print(f"Error attaching resume: {e}")
   
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  
            server.login(smtp_user, smtp_password)
            
            for to_email in to_emails:
                msg['To'] = to_email
                server.sendmail(smtp_user, to_email, msg.as_string())
                print(f"Email sent to {to_email}")
                time.sleep(5)
    
    except Exception as e:
        print(f"Error: {e}")

def load_emails(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def main():
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'Your email address'  
    smtp_password = 'Your App Password - watch youtube'  
 # add your own email template 
    subject = "Requesting for the cyber security analyst intern position"
    body = """
    Subject: Opportunity for Cyber Security Analyst Position at [Company Name]

Dear [Name],

I hope this message finds you well. My name is [Your Name], and I am a [Your Job Title] at [Company Name]. We are currently looking for a talented Cyber Security Analyst to join our team, and after reviewing your profile, I believe you could be a great fit for this role.

At [Company Name], we are committed to safeguarding our digital infrastructure and ensuring the security of our systems and data. As a Cyber Security Analyst, you would play a pivotal role in protecting our network, analyzing security incidents, and implementing effective security measures.

    """

    
    email_file = 'email.txt'
    to_emails = load_emails(email_file)

    resume_path = 'resume.pdf'  # add ur actual file path


    send_email(subject, body, to_emails, smtp_server, smtp_port, smtp_user, smtp_password, resume_path)

if __name__ == '__main__':
    main()
