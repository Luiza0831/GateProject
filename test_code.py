import pytest,datetime,threading,os,time,csv
from CheckWorkHours import CheckWorkHours
from ConMySQL import Con_MySQL
from EmailSender import EmailSender
from FileCheck import FileCheck
from PoartaTip2 import PoartaTip2
from Utilizatori import utilizatori
from PoartaTip1 import *
from FlaskServer import *

@pytest.fixture
def ConnAngajati():
    return Con_MySQL('localhost','root','root','birouri_test','angajati_test')

@pytest.fixture
def ConnAccess():
    return Con_MySQL('localhost','root','root','birouri_test','access_test')

@pytest.fixture
def Angajati(ConnAngajati):
    return utilizatori(ConnAngajati)

@pytest.fixture
def query():
    return 'SELECT IDAccess FROM birouri_test.access_test;'

def test_inregistrez_utilizator(Angajati):
    lista=Angajati._lista_angajati()
    angajat={
        'Nume':'Alexandru',
        'Prenume':'Luiza-Cristina',
        'Companie':'Test',
        'IDManager':'1'
    }
    Angajati._inregistrez_utilizator(angajat)
    lista_noua=Angajati._lista_angajati()
    assert len(lista_noua)==len(lista)+1

def test_poarta_tip2(ConnAccess,query):
    Poarta2=PoartaTip2(ConnAccess)
    access=(ConnAccess._select(query))[-1][-1]
    Poarta2.inregistreaza_access_db(1,'in',4,checkID(1))
    access_nou=(ConnAccess._select(query))[-1][-1]
    assert access_nou==access+1
    
def test_file_check(ConnAccess,query):
    CheckFiles=FileCheck('testing/intrariTest',ConnAccess)
    access=(ConnAccess._select(query))[-1][-1]
    t1=threading.Thread(target=CheckFiles.startProgram)
    t1.start()
    time.sleep(5)
    pathTXT='testing/intrariTest/Poarta1.txt'
    with open(pathTXT,'w')as file:
        file.write('1,2023-05-21T13:49:51.141Z,in;\n1,2023-05-21T13:52:53.142Z,out;')
    time.sleep(5)
    dir=os.listdir('testing/intrariTest/backup/')
    access_nou=(ConnAccess._select(query))[-1][-1]
    assert len(dir)==1 and dir[0].split('.')[1]=='txt' and access_nou==access+2

    pathCSV='testing/intrariTest/Poarta2.csv'
    with open(pathCSV,'w',newline='')as csvfile:
        writer=csv.writer(csvfile)
        list=[['IdPersoana','Data','Sens'],['1','2023-05-21T13:49:51.141Z','in'],['1','2023-05-21T13:52:53.142Z','out']]
        writer.writerows(list)
    time.sleep(5)
    dir=os.listdir('testing/intrariTest/backup/')
    access_nou=(ConnAccess._select(query))[-1][-1]
    assert len(dir)==2 and dir[1].split('.')[1]=='csv' and access_nou==access+4

def test_check_work_hours(ConnAccess,ConnAngajati,Angajati):
    path='testing/adminDetails_test.json'
    Admins=admin_details(path,'read')
    Email=EmailSender('alexandru97luiza.cristina@gmail.com')
    CheckHours=CheckWorkHours(ConnAccess,ConnAngajati,Angajati,'testing/intrariTest/backup',datetime.datetime.now().hour,Email)
    time.sleep(5)
    admin=Admins[0]
    t1=threading.Thread(target=CheckHours.start(admin))
    t1.start()
    name=f'{datetime.datetime.now().date()}_chiulangii'
    dir=os.listdir('testing/intrariTest/backup/')
    assert (name+'.txt') in dir and (name+'.csv') in dir