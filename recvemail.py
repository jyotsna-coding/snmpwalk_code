import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import getpass

username = "jyotsna.alcove@gmail.com"
password = getpass.getpass(prompt="Type your password for jyotsna.alcove@gmail.com and press enter: ")

def clean(text):
    # clean text for creating folder
    return "".join(c if c.isalnum() else "_" for c in text)

imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(username, password)
# print(imap.list())
imap.select("INBOX")
status, messages = imap.select("INBOX")
# status, messages = imap.search(None, "UNSEEN")
N = 3 # No. of mesages to fetch
messages = int(messages[0]) # total no. of emails

for i in range(messages, messages-N, -1):
    res, msg = imap.fetch(str(i), ("RFC822"))
    # print("Res is : ", res)
    # print ("msg is :", msg)
    for response in msg:
        if isinstance(response, tuple):

            msg = email.message_from_bytes(response[1])
            # print(msg)
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):

                subject = subject.decode(encoding)
                # print(subject)
            From, encoding = decode_header((msg.get("From")))[0]
            if isinstance(From, bytes):
                From = From.decode(encoding)
            print("Subject:  ", subject)
            print("From:  ", From)

