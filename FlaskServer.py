from flask import Flask

class FlaskServer():

    def __init__(self):
        app=Flask(__name__)

        @app.route('/')
        def home():
            pass

        if __name__=='__main__':
            app.run(host='0.0.0.0',port=5000,debug=True)