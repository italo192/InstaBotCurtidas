#bot de curtida no instagram
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep 
from selenium.common.exceptions import NoSuchElementException

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR','--window-size= 800,600','--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)
        
    chrome_options.add_experimental_option('prefs', {
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,

    })

    #inicializando o webdriver
    driver= webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)
    return driver
#entrar no site do instgram
driver = iniciar_driver()
driver.get('https://www.instagram.com')
sleep(50)
# fazer login
usuario = ''
senha = ''
# nome do usuario
login = driver.find_element(By.XPATH,'//input[@name="username"]')
login.click()
login.send_keys(f'{usuario}')
sleep(5)
#senha do usuario
login = driver.find_element(By.XPATH,'//input[@name="password"]')
login.click()
login.send_keys(f'{senha}')
sleep(8)
# entrar
login = driver.find_element(By.XPATH,'//button[@class="_acan _acap _acas _aj1-"]')
login.click()
sleep(10)
# navegar ate a pagina
pagina = 'https://www.instagram.com/username/'
driver.get(f'{pagina}')
sleep(10)
#rolar a pagina
driver.execute_script("window.scrollTo(0,500);")
sleep(3)
#clicar na ultima postagem
post = driver.find_elements(By.XPATH,'seletor')
if len(post) > 0:
    # Clique no primeiro elemento (índice 0)
    post[0].click()
    sleep(5)
#verificar se ja foi curtida
selector = 'seletor'

# Encontrar elementos com o seletor CSS
elements = nome = driver.find_elements(By.CSS_SELECTOR,'seletor')

# Verificar se o primeiro elemento foi encontrado
if elements:
    primeiro_elemento = elements[0]
    texto_do_title = primeiro_elemento.get_attribute('textContent')
    
    if texto_do_title.strip() == "Curtir":
        # Encontrar elementos com o XPath especificado
        elementos_a_clicar = driver.find_elements(By.XPATH, 'seletor')

        # Verificar se existe pelo menos 4 elementos para clicar no quarto
        if len(elementos_a_clicar) >= 4:
            elementos_a_clicar[3].click()
        else:
            print("Não há elementos suficientes para clicar no quarto elemento.")
    else:
        print("O texto do título não é 'Curtir'.")
else:
    print(f"O elemento com o seletor '{selector}' NÃO está presente na página.")

sleep(86400)       

#verificar se ja foi curtida casonao tenha curtido curtir
input('')
