#!/Users/xxxx/opt/anaconda3/bin/python3
''' Program to send personalized emails to a list of users '''
from email.message import EmailMessage  
import pandas as pd
import ssl
import smtplib
data = pd.read_csv(r'/path_to_csv_file/contacts.csv') 
select=["FirstName","LastName","EmailId"]


email_list = data[select]
  
# getting the names and the emails

# iterate through the records
for i in range(len(email_list)):
  
    # for every record get the name and the email addresses
    
    email = email_list.at[i,'EmailId']
    receiverFirstName=email_list.at[i,'FirstName']
    receiverLastName=email_list.at[i,'LastName']
#from app2 import gmailapp_password


    email_sender = ' xxxxx@gmail.com'
    email_password = 'xxxxxxxx'   #app password to be obtained from service provider
    email_receiver = email

    subject = "Dont forget to subscribe now"
    body =f' Hello {receiverFirstName} {receiverLastName} ,When you watch my youtube channel, please hit subscribe'
    
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())