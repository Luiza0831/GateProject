from FlaskServer import app
from Details import Checker
import threading

if __name__=='__main__':
    t1=threading.Thread(target=Checker.startProgram)
    t1.start()
    app.run(host='0.0.0.0',port=4000,debug=True)