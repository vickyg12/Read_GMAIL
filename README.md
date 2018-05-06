Hello,

Libraries needed:
imaplib
email
os


The scope of the project is use to read the content of the mail based on the subject and download the attachment and save in the local.


>>>> Based on subject - searching
result, data = mail.search(None, '(SUBJECT "Contract note")')

>>>>searching whole mailbox
mail.select('"[Gmail]/All Mail"')


>>>>> New changes
Added timestamp condition on search operation instead of getting whole attachment everytime. Now getting only the details for 7 days.

>>>>> Fixed the filename issue
In my mail i used to get the attachment in the same so that i will added the timestamp along with filename for easy searching.


Happy Coding !!!
