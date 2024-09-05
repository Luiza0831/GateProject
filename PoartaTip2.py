import datetime

class PoartaTip2():
    def __init__(self,database):
        self.database=database

    def inregistreaza_access_db(self,id,sens,idPoarta,checkID):
        if checkID!=None:
            access={'IDPersoana':id,
                'Data':datetime.datetime.now(),
                'Sens':sens,
                'IDPoarta':idPoarta}
            self.database._insert(access)
            return 'Accessul angajatului a fost inregistrat cu succes!'
        return 'Id-ul persoanei nu exista in baza de date!'