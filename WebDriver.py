from EmailSender import Sender
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


class Window:
    def __init__(self, pagina):

        self.pagina = pagina


    def Open(self):
        # -------- Check sitio --------

        # Estas 3 opciones mantienen la ventana abierta.
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(self.pagina)  # Pagina de la embajada
        emailSent = False

        while emailSent is False:
            element_table = driver.find_element(By.XPATH, "//table/tbody/tr[last()-11]/td[last()-1]").text

            if element_table == "fecha por confirmar":
                driver.refresh()
                time.sleep(10)
            else:
                # ToDo: Implementar un foreach que itere por varios emails
                email = Sender("marcelojigena1@gmail.com", "zpne ukyl duzl obhu ", "marcelojigena1@gmail.com")
                email.Send()
                email = Sender("marcelojigena1@gmail.com", "zpne ukyl duzl obhu ", "micaeladdlf@gmail.com")
                email.Send()
                driver.quit()
                emailSent = True
