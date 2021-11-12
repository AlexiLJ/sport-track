#TODO write class that creates and/or writes into SQLite db
import sqlite3

def insert_data(table):
    con = sqlite3.connect('test.db')

    cur = con.cursor()

    cur.execute(f""""CREATE TABLE IF NOT EXISTS {table} (date text, name text)""")

    cur.execute(f'''INSERT INTO {table} VALUES ('15/03/1994', 'mamat')''')

# TODO write service that synchronize Spreadsheets with db an vice versa
# accordingly to the time stamp 

# enable excell sheets functionality???
if __name__ == "__main__":
    insert_data('jebocka')