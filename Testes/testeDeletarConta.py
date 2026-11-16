import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_loginUsuario():
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

        WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//a[contains(text(),'Logged in as')]")
            )
        )

        deletarConta = navegador.find_element(
            By.XPATH,
            '//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a'
        )
        deletarConta.click()

        time.sleep(5)

        WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Account Deleted!')]")
            )
        )

        navegador.save_screenshot("Evidencias/CT08_deletar_conta.png")

    finally:
        time.sleep(5)
        navegador.quit()