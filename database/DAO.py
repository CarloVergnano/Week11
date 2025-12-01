from database.DB_connect import DBConnect
from model.object import Object


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def readObjects():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = "select * from objects"
        cursor.execute(query)
        for row in cursor:
            result.append(Object(row["object_id"], row["object_name"], row["title"]))
            # result.append(Object(**row))  ** fa l'unpacking del dizionario

        conn.close()
        cursor.close()
        return result