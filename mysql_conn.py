import pymysql

class MySQLConn:
    __props=None
    def __init__(self, props):
        self.__props=props

    def getConn(self):
        connection = pymysql.connect(
            host=self.__props['host'],
            user=self.__props['user'],
            password=self.__props['password'],
            db=self.__props['db'],
            ssl_disabled=True  # optional if no SSL
        )
        return connection
    async def query (self,sql, values=None):
        conn=self.getConn()
        cursor=conn.cursor()

        if values!=None:
            cursor.execute(sql, values)
        else:
            cursor.execute(sql)
        results = cursor.fetchall()
        cursor.close()
        conn.commit()
        print(results)
        return results