from PoartaTip1 import *
import os,time

class FileCheck():

    def __init__(self,path):
        self.path=path
        os.makedirs(self.path+'/backup')

    def __backup(self,name):
        os.rename(self.path+'/backup/'+name)

    def __listener(self):
       while True:
            files=os.listdir(self.path)
            for file in files:
                if file.endswith('.txt'):
                    pass
                elif file.endswith('.csv'):
                    pass
            time.sleep(3)