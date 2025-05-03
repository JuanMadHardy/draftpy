from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import yaml


service = Service("/home/mainhead/projects/draftpy/src/chromedrv/chromedriver")
options = Options()
options.add_argument("--headless")  # Run in headless mode (no GUI)
#options.add_argument("--no-sandbox")  # Bypass OS security
driver = webdriver.Chrome(service=service, options=options)
teams = []
dataPicks = []

# Specify the path to your ChromeDriver (or other browser driver)
# If it's in your PATH, you can skip this line
#driver = webdriver.Chrome(executable_path="/home/devmadhardy/projects/draftpy/src/chromedrv/chromedriver"))

# If the driver is in your system's PATH, you can simply do:
#driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://www.nfl.com/draft/tracker/teams/buffalo-bills/2025")
try:
    # Esperar hasta que el elemento esté presente
    """ selectTeam = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "team"))
    )"""
    dataPicks= WebDriverWait(driver, 40).until(
        #EC.visibility_of_element_located((By.XPATH, '//*[@data-test-id="facemask-column"]'))
        EC.presence_of_all_elements_located((By.XPATH, '//*[@data-test-id="facemask-column"]'))
    )
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

data = {"teams": [{"name": team, "slug": team.lower().replace(" ", "-")} for team in teams]}

""" with open("teams.yaml", "w") as file:
    yaml.dump(data, file, default_flow_style=False)

print("YAML file created successfully!")
"""