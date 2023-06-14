from dbconnection import Dbconnection
conn = Dbconnection().get_connection_db()
class DBHelper:
    def executedbsqlquery(self,query=None):
        if query is not None :
            try:
                cursor = conn.cursor()

                cursor.execute(query)

                conn.commit()

            except Exception as e:
                print(f"Sql statement formation error {e}")
