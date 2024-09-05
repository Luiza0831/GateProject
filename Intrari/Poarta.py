from abc import ABC,abstractmethod
import os,datetime

class Poarta(ABC):

    def __init__(self,path,database):
        self.path=path
        self.database=database

    def _fileExists(self,path):
        return os.path.exists(path)
    
    def _getCurrentTime(self):
        return datetime.datetime.now()
    
    def _checkID(self,id):
        if type(id)==int or id.isdigit():
            check=self.database._select(f"SELECT `ID` FROM `{self.database.db}`.`{self.database.table}` WHERE `ID`= {id};")
            if check != []:
                return check[0][0]
        return None
    
    def _list_to_dict(self,list,keys):
        dict={}
        if len(list)==len(keys):
            for i in range(len(list)):
                dict[keys[i]]=list[i]
        return dict
    
    def entrance(self,id,sens):
        check=self._checkID(id)
        if check!=None:
            list=[id,self._getCurrentTime(),sens]
        return list

    @abstractmethod
    def save_to_database(self):
        pass

    @abstractmethod
    def generateFile(self):
        pass

    @abstractmethod
    def readFile(self):
        pass