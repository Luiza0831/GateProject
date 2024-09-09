from Utilizatori import utilizatori
from ConMySQL import Con_MySQL
from FileCheck import FileCheck
from CheckWorkHours import CheckWorkHours
from EmailSender import EmailSender
from PoartaTip2 import *
import hashlib,json,os

def admin_details(path,method,newcontent=None):
    if method=='read':
        if os.path.exists(path):
            with open(path,'r')as jsonfile:
                content=json.load(jsonfile)
                return content
        else:
            return []
    elif method=='write' and newcontent!=None:
        with open(path,'w')as jsonfile:
            json.dump(newcontent,jsonfile)
            return 'Am salvat!'

def hash_password(password):
    return hashlib.md5(str(password).encode('utf-8')).hexdigest()

path='adminDetails.json'
conAngajati=Con_MySQL('localhost','root','root','birouri','angajati')
conAccess=Con_MySQL('localhost','root','root','birouri','access')
angajati=utilizatori(conAngajati)
admins=admin_details(path,'read')
current_admin=admins[0]
poartatip2=PoartaTip2(conAccess)
Checker=FileCheck('Intrari',conAccess)
emailSender=EmailSender('alexandru97luiza.cristina@gmail.com')
checkHours=CheckWorkHours(conAccess,conAngajati,angajati,'Intrari/Backup','20',emailSender)

def checkID(id):
    if type(id)==int or id.isdigit():
        check=conAngajati._select(f"SELECT `ID` FROM `{conAngajati.db}`.`{conAngajati.table}` WHERE `ID`= {id};")
        if check != []:
            return check[0][0]
    return None

def checkSens(id):
    check=conAccess._select(f'SELECT `Sens` FROM `{conAccess.db}`.`{conAccess.table}` WHERE `IDPersoana`={id} ORDER BY `Data`;')
    if check!=[]:
        if check[-1][-1]=='in':
            return 'out'
        else:
            return 'in'
    return 'in'
