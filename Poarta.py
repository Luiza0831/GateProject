from abc import ABC,abstractmethod
import os,datetime

class Poarta(ABC):

    def __init__(self,path,database):
        self.path=path
        self.database=database

    def _fileExists(self,path):
        return os.path.exists(path)
    
    def _list_to_dict(self,list,keys):
        dict={}
        if len(list)==len(keys):
            for i in range(len(list)):
                dict[keys[i]]=list[i]
        return dict
    
    def entrance(self,id,sens,checkID):
        if checkID!=None:
            list=[id,datetime.datetime.now(),sens]
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