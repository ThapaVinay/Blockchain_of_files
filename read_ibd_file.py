# to export the file from the database : mysqldump -u vinay -p series_manage sereis > series.sql

# reading a .sql file
with open('series.sql', 'r') as f:
    sql = f.read()
    print(sql)

print(type(sql))