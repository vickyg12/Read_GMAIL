Hello,

Modules needed:
imaplib
email
os


I have read the content of the GMAIL using a specific subject and downloaded the attachments. Saved in the local.

#Based on subject - searching
result, data = mail.search(None, '(SUBJECT "Contract note")')

#searching whole mailbox
mail.select('"[Gmail]/All Mail"')
