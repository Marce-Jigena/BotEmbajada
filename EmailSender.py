import smtplib
from email.message import EmailMessage
import ssl


class Sender:
    def __init__(self, email, password, receiver):

        self.email = email
        self.password = password
        self.receiver = receiver

    def Send(self):
        subject = 'Ya hay truno!'
        body = """
        Ya hay turno para tramitar la ciudadania
        """

        em = EmailMessage()
        em['From'] = self.email
        em['To'] = self.receiver
        em['Subject'] = subject

        em.set_content(body)

        # Envia el mail
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context()) as smtp:
            smtp.login(self.email, self.password)
            smtp.sendmail(self.email, self.receiver, em.as_string())
