import sqlite3 as sql

def main():
    try: 
        db = sql.connect('Novi_BukuTelephone.db')
        cur = db.cursor()
        tablequery = "CREATE TABLE Users (id INT, namalengkap TEXT, prodi TEXT, kota TEXT, telefon TEXT, email TEXT)"

        cur.execute(tablequery)
        print("Table Created Succesfully")

    except sql.Error as e:
        print("There is a table or an error has occurred")

    finally:
        db.close()
        
if __name__ == "__main__":
    main()