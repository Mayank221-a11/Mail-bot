import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
# import all libraries
listener = sr.Recognizer()
print(listener)
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(reciver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Enter your Email address to send Mail in Ln. 32
    server.login('')
    email = EmailMessage()
    # enter your Email address in Ln. 35 to send Mail
    email['from'] = ''
    email['To'] = reciver
    email['subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    # 'Name': 'Email',
    # 'Name': 'Email'
}


def get_email_info():
    talk('To whom you want to send E-mail')
    name = get_info()
    reciver = email_list[name]
    print(reciver)
    talk('What is the subject of your E-mail')
    subject = get_info()
    talk('Tell me the text in your E-mail')
    message = get_info()
    send_email(reciver, subject, message)
    talk('Hey your email is Sent')
    talk('Do you want to send more email')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()




get_email_info()
