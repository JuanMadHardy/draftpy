from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml
import time

""" ojo hay que cambiar el path del chromedriver la carpeta por cada usuario
/home/devmadhardy/projects/draftpy/src/chromedrv/chromedriver
"""
service = Service("/home/devmadhardy/projects/draftpy/src/chromedrv/chromedriver")
options = Options()
options.add_argument("--headless")  # Run in headless mode (no GUI)
#options.add_argument("--no-sandbox")  # Bypass OS security
driver = webdriver.Chrome(service=service, options=options)
teams = []
dataPicks = []
picks = []

# Specify the path to your ChromeDriver (or other browser driver)
# If it's in your PATH, you can skip this line
#driver = webdriver.Chrome(executable_path="/home/devmadhardy/projects/draftpy/src/chromedrv/chromedriver"))

# If the driver is in your system's PATH, you can simply do:
#driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://www.nfl.com/draft/tracker/teams/buffalo-bills/2025")
time.sleep(5)
try:
    # Intentar encontrar los elementos con un bucle de reintento
    max_retries = 3
    retry_count = 0
    while retry_count < max_retries:
        try:
            dataPicks = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//*[@data-test-id="facemask-column"]'))
            )
            if dataPicks:
                break  # Salir del bucle si se encuentran los elementos
        except Exception as e:
            print(f"Intento {retry_count + 1} fallido: {e}")
            retry_count += 1
            time.sleep(5)  # Esperar 5 segundos antes de reintentar

    if not dataPicks:
        print("No se pudieron encontrar los elementos después de varios intentos.")
        driver.quit()
        exit(1)  # Salir del script si no se encuentran los elementos

    print(f"DATA PICKS: {dataPicks[3].text}")
    picks = dataPicks[3].text.split("Rnd")
    #teams = selectTeam.text.split("\n")
    #print(f"tipo de elemento: {type(teams)}")
    #print(f"Elemento encontrado: {teams}")
    print(f"Elemento encontrado: {picks}")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Print the title of the page
    #print(f"Title of the page: {driver.title}")
    # Close the browser
    driver.quit()

data = {"teams": [{"name": pick, "slug": pick.lower().replace(" ", "-")} for pick in picks]}

with open("picks.yaml", "w") as file:
    yaml.dump(data, file, default_flow_style=False)

print("YAML file created successfully!")
