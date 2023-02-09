#!/Users/sankarasarma/opt/anaconda3/bin/python3
"""
Author : Sankara Sarma  <xxxxx@gmail.com>
Date   : 02/08/2023
Purpose: Program to send personalized emails to a list of users
"""
import argparse
from email.message import EmailMessage  #email.message - a module, EmailMessage-class
import pandas as pd
import ssl
import smtplib

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Send personalized emails to a list of users',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        required=True)

    

    return parser.parse_args()


# --------------------------------------------------

def sendemails(inputfile):
    data = pd.read_csv(inputfile)
    select=["FirstName","LastName","EmailId"]
    email_list = data[select]
    
    # getting the names and the emails
    # iterate through the records
    for i in range(len(email_list)):
    
        # for every record get the name and the email addresses

        email = email_list.at[i,'EmailId']
        receiverFirstName=email_list.at[i,'FirstName']
        receiverLastName=email_list.at[i,'LastName']



        email_sender = ' xxxx@gmail.com'
        email_password = 'xxxxxxxxx'   #app password to be obtained from service provider
        email_receiver = email

        subject = "Dont forget to subscribe now"
        body =f' Hello {receiverFirstName} {receiverLastName} ,When you watch a video, please hit subscribe'
        
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)


        context = ssl.create_default_context()

        with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
def main():
    """Main Program"""

    args = get_args()
    file_arg = args.file
    file2open=file_arg.name
    sendemails(file2open)


# --------------------------------------------------
if __name__ == '__main__':
    main()
