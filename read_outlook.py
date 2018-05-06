import datetime
import email
import imaplib
import os
import datetime

from config import user, password, imap_url, attachment_dir


def read_email_from_gmail():
    mail = imaplib.IMAP4_SSL(imap_url)
    mail.login(user, password)
    """ Searching for the whole mailbox instead of a specific folder """
    mail.select('"[Gmail]/All Mail"')
    print("Login into Mailbox")
    today = datetime.datetime.today()
    cutoff = today - datetime.timedelta(days=7)
    """ Searching mails based on subject and the timestamp of 7 days"""
    result, data = mail.search(None, '(SUBJECT "Contract note")', 'SINCE', cutoff.strftime('%d-%b-%Y'))
    for num in data[0].split():
        result, data = mail.fetch(num, "(RFC822)")
        raw_email_string = data[0][1].decode('utf-8')
        msg = email.message_from_string(raw_email_string)
        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            email_date = msg['Date'].split(" ")
            filename = part.get_filename()
            """ I will be receiving the same filename in the mails so to differentiate 
            i have added timestamp along with files for easy identification"""
            filename = filename + "-" + str(int(email_date[1]) - 1) + str(email_date[2]) + str('.pdf')
            if bool(filename):
                """ writing file into directory """
                filepath = os.path.join(attachment_dir, filename)
                with open(filepath, 'wb') as e:
                    e.write(part.get_payload(decode=True))


if __name__ == "__main__":
    read_email_from_gmail()
