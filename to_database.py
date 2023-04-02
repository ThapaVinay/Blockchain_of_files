# it is the code to make the table back from the .sql file


import mysql.connector

# Connect to MySQL server
mydb = mysql.connector.connect(
  host="localhost",
  user="vinay",
  password="vinay",
  database="test"
)

# Create cursor object
mycursor = mydb.cursor()

# Read SQL file
with open('series.sql', 'r') as f:
    sql = f.read()

# Execute SQL commands
for result in mycursor.execute(sql, multi=True):
    pass  # Need to consume results due to "multi=True"

# Commit changes
mydb.commit()

# Close connection
mycursor.close()
mydb.close()
