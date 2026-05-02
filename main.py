from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import re

import os
import base64
from email.mime.text import MIMEText
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def autenticar():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

def criar_email(remetente, destinatario, assunto, mensagem):
    msg = MIMEText(mensagem)
    msg['to'] = destinatario
    msg['from'] = remetente
    msg['subject'] = assunto

    raw = base64.urlsafe_b64encode(msg.as_bytes())
    return {'raw': raw.decode()}

def enviar_email(service, mensagem):
    return service.users().messages().send(userId="me", body=mensagem).execute()

def flags(preco_produto):

    numeros = re.findall(r'\d+(?:[.,]\d+)*', preco_produto)
    if len(numeros) < 2:
        return "Erro: Formato de texto não reconhecido"
    
    parcelas = int(numeros[0])
    valor_parcela = float(numeros[1].replace('.', '').replace(',', '.'))
    valor_final = parcelas * valor_parcela

    if valor_final < 3500:
        return "Bandeira verde 🟢"
    elif valor_final < 4000:
        return "Bandeira amarela 🟡"
    else:
        return "Bandeira vermelha 🔴"


#busca usando o selenium
navegador = webdriver.Chrome()
time.sleep(2)
navegador.get("https://www.amazon.com.br/")
navegador.maximize_window()
time.sleep(5)
barra_pesquisa = navegador.find_element("id", "twotabsearchtextbox")
barra_pesquisa.click()
barra_pesquisa.send_keys("Galaxy S25")
barra_pesquisa.send_keys(Keys.ENTER)
time.sleep(2)

#localiza o container do produto pelo ASIN e clica no link
produto1 = navegador.find_element("css selector", f'div[data-asin="B0DSY665M3"] a.a-link-normal')
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", produto1)
produto1.click()

time.sleep(5)
nome_produto1 =  navegador.title
precoInt_produto1 = navegador.find_element("class name", "a-price-whole").text
precoFloat_produto1 = navegador.find_element("class name", "a-price-fraction").text
precoParcelado_produto1 = navegador.find_element("css selector", ".a-size-base.a-text-bold").text
flags_produto1 = flags(precoParcelado_produto1)
print(f"Nome - {nome_produto1}")
print(f"Preço à vista - R$ {precoInt_produto1},{precoFloat_produto1}")
print(f"Preço parcelado - {precoParcelado_produto1}")
print(f"{flags_produto1}")

#cria e manda o email
creds = autenticar()
service = build('gmail', 'v1', credentials=creds)

email = criar_email(
    "me",
    "pedrohenriquepvalente@gmail.com",
    "Preço do seu produto",
    f"""Bom dia, Pedro! Abaixo seguem as informações mais recentes do anúncio do seu próximo celular:\n
    Nome: {nome_produto1}
    {flags_produto1}
    Preço à vista: R$ {precoInt_produto1},{precoFloat_produto1}
    {precoParcelado_produto1}""")

enviar_email(service, email)

time.sleep(5)
navegador.quit()
