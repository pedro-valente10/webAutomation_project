# WebAutomation_project

🤖 Web Automation & Gmail Integration

Este projeto é uma automação web que utiliza **Selenium** para buscar preços de produtos na Amazon Brasil e a **API do Gmail** para enviar os resultados capturados automaticamente por e-mail.

## 🚀 Funcionalidades
* Faz busca automatizada de produtos (ex: Galaxy S25).
* Extrai o nome e o preço atualizado diretamente do site.
* Autentica de forma segura com a API do Google.
* Envia um e-mail formatado com os detalhes do produto encontrado.

## 🛠️ Tecnologias Utilizadas
* **Python 3.x**
* **Selenium WebDriver**: Para navegação e web scraping.
* **Google APIs Client Library**: Para integração com Gmail (OAuth2).
* **Chrome WebDriver**: Para controle do navegador.

## 📋 Pré-requisitos

Antes de rodar o script, você precisará:
1. Instalar as bibliotecas necessárias:
   ```bash
   pip install selenium google-auth-oauthlib google-api-python-client
   ```
2. Ter o Google Chrome instalado.

## 🔐 Configuração das Credenciais (Importante)

Para que o envio de e-mail funcione, você deve configurar suas próprias credenciais do Google Cloud:

1. Vá ao [Google Cloud Console](https://console.cloud.google.com/).
2. Crie um novo projeto e habilite a **Gmail API**.
3. Em "Credentials", crie um **OAuth 2.0 Client ID** (tipo: Desktop App).
4. Baixe o arquivo JSON, renomeie para `credentials.json` e coloque na raiz deste projeto.
5. **Nota:** O arquivo `token.json` será gerado automaticamente após a primeira execução e autenticação no navegador.

> ⚠️ **Atenção:** Os arquivos `credentials.json` e `token.json` estão listados no `.gitignore` e não devem ser enviados para repositórios públicos por questões de segurança.

## 💻 Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/pedro-valente10/webAutomation_project.git
   ```
2. Navegue até a pasta e execute o script:
   ```bash
   python nome_do_seu_arquivo.py
   ```

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

---
Feito por [Pedro Valente](https://github.com/pedro-valente10)

---
