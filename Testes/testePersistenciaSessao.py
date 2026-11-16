import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def fechar_anuncio(navegador):
    try:
        WebDriverWait(navegador, 7).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "close-button"))
        ).click()
    except:
        pass

def test_persistencia_carrinho():
    navegador = webdriver.Chrome()
    
    try:
        navegador.maximize_window()
        navegador.get("https://www.automationexercise.com/")

        cadastroLogin = navegador.find_element(
            By.XPATH,
            '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a'
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

        navegador.execute_script("document.body.style.zoom='70%'")

        clicarLogin = navegador.find_element(
            By.XPATH,
            '//*[@id="form"]/div/div/div[1]/div/form/button'
        )
        clicarLogin.click()

        WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//a[contains(text(),'Logged in as')]")
            )
        )

        # Clica na aba de produtos
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a')
            )
        ).click()
        fechar_anuncio(navegador)
        
        navegador.execute_script("document.body.style.zoom='70%'")
        
        adicionarAoCarrinho = navegador.find_element(
            By.XPATH,
            '/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a'
        )
        adicionarAoCarrinho.click()

        clicarLogout = navegador.find_element(
            By.XPATH,
            '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]'
        )
        clicarLogout.click()

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

        navegador.execute_script("document.body.style.zoom='70%'")

        clicarLogin = navegador.find_element(
            By.XPATH,
            '//*[@id="form"]/div/div/div[1]/div/form/button'
        )
        clicarLogin.click()

        #Acessa o carrinho
        WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]')
            )
        ).click()
        fechar_anuncio(navegador)
        
        navegador.save_screenshot("Evidencias/CT09_persistencia_carrinho.png")
        
    finally:
        time.sleep(5)
        navegador.quit()