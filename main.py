from FlaskServer import app
from Details import *
import threading

if __name__=='__main__':
    t1=threading.Thread(target=checker.startProgram)
    t2=threading.Thread(target=checkHours.start(current_admin))
    t1.start()
    t2.start()
    app.run(host='0.0.0.0',port=4000,debug=True)