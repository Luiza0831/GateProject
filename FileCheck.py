from PoartaTip1 import *
import os,time

class FileCheck():

    def __init__(self,path,database):
        self.path=path
        self.database=database
        self.txtfile=PoartaTXT(self.path,self.database)
        self.csvfile=PoartaCSV(self.path,self.database)
        self.txtfile._generateBackupDirectory()
        self.__listener()

    def __listener(self):
       while True:
            print('working..')
            files=os.listdir(self.path)
            for file in files:
                if file.endswith('.txt'):
                    print('file saved')
                    self.txtfile._save_to_database(file)
                    self.txtfile._generateBackupFile(file)
                elif file.endswith('.csv'):
                    print('file saved')
                    self.csvfile._save_to_database(file)
                    self.csvfile._generateBackupFile(file)
            time.sleep(5)