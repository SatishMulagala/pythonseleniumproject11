import mysql.connector
class DBConnectionFile:
    def dbconnect(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Chinn@@mys440",
                                       database="seleniumproject")
        mycursor=conn.cursor()
        mycursor.execute("select * from project")
        data=mycursor.fetchall()
        return data
