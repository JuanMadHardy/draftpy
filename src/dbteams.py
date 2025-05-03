import yaml
import mysql.connector
import os

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kuko8701",
    database="draft"
)


path = os.getcwd()
print(path)


cursor = db.cursor()

with open(path + "/teams.yaml", "r") as file:
    data = yaml.safe_load(file)

# Loop through list inside dictionary
for team in data["teams"]:
    # Insert data into MySQL
    cursor.execute("INSERT INTO teams (name, slug) VALUES (%s, %s)", (team['name'], team['slug']))
    db.commit()

# Close connection
cursor.close()
db.close()

