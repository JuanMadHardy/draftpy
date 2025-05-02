from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("/home/devmadhardy/projects/draftpy/src/chromedrv/chromedriver")
driver = webdriver.Chrome(service=service)


# Specify the path to your ChromeDriver (or other browser driver)
# If it's in your PATH, you can skip this line
#driver = webdriver.Chrome(executable_path="/home/devmadhardy/projects/draftpy/src/chromedrv/chromedriver"))

# If the driver is in your system's PATH, you can simply do:
#driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://www.nfl.com/draft/tracker/teams/buffalo-bills/2025")

# Print the title of the page
print(f"Title of the page: {driver.title}")

# Close the browser
driver.quit()