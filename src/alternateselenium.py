from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("/home/devmadhardy/projects/draftpy/src/chromedrv/chromedriver")
#options = Options()
#options.add_argument("--headless")  # Run in headless mode (no GUI)
#options.add_argument("--no-sandbox")  # Bypass OS security
driver = webdriver.Chrome(service=service)


# Specify the path to your ChromeDriver (or other browser driver)
# If it's in your PATH, you can skip this line
#driver = webdriver.Chrome(executable_path="/home/devmadhardy/projects/draftpy/src/chromedrv/chromedriver"))

# If the driver is in your system's PATH, you can simply do:
#driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://www.nfl.com/draft/tracker/teams/buffalo-bills/2025")
try:
    # Esperar hasta que el elemento esté presente
    selectTeam = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "team"))
    )
    teams = selectTeam.text.split("\n")
    print(f"tipo de elemento: {type(teams)}")
    print(f"Elemento encontrado: {teams}")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Print the title of the page
    #print(f"Title of the page: {driver.title}")
    # Close the browser
    driver.quit()