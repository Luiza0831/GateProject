import mysql.connector

class Con_MySQL():

    def __init__(self,host,user,password,db,table):
        self.host=host
        self.user=user
        self.password=password
        self.db=db
        self.table=table
        self.mydb=mysql.connector.connect(host=self.host,
                                          user=self.user,
                                          password=self.password,
                                          database=self.db,
                                          auth_plugin='mysql_native_password')
        self.cursor=self.mydb.cursor()

    def _select(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def _insert(self,dict:dict):
        query=f'INSERT INTO `{self.db}`.`{self.table}` VALUES('
        for key in dict:
            if type(dict[key])==int or dict[key]=='null':
                query+=f"{dict[key]},"
            else:
                query+=f"'{dict[key]}',"
        query=query[:-1]
        query+=');'
        self.cursor.execute(query)
        self.mydb.commit()
        return 'Dictionarul atasat a fost inserat in baza de date!'
        
    def _update(self,id:int,dict:dict):
        query=f'UPDATE `{self.db}`.`{self.table}` SET '
        for key in dict:
            if type(dict[key])==int or dict[key]=='null':
                query+=f"`{key}` = {dict[key]},"
            else:
                query+=f"`{key}` = '{dict[key]}',"
        query=query[:-1]
        query+=f' WHERE `ID` = {id};'
        self.cursor.execute(query)
        self.mydb.commit()
        return 'Datele introduse au fost updatate!'

    def _delete(self,id:int):
        self.cursor.execute(f'DELETE FROM `{self.db}`.`{self.table}` WHERE `ID` = {id};')
        self.mydb.commit()
        return 'Datele au fost sterse!'