from Poarta import Poarta
import csv

class PoartaTXT(Poarta):

    def _readFile(self,name):
        if self._fileExists(self.path+'/'+name):
            with open(self.path+'/'+name,'r') as txtfile:
                lines=txtfile.readlines()
                for i in range(len(lines)-1,-1,-1):
                    lines[i]=lines[i].replace('; \n','')
                    lines[i]=lines[i].replace(';\n','')
                return lines
        return []

    def _save_to_database(self,name):
        lines=self._readFile(name)
        for line in lines:
            list=line.split(',')
            dict=self._list_to_dict(list,['IDPersoana','Data','Sens'])
            dict['IDPoarta']=name.split('.')[0].split(('ta'))[1]
            self.database._insert(dict)

class PoartaCSV(Poarta):

    def _readFile(self,name):
        list=[]
        if self._fileExists(self.path+'/'+name):
            with open(self.path+'/'+name,'r') as csvfile:
                reader=csv.reader(csvfile)
                next(reader, None) 
                for row in reader:
                    list.append(row)
        return list

    def _save_to_database(self,name):
        rows=self._readFile(name)
        for row in rows:
            dict=self._list_to_dict(row,['IDPersoana','Data','Sens'])
            dict['IDPoarta']=name.split('.')[0].split(('ta'))[1]
            self.database._insert(dict)