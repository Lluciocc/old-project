# On importe les différents modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# On définit les options du webdriver pour Chrome
chrome_options = Options()

# On initialise le webdriver
driver = webdriver.Chrome(
    executable_path="./chromedriver",
    chrome_options=chrome_options
)

# On accède à la page d'accueil du site de python
driver.get("https://www.wakanim.tv/fr/v2/catalogue")

# On récupère tous les liens de la barre de navigation
liens = driver.find_elements(By.CLASS_NAME, "catalog_item")

# On fait le tour des liens trouvés
for lien in liens:
    genres = lien.find_elements(By.CSS_SELECTOR , ".tooltip .tooltip_genre")
    texte_genre  = []
    anime = lien.find_elements(By.TAG_NAME , "href")

    for genre in genres:
        t = genre.get_attribute('innerHTML')
        

        texte_genre.append(t)
        
    
    titre = lien.find_element(By.CSS_SELECTOR , ".slider_item_title strong").text#.get_attribute('text_content')
    print(titre.ljust(40)  + "  " +"".join(texte_genre) + anime.rjust(50))

print("J AI FINI")
# On referme le driver
driver.close()

