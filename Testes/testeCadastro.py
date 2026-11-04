import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def test_cadastroUsuario():
    navegador = webdriver.Chrome()

    try:
        navegador.maximize_window()
        navegador.get("https://www.automationexercise.com/")

        cadastroLogin = navegador.find_element(
            By.XPATH,
            '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a/i'
        )
        cadastroLogin.click()

        realizaCadastro = navegador.find_element(
            By.XPATH,
            '//*[@id="form"]/div/div/div[3]/div/form/input[2]'
        )
        realizaCadastro.send_keys("Teste123")

        time.sleep(2)

        adicionaEmail = navegador.find_element(
            By.XPATH,
            '//*[@id="form"]/div/div/div[3]/div/form/input[3]'
        )
        adicionaEmail.send_keys("testeamazon985@gmail.com")

        time.sleep(2)

        clicaParaCadastrar = navegador.find_element(
            By.XPATH,
            '//*[@id="form"]/div/div/div[3]/div/form/button'
        )
        clicaParaCadastrar.click()

        FormCadastro = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="form"]/div/div/div/div[1]/h2'))
        )

        escolhaGenero = navegador.find_element(
            By.ID,
            'uniform-id_gender1'
        )
        escolhaGenero.click()

        definirSenha = navegador.find_element(
            By.ID,
            'password'
        )
        definirSenha.send_keys('Senha1234@')

        definirNome = navegador.find_element(
            By.ID,
            "first_name"
        )
        definirNome.send_keys('Teste')

        definirSobrenome = navegador.find_element(
            By.ID,
            "last_name"
        )
        definirSobrenome.send_keys('Automation')

        definirEndereco = navegador.find_element(
            By.ID,
            "address1"
        )
        definirEndereco.send_keys('Rua Existente, 123')

        pais = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.NAME, "country"))
        )

        selecaoPais = Select(pais)
        selecaoPais.select_by_visible_text("Canada")

        definirEstado = navegador.find_element(
            By.ID,
            'state'
        )
        definirEstado.send_keys('Paraná')

        definirCidade = navegador.find_element(
            By.ID,
            'city'
        )
        definirCidade.send_keys('Curitiba')

        definirCEP = navegador.find_element(
            By.ID,
            'zipcode'
        )
        definirCEP.send_keys('123456789')

        definirTelefone = navegador.find_element(
            By.ID,
            'mobile_number'
        )
        definirTelefone.send_keys('9876543210')

        criarConta = navegador.find_element(
            By.XPATH,
            '//*[@id="form"]/div/div/div/div[1]/form/button'
        )
        criarConta.click()

        criacaoConta = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="form"]/div/div/div/div/a'))
        )

        navegador.save_screenshot("Evidencias/CT01_criacao_conta.png")

        criacaoConta.click()

    finally:
        time.sleep(5)
        navegador.quit()