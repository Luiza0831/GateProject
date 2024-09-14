import os,datetime,csv

class CheckWorkHours():

    def __init__(self,conAccess,conAngajati,angajati,path,running_hour,emailSender):
        self.conAccess=conAccess
        self.conAngajati=conAngajati
        self.angajati=angajati
        self.path=path
        self.running_hour=running_hour
        self.emailSender=emailSender

    def __generateBackupDirectory(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)
    
    def __readLastCheckedID(self):
        if os.path.exists(self.path+'/lastID.txt'):
            with open(self.path+'/lastID.txt','r') as file:
                return file.read()
        return 1

    def __writeLastCheckedID(self,lastID):
        with open(self.path+'/lastID.txt','w') as file:
            file.write(str(lastID))

    def __getLastID(self):
        lastID=self.conAccess._select(f'SELECT `IDAccess` FROM `{self.conAccess.db}`.`{self.conAccess.table}`;')
        return lastID[-1][0]
    
    def __convert(self,n):
        m=0
        while n>=60:
            m+=1
            n-=60
        return m,n
    
    def __scadere(self,a,b):
        if a>=b:
            return a-b
        else:
            return 60+a-b
    
    def __checkIfFileExists(self,path):
        if os.path.exists(path):
            return 'a'
        else:
            return 'w'

    def __intrariAngajat(self,id,lastID):
        intrari=self.conAccess._select(f'SELECT `Data` FROM `{self.conAccess.db}`.`{self.conAccess.table}` WHERE `IDPersoana` = {id} and `IDAccess` > {lastID} ORDER BY `Data`;')
        intrariPeZi={}
        lista=[]
        for intrare in intrari:
            data=intrare[0].split('T')[0]
            if data not in intrariPeZi.keys():
                lista=[]
            lista.append(intrare[0].split('T')[1].split('.')[0])
            intrariPeZi[data]=lista
        return intrariPeZi

    def __workHours(self,id,lastID):
        intrariPeZi=self.__intrariAngajat(id,lastID)
        keys=intrariPeZi.keys()
        for zi in keys:
            oreLucratePeZi=''
            sumaOre=0
            sumaMinute=0
            sumaSecunde=0
            for i in range(0,len(intrariPeZi[zi]),2):
                try:
                    hms_in=intrariPeZi[zi][i].split(':')
                    hms_out=intrariPeZi[zi][i+1].split(':')
                    sumaSecunde+=self.__scadere(int(hms_out[2]),int(hms_in[2]))
                    sumaMinute+=self.__scadere(int(hms_out[1]),int(hms_in[1]))
                    sumaOre+=int(hms_out[0])-int(hms_in[0])
                except IndexError:
                    pass
            aux=self.__convert(sumaSecunde)
            sumaSecunde=aux[1]
            sumaMinute+=aux[0]
            aux=self.__convert(sumaMinute)
            sumaMinute=aux[1]
            sumaOre+=aux[0]
            oreLucratePeZi=f'{sumaOre}:{sumaMinute}:{sumaSecunde}'
            intrariPeZi[zi]=oreLucratePeZi
        return intrariPeZi

    def __verificTotiAngajatii(self,lastID,companie):
        listaAngajati=self.angajati._lista_angajati()
        oreLucrateTotiAngajati=[]
        for angajat in listaAngajati:
            if companie==angajat['Companie']:
                oreLucrate=self.__workHours(angajat['ID'],lastID)
                if oreLucrate!={}:
                    oreLucrateAngajat={'ID':angajat['ID'],
                                       'Nume':angajat['Nume'],
                                       'Prenume':angajat['Prenume'],
                                       'OreLucrate':oreLucrate}
                    oreLucrateTotiAngajati.append(oreLucrateAngajat)
        return oreLucrateTotiAngajati
    
    def __writeTXTandCSV(self,list):
        if list!=[]:
            dataCurenta=f'{datetime.datetime.now().date()}'
            path=self.path+'/'+dataCurenta+'_chiulangii.'
            txtmode=self.__checkIfFileExists(path+'txt')
            with open(path+'txt',txtmode) as file:
                for row in list:
                    file.write(row[0]+','+row[1]+';\n')
            csvmode=self.__checkIfFileExists(path+'csv')
            with open(path+'csv',csvmode) as csvfile:
                writer=csv.writer(csvfile)
                if csvmode=='w':
                    header=['Nume','OreLucrate']
                    writer.writerow(header)
                writer.writerows(list)

    def start(self,currentAdmin):
        hr=self.running_hour
        if str(hr)==str(datetime.datetime.now().hour):
            list=[]
            lastID=self.__readLastCheckedID()
            listaAngajati=self.__verificTotiAngajatii(lastID,currentAdmin.get('Companie'))
            for angajat in listaAngajati:
                for zi in angajat['OreLucrate'].keys():
                    if angajat['OreLucrate'][zi].split(':')[0]<'8':
                        print('Angajatul n-a lucrat destul')
                        listaOre=[f'{angajat['Nume']} {angajat['Prenume']}',f'{zi}-{angajat['OreLucrate'][zi]}']
                        list.append(listaOre)
                        message=f"""Angajatul cu numele {angajat['Nume']} {angajat['Prenume']} a chiulit de la munca in data de {zi}.
A lucrat numai {angajat['OreLucrate'][zi].split(':')[0]} ore si {angajat['OreLucrate'][zi].split(':')[1]} minute."""
                        managerAngajat=self.conAngajati._select(F'SELECT `IDManager` FROM `{self.conAngajati.db}`.`{self.conAngajati.table}` WHERE `ID` = {angajat['ID']}')
                        if managerAngajat[0][0]!=None:
                            print('Am trimis Email catre managerul angajatului!')
                            managerEmail=currentAdmin['Manageri'][f'{managerAngajat[0][0]}']
                            self.emailSender._send_email(message,managerEmail)
                        else:
                            print('Am trimis Email catre administratorul firmei!')
                            self.emailSender._send_email(message,currentAdmin['Email'])
            self.__generateBackupDirectory()
            self.__writeTXTandCSV(list)
            self.__writeLastCheckedID(self.__getLastID())