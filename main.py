from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

navegador = webdriver.Chrome()
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

navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})",
                         produto1)
produto1.click()


time.sleep(10)

# # Configuração do Driver
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
# driver.get('https://www.amazon.com.br')

# time.sleep(2)

# try:
#     # 1. Pesquisa (usando sua lógica mista)
#     barra_pesquisa = driver.find_element(By.ID, "twotabsearchtextbox")
#     barra_pesquisa.click()
#     time.sleep(1)
#     p.write('galaxy s25', interval=0.1)
#     p.press('enter')
    
#     # Aguarda os resultados carregarem
#     time.sleep(5)

#     # 2. Localizar os anúncios na página de resultados
#     # Na Amazon, os anúncios costumam ter o atributo 'data-asin'
#     anuncios = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

#     lista_links = []

#     print(f"Encontrados {len(anuncios)} anúncios na primeira página.\n")

#     for anuncio in anuncios[:5]:  # Limitando aos 5 primeiros para teste
#         asin = anuncio.get_attribute("data-asin")
        
#         if asin:
#             # Encontra o link dentro do anúncio
#             link_elemento = anuncio.find_element(By.TAG_NAME, "h2").find_element(By.TAG_NAME, "a")
#             url_completa = link_elemento.get_attribute("href")
            
#             print(f"ID (ASIN): {asin}")
#             print(f"Link: {url_completa}")
#             lista_links.append(url_
