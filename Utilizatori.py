class utilizatori():

    def __init__(self,angajatiMySQL):
        self.angajatiMySQL=angajatiMySQL
        self.listaAngajati=[]
        angajatiDB=self.angajatiMySQL._select(f'SELECT * FROM `{self.angajatiMySQL.db}`.`{self.angajatiMySQL.table}`;')
        for angajat in angajatiDB:
            self.listaAngajati.append(self.__tupple_to_dict(angajat,['ID','Nume','Prenume','Companie','IDManager']))

    def _inregistrez_utilizator(self,utilizator):
        self.angajatiMySQL._insert(utilizator)
        utilizator['ID']=(self.angajatiMySQL._select('SELECT last_insert_id()'))[0][0]
        self.listaAngajati.append(utilizator)
        return 'Utilizator inregistrat cu succes!'

    def __tupple_to_dict(self,tuple,list):
        dict={}
        if len(tuple)==len(list):
            for i in range(len(tuple)):
                dict[list[i]]=self.__str_or_list(tuple[i])
        return dict
