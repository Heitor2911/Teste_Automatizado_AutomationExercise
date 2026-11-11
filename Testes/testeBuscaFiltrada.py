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


def test_buscaFiltrada():
    navegador = webdriver.Chrome()
    
    try:
        navegador.maximize_window()
        navegador.get("https://www.automationexercise.com/")

        cadastroLogin = navegador.find_element(
            By.XPATH,
            '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a/i'
        )
        fechar_anuncio(navegador)
        cadastroLogin.click()

        acessarAbaProdutos = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.material-icons.card_travel'))
        )
        fechar_anuncio(navegador)
        acessarAbaProdutos.click()

        navegador.execute_script("document.body.style.zoom='70%'")

        acessarCategoria = navegador.find_element(
            By.XPATH,
            '//*[@id="accordian"]/div[2]/div[1]/h4/a'
        )
        fechar_anuncio(navegador)
        acessarCategoria.click()

        escolherEspecificacao = navegador.find_element(
            By.XPATH,
            '//*[@id="Men"]/div/ul/li[2]/a'
        )
        fechar_anuncio(navegador)
        escolherEspecificacao.click()

        navegador.execute_script("document.body.style.zoom='70%'")

        escolherProduto = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, 
            '/html/body/section/div/div[2]/div[2]/div/div[3]/div/div[2]/ul'))
        )
        fechar_anuncio(navegador)
        escolherProduto.click()

        time.sleep(2)
        
        navegador.save_screenshot("Evidencias/CT07_busca_categorizada.png")

    finally:
        time.sleep(5)
        navegador.quit()