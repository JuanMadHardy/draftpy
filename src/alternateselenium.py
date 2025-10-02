from logging import basicConfig, error, info, INFO
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml
import os
import logging
from selenium.common.exceptions import TimeoutException


# Configuración de logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constantes
DRAFT_URL = os.getenv(
    "DRAFT_URL", "https://www.nfl.com/draft/tracker/teams/buffalo-bills/2025"
)
TEAM_SITE = os.getenv("TEAM_SITE", "https://www.nfl.com/international")
PICKS_YAML = os.getenv("PICKS_YAML", "picks.yaml")

# Definir correctamente la ruta del chromedriver
CHROMEDRIVER_PATH = os.getenv(
    "CHROMEDRIVER_PATH", "/home/mainhead/projects/draftpy/src/chromedrv/chromedriver"
)
DRAFT_URL = os.getenv(
    "DRAFT_URL", "https://www.nfl.com/draft/tracker/teams/buffalo-bills/2025"
)
ADDAM_SCHEFTER = os.getenv(
    "ADDAM_SCHEFTER", "https://www.espn.com/contributor/adam-schefter"
)

TEAM_SITE = os.getenv("TEAM_SITE", "https://www.nfl.com/international")
PICKS_YAML = os.getenv("PICKS_YAML", "picks.yaml")

service = Service(CHROMEDRIVER_PATH)
options = Options()
options.add_argument("--headless")  # Run in headless mode (no GUI)
# options.add_argument("--no-sandbox")  # Bypass OS security
driver = webdriver.Chrome(service=service, options=options)


# If the driver is in your system's PATH, you can simply do:
#driver = webdriver.Chrome()

# Navigate to a website
# driver.get("https://www.nfl.com/draft/tracker/teams/buffalo-bills/2025")

def get_data_picks(driver):
    driver.get("https://www.espn.com/contributor/adam-schefter")
    time.sleep(5)
    wait_time = 10  # segundos
    retries = 3
    for attempt in range(retries):
        try:
            data_picks = WebDriverWait(driver, wait_time).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//*[@data-test-id="facemask-column"]')
                )
            )
            if data_picks:
                return data_picks
        except TimeoutException as e:
            logging.warning(f"Intento {attempt + 1} fallido: {e}")
        except Exception as e:
            logging.error(f"Error inesperado: {e}")
        if attempt < retries - 1:
            time.sleep(5)
    return []


def get_footer_url_teams(driver):
    try:
        footer = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "footer"))
        )
        ul = footer.find_element(By.TAG_NAME, "ul")
        li_elements = ul.find_elements(By.TAG_NAME, "li")
        teams_urls = {}
        for li in li_elements:
            a_tag = li.find_element(By.TAG_NAME, "a")
            url = a_tag.get_attribute("href")
            # Solo aplicar regex si url no es None
            if url:
                match = re.search(r"https?://(?:www\.)?([^.]+)", url)
                team_name = match.group(1) if match else url
                if team_name:
                    teams_urls[team_name] = url
        logging.info(f"URLs encontradas en el footer: {teams_urls}")

        # Guardar en YAML con formato team: url
        with open("urls_teams.yaml", "w") as file:
            yaml.dump(teams_urls, file, default_flow_style=False)
        logging.info("Archivo urls_teams.yaml creado correctamente.")

        return teams_urls
    except Exception as e:
        logging.error(f"Error al obtener URLs del footer: {e}")
        return []


def get_adam_schefter_news(driver, retries=3, wait_time=40):
    for attempt in range(retries):
        try:
            driver.get(ADDAM_SCHEFTER)
            news_elements = WebDriverWait(driver, wait_time).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//section[contains(@class, "ContentList")]//a')
                )
            )
            news_links = [
                elem.get_attribute("href")
                for elem in news_elements
                if elem.get_attribute("href")
            ]
            if news_links:
                logging.info(f"Noticias encontradas: {news_links}")
                return news_links
        except TimeoutException as e:
            logging.warning(f"Intento {attempt + 1} fallido: {e}")
        except Exception as e:
            logging.error(f"Error inesperado: {e}")
        if attempt < retries - 1:
            time.sleep(5)
    return []


def main():
    picks = []
    try:
        # driver.get(DRAFT_URL)
        driver.get(TEAM_SITE)
        # data_picks = get_data_picks(driver)
        data_urls = get_footer_url_teams(driver)
        if not data_urls:
            logging.error(
                "No se pudieron encontrar los elementos después de varios intentos."
            )
            return
        # logging.info(f"DATA PICKS: {data_picks[3].text if len(data_picks) > 3 else 'No hay suficientes elementos'}")
        """ if len(data_picks) > 3:
            picks = data_picks[3].text.split("Rnd")
            logging.info(f"Elemento encontrado: {picks}")
        else:
            logging.warning("No hay suficientes elementos en data_picks para extraer picks.") """
    except Exception as e:
        logging.error(f"Error en main: {e}")
    finally:
        driver.quit()

    """ if picks:
        data = {"teams": [{"name": pick, "slug": pick.lower().replace(" ", "-")} for pick in picks]}
        try:
            with open(PICKS_YAML, "w") as file:
                yaml.dump(data, file, default_flow_style=False)
            logging.info("YAML file created successfully!")
        except Exception as e:
            logging.error(f"Error al escribir el archivo YAML: {e}") """


if __name__ == "__main__":
    main()
