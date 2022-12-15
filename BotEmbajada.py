from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from email.message import EmailMessage
import ssl
import smtplib

#-------- Mandar el Email --------

email_sender = '' #Tu Gmail
email_password = '' #Contraseña que te proporciona Gmail (Generar contraseña para aplicacion en myaccount.google.com)
email_receiver = '' #El Email receptor

subject = 'Ya hay truno!'
body = """
Ya hay turno para tramitar la ciudadania
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject

em.set_content(body)

context = ssl.create_default_context()

#-------- Check sitio --------

#Estas 3 opciones mantienen la ventana abierta.
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

PATH = "C:\Program Files (x86)\chromedriver.exe" #Si lanza error buscar donde esta el ejecutable chromedriver.exe

driver.get("https://www.cgeonline.com.ar/informacion/apertura-de-citas.html") #Pagina de la embajada

while True:
    element_table = driver.find_element(By.XPATH, "//table/tbody/tr[last()-4]/td[last()-1]").text #Lee el texto de la pagina

    if element_table == "fecha por confirmar":
        #print("Todavia no hay fecha")
        driver.refresh()
        time.sleep(10)
    else:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: #Envia el mail
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        quit()