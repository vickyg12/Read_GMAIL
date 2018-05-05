import imaplib
import email
import os
from config import user, password, imap_url, attachment_dir


def read_email_from_gmail():
    mail = imaplib.IMAP4_SSL(imap_url)
    mail.login(user, password)
    mail.select('"[Gmail]/All Mail"')
    print("Login into Mailbox")
    result, data = mail.search(None, '(SUBJECT "Contract note")')
    count = 0
    for num in data[0].split():
        result, data = mail.fetch(num, "(RFC822)")
        raw_email_string = data[0][1].decode('utf-8')
        msg = email.message_from_string(raw_email_string)
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                print(part.get_payload(decode=True))

            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            fileName = part.get_filename()
            print(part.get_)
            fileName = fileName+str(count)+str('.pdf')
            count = count + 1
            if bool(fileName):
                filePath = os.path.join(attachment_dir, fileName)
                with open(filePath, 'wb') as e:
                    e.write(part.get_payload(decode=True))


if __name__ == "__main__":
    read_email_from_gmail()
