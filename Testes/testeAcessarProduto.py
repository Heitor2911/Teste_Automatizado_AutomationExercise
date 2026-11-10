import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_acessarProduto():
    navegador = webdriver.Chrome()
    
    try:
        navegador.maximize_window()
        navegador.get("https://www.automationexercise.com/")
        
        cadastroLogin = navegador.find_element(
            By.XPATH,
            '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a/i'
        )
        cadastroLogin.click()

        acessarAbaProdutos = navegador.find_element(
            By.XPATH,
            '//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a'
        )
        acessarAbaProdutos.click()
        
        pesquisarProduto = navegador.find_element(
            By.ID,
            'search_product'
        )
        pesquisarProduto.send_keys("Blue Top")
        
        enviarBusca = navegador.find_element(
            By.ID,
            'submit_search'
        )
        enviarBusca.click()
        
        navegador.execute_script("document.body.style.zoom='70%'")

        time.sleep(2)
        
        acessarPrimeiroProduto = navegador.find_element(
            By.XPATH,
            '/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]'
        )
        acessarPrimeiroProduto.click()
        
        WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div'))
        )
        
        navegador.save_screenshot("Evidencias/CT03_acessar_produto.png")

    finally:
        time.sleep(5)
        navegador.quit()