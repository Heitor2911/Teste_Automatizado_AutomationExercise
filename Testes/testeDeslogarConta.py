import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from PIL import Image

def test_deslogUsuario():
    navegador = webdriver.Chrome()
    
    try:
        navegador.maximize_window()
        navegador.get("https://www.automationexercise.com/")

        cadastroLogin = navegador.find_element(
            By.XPATH,
            '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a/i'
        )
        cadastroLogin.click()

        adicionaEmail = navegador.find_element(
            By.XPATH,
            '//*[@id="form"]/div/div/div[1]/div/form/input[2]'
        )
        adicionaEmail.send_keys("testeamazon985@gmail.com")

        EscreverSenha = navegador.find_element(
            By.XPATH,
            '//*[@id="form"]/div/div/div[1]/div/form/input[3]'
        )
        EscreverSenha.send_keys('Senha1234@')

        navegador.execute_script("document.body.style.zoom='80%'")

        clicarLogin = navegador.find_element(
            By.XPATH,
            '//*[@id="form"]/div/div/div[1]/div/form/button'
        )
        clicarLogin.click()

        time.sleep(2)
        navegador.save_screenshot("Evidencias/login.png")

        clicarLogout = navegador.find_element(
            By.XPATH,
            '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]'
        )
        clicarLogout.click()

        navegador.save_screenshot("Evidencias/logout.png")

        imagem_login = Image.open("Evidencias/login.png")
        imagem_logout = Image.open("Evidencias/logout.png")

        # Deixa ambas com a mesma altura
        altura = min(imagem_login.height, imagem_logout.height)

        largura_login = int(imagem_login.width * altura / imagem_login.height)
        largura_logout = int(imagem_logout.width * altura / imagem_logout.height)

        imagem_login = imagem_login.resize((largura_login, altura))
        imagem_logout = imagem_logout.resize((largura_logout, altura))

        # Cria uma nova imagem para colocar as duas lado a lado
        imagem_final = Image.new(
            "RGB",
            (largura_login + largura_logout, altura)
        )

        imagem_final.paste(imagem_login, (0, 0))
        imagem_final.paste(imagem_logout, (largura_login, 0))

        imagem_final.save("Evidencias/CT06_deslogar_conta.png")

    finally:
        time.sleep(5)
        navegador.quit()