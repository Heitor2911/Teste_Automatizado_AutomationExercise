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

def test_realizar_checkout():
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
        
        irParaCarrinho = navegador.find_element(
            By.XPATH,
            '//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]'
        )
        irParaCarrinho.click()

        clicarParaCheckout = navegador.find_element(
            By.XPATH,
            '//*[@id="do_action"]/div[1]/div/div/a'
        )
        clicarParaCheckout.click()
        fechar_anuncio(navegador)

        fazerPedido = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="cart_items"]/div/div[7]/a')
            )
        )
        fazerPedido.click()

        nomeCartao = navegador.find_element(
            By.XPATH,
            '//*[@id="payment-form"]/div[1]/div/input'
        )
        nomeCartao.send_keys('Testando')

        numeroCartao = navegador.find_element(
            By.XPATH,
            '//*[@id="payment-form"]/div[2]/div/input'
        )
        numeroCartao.send_keys('1234567')

        numeroCVC = navegador.find_element(
            By.XPATH,
            '//*[@id="payment-form"]/div[3]/div[1]/input'
        )
        numeroCVC.send_keys('123')

        mesExpiracao = navegador.find_element(
            By.XPATH,
            '//*[@id="payment-form"]/div[3]/div[2]/input'
        )
        mesExpiracao.send_keys('12')

        anoExpiracao = navegador.find_element(
            By.XPATH,
            '//*[@id="payment-form"]/div[3]/div[3]/input'
        )
        anoExpiracao.send_keys('2697')

        clicarPagar = navegador.find_element(
            By.ID,
            'submit'
        )
        clicarPagar.click()

        WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Order Placed!')]")
            )
        )
        
        navegador.save_screenshot("Evidencias/CT10_checkout_realizado.png")
        
    finally:
        time.sleep(5)
        navegador.quit()