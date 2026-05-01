from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options = Options()

caminho_perfil = r"C:\Users\Pedro Valente\AppData\Local\Google\Chrome\User Data"
options.add_argument(f"user-data-dir={caminho_perfil}")
options.add_argument("--profile-directory=Default")

options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-first-run")
options.add_argument("--no-service-autorun")
options.add_argument("--password-store=basic")

navegador = webdriver.Chrome(options=options)
time.sleep(2)
navegador.get("https://www.amazon.com.br/")
navegador.maximize_window()
time.sleep(5)
barra_pesquisa = navegador.find_element("id", "twotabsearchtextbox")
barra_pesquisa.click()
barra_pesquisa.send_keys("Galaxy S25")
barra_pesquisa.send_keys(Keys.ENTER)
time.sleep(2)

# Localiza o container do produto pelo ASIN e clica no link
produto1 = navegador.find_element("css selector", f'div[data-asin="B0DSY665M3"] a.a-link-normal')
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", produto1)
produto1.click()

time.sleep(10)
nome_produto1 =  navegador.title
precoInt_produto1 = navegador.find_element("class name", "a-price-whole").text
precoFloat_produto1 = navegador.find_element("class name", "a-price-fraction").text
print(f"Nome - {nome_produto1}")
print(f"Preço - R$ {precoInt_produto1},{precoFloat_produto1}")

#cria e muda para a nova guia do email
navegador.execute_script("window.open('');")
abas = navegador.window_handles
navegador.switch_to.window(abas[1])
navegador.get("https://mail.google.com/mail/u/0/#inbox")

botao_escrever = navegador.find_element("css selector", "T-I.T-I-KE.L3")
botao_escrever.click()
botao_destinatario = navegador.find_element("css selector", "agP.aFw")
botao_destinatario.click()
navegador.send_keys("pedrohenriquepvalente@gmail.com")
navegador.send_keys(Keys.ENTER)

time.sleep(10)
navegador.quit()
