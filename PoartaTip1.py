from Poarta import Poarta
import csv

class PoartaTXT(Poarta):

    def readFile(self,name):
        if self._fileExists(self.path+'/'+name):
            with open(self.path+'/'+name,'r') as txtfile:
                lines=txtfile.readlines()
                for i in range(len(lines)-1,-1,-1):
                    lines[i]=lines[i].replace('; \n','')
                    lines[i]=lines[i].replace(';\n','')
                return lines
        return []
    
    def generateFile(self,name,list):
        with open(self.path+'/'+name,'w') as txtfile:
            for line in list:
                txtfile.write(line+'\n')

    def save_to_database(self,name):
        lines=self.readFile(name)
        for line in lines:
            list=line.split(',')
            dict=self._list_to_dict(list,['IDPersoana','Data','Sens'])
            dict['IDPoarta']=name.split('.')[0].split(('ta'))[1]
            self.database._insert(dict)

class PoartaCSV(Poarta):

    def readFile(self,name):
        list=[]
        if self._fileExists(self.path+'/'+name):
            with open(self.path+'/'+name,'r') as csvfile:
                reader=csv.reader(csvfile)
                for row in reader:
                    list.append(row)
        return list

    def generateFile(self,name,list):
        with open(self.path+'/'+name,'w',newline='') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerows(list)

    def save_to_database(self):
        pass