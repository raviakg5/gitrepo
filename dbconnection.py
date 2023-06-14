import mysql.connector


class Dbconnection :
     def get_connection_db(self):

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234",
                database="ab",

            )

            return connection
        except Exception as e:
            print(f"database connectivity error {e}")



