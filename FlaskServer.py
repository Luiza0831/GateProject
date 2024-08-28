from flask import Flask,request,render_template
from Utilizatori import utilizatori
from ConMySQL import Con_MySQL
from adminDetails import *
import hashlib
conAngajati=Con_MySQL('localhost','root','root','birouri','angajati')
angajati=utilizatori(conAngajati)

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def frontlogin():
    return render_template('login.html')

@app.route('/userinsert')
def frontuserinsert():
    return render_template('userinsert.html')

@app.route('/adminlogin',methods=['POST'])
def login():
    inputs=request.form
    if inputs['Email']==email:
        if hashlib.md5(str(inputs['Password']).encode('utf-8')).hexdigest()==password:
            return  render_template('options.html')
        else:
            return 'Password doesnt match!'
    else:
        return 'Email doesnt match!'


@app.route('/inregistrare',methods=['POST'])
def inregistrare():
    inputs=request.form.to_dict()
    angajati._inregistrez_utilizator(inputs)
    return angajati.listaAngajati

if __name__=='__main__':
    app.run(host='0.0.0.0',port=4000,debug=True)
