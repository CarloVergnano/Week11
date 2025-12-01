from database.DB_connect import DBConnect
from model.object import Object
from model.connessione import Connessione


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


    @staticmethod
    def readConnessioni(objects_dict):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select eo1.object_id as o1, eo2.object_id as o2, COUNT(*) as peso  
                from  exhibition_objects as eo1, exhibition_objects as eo2
                where eo1.exhibition_id = eo2.exhibition_id
                and eo1.object_id < eo2.object_id 
                group by eo1.object_id , eo2.object_id """
        cursor.execute(query)
        for row in cursor:
            o1 = objects_dict[row["o1"]]
            o2 = objects_dict[row["o2"]]
            peso = row["peso"]
            result.append(Connessione(o1, o2, peso))


        conn.close()
        cursor.close()
        return result