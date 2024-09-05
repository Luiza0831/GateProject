from flask import Flask,request,render_template
from main import *

app=Flask(__name__)

@app.route('/')
def front_home():
    return render_template('home.html')

@app.route('/access')
def front_access():
    return render_template('access.html')

@app.route('/login')
def front_login():
    return render_template('login.html')

@app.route('/adauga/angajat')
def front_adauga_angajat():
    return render_template('adauga_angajat.html')

@app.route('/adauga/manager')
def front_adauga_manager():
    return render_template('adauga_manager.html')

@app.route('/signup')
def front_signup():
    return render_template('signup.html')

@app.route('/adminsignup',methods=['POST'])
def admin_signup():
    global admins
    inputs=request.form.to_dict()
    for admin in admins:
        if inputs['Companie']==admin['Companie']:
            return 'Numele companiei trebuie sa fie unic!'
    if inputs['Email'].endswith('@yahoo.com') or inputs['Email'].endswith('@gmail.com'):
        if inputs['Password']==inputs['Repeat_Password']:
            inputs['Password']=hash_password(inputs['Password'])
            inputs['Manageri']=[]
            del inputs['Repeat_Password']
            admins.append(inputs)
            admin_details(path,'write',admins)
            return 'Ati inregistrat noul cont cu succes!'
        else:
            return 'Trebuie sa introduceti aceeasi parola!'
    else:
        return 'Introduceti un email valid!'

@app.route('/home',methods=['POST'])
def home():
    global current_admin
    inputs=request.form
    for admin in admins:
        if inputs['Companie']==admin['Companie']:
            current_admin=admin
            return render_template('menu.html')
    return 'Compania nu este inregistrata in baza de date!'
    
@app.route('/adminlogin',methods=['POST'])
def login():
    global current_admin
    inputs=request.form
    if inputs['Email']==current_admin['Email']:
        if hash_password(inputs['Password'])==current_admin['Password']:
            return  render_template('options.html')
        else:
            return 'Parola incorecta!'
    else:
        return 'Email incorect!'

@app.route('/inregistrare/angajat',methods=['POST'])
def inregistrare_angajat():
    global current_admin
    inputs=request.form.to_dict()
    if inputs['Companie'] != current_admin['Companie']:
        return f'Introduceti compania administrata de dumneavoastra!'
    if int(inputs['IDManager']) not in current_admin['Manageri']:
        return f'Introduceti id-ul din lista de manageri a companiei dumneavoastra! Lista actuala: {current_admin['Manageri']}. Daca nu exista nici un manager adaugati-l manual.'
    angajati._inregistrez_utilizator(inputs)
    return 'Angajat inregistrat cu succes!'

@app.route('/inregistrare/manager',methods=['POST'])
def inregistrare_manager():
    global current_admin
    inputs=request.form.to_dict()
    if inputs['Companie'] != current_admin['Companie']:
        return f'Introduceti compania administrata de dumneavoastra!'
    angajati._inregistrez_utilizator(inputs)
    id=angajati.listaAngajati[-1]['ID']
    current_admin['Manageri'].append(id)
    for i in range(len(admins)):
        if admins[i]['Companie']==current_admin['Companie']:
            admins[i]['Manageri']=current_admin['Manageri']
    admin_details(path,'write',admins)
    return 'Manager inregistrat cu succes!'

@app.route('/inregistrare/poarta',methods=['POST'])
def inregistrare_poarta():
    inputs=request.form.to_dict()
    return poartatip2.inregistreaza_access_db(inputs['IDPersoana'],checkSens(inputs['IDPersoana']),inputs['IDPoarta'],checkID(inputs['IDPersoana']))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=4000,debug=True)
