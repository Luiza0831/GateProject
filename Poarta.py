from abc import ABC,abstractmethod
import os,datetime

class Poarta(ABC):

    def __init__(self,path,database):
        self.path=path
        self.database=database

    def _fileExists(self,path):
        return os.path.exists(path)
    
    def _generateBackupDirectory(self):
        if not self._fileExists(self.path):
            os.makedirs(self.path)
        if not self._fileExists(self.path+'/backup'):
            os.makedirs(self.path+'/backup')
    
    def _generateTime(self):
        date=str(datetime.datetime.now())
        dateSplit=date.split(' ')
        newdate=dateSplit[0]+'T'+(dateSplit[1].split('.'))[0]
        newdate=newdate.replace(':','-')
        return newdate

    def _generateBackupFile(self,name):
        if self._fileExists(self.path+'/'+name):
            splitName=name.split('.')
            newName=f'{splitName[0]}_{self._generateTime()}.{splitName[1]}'
            os.rename(self.path+'/'+name,self.path+'/backup/'+newName)
        return False

    def _list_to_dict(self,list,keys):
        dict={}
        if len(list)==len(keys):
            for i in range(len(list)):
                dict[keys[i]]=list[i]
        return dict

    @abstractmethod
    def _save_to_database(self):
        pass

    @abstractmethod
    def _readFile(self):
        pass