import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_adicionar_ao_carrinho():
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

        navegador.execute_script("document.body.style.zoom='70%'")

        clicarLogin = navegador.find_element(
            By.XPATH,
            '//*[@id="form"]/div/div/div[1]/div/form/button'
        )
        clicarLogin.click()
        
        acessarAbaProdutos = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a')
            )
        )
        acessarAbaProdutos.click()
        
        navegador.execute_script("document.body.style.zoom='70%'")
        
        adicionarAoCarrinho = navegador.find_element(
            By.XPATH,
            '/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a'
        )
        adicionarAoCarrinho.click()
        
        irParaCarrinho = navegador.find_element(
            By.XPATH,
            '//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]'
        )
        irParaCarrinho.click()
        
        navegador.save_screenshot("Evidencias/CT04_adicionar_carrinho.png")
        
    finally:
        time.sleep(5)
        navegador.quit()