import sqlite3


DB = 'database.sql'

with open('Words.md', 'r') as f:
    x = f.readlines()[2:]


def data_loader():
    try:
        c = 0
        conn = sqlite3.connect(DB)
        db = conn.cursor()
        cmd = 'INSERT INTO ZEALOT (slang,acc_word,definition) values(?,?,?)'
        for i in x:
            slang = str(i.split('|')[0])
            acc_word = str(i.split('|')[1])
            definition = str(i.split('|')[2])
            db.execute(cmd, (slang, acc_word, definition))
            c += 1

        conn.commit()
        return c
    except:
        pass
    finally:
        conn.close()


print(data_loader())   # returns the count of rows inserted
