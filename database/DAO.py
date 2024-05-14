from database.DB_connect import DBConnect
from model.country import Country
from model.connessioni import Connect

class DAO():

    @staticmethod
    def vertici(y):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = '''select state1ab ,state1no 
                from contiguity c  
                join country c2 on c.state1no =c2.CCode 
                where `year` <= %s
                group by state1ab ,state1no  '''

        cursor.execute(query, (y,))

        for row in cursor:
            result.append(Country(row['state1ab'],row['state1no']))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def archi(y):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = ''' select *
                    from contiguity c 
                    where `year` <= %s and conttype =1'''

        cursor.execute(query, (y,))

        for row in cursor:
            result.append(Connect(**row))

        cursor.close()
        conn.close()
        return result