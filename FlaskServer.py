from flask import Flask,request
from Utilizatori import utilizatori
from ConMySQL import Con_MySQL
conAngajati=Con_MySQL('localhost','root','root','birouri','angajati')
angajati=utilizatori(conAngajati)

app=Flask(__name__)

@app.route('/')
def home():
    pass
@app.route('/inregistrare',methods=['POST'])
def inregistrare():
    inputs=request.json
    angajati._inregistrez_utilizator(inputs)
    return angajati.listaAngajati

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
