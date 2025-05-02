import requests
from bs4 import BeautifulSoup
import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kuko8701",
    database="draft"
)
cursor = db.cursor()

# Scrape the webpage
url = "https://www.nfl.com/draft/tracker/teams/buffalo-bills/2025"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract data
title = soup.find("h1").text
description = soup.find("p").text

# Insert data into MySQL
cursor.execute("INSERT INTO teams (title, description) VALUES (%s, %s)", (title, description))
db.commit()

# Close connection
cursor.close()
db.close()
