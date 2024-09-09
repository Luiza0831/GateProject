import smtplib, ssl
class EmailSender():
    
    def __init__(self,sender_email):
        self.password=self.__readTXT('GmailPassw.txt')
        self.sender_email=sender_email

    def __readTXT(self,path):
        with open(path,'r') as file:
            content=file.read()
            return content

    def _send_email(self,message="",receiver_email=""):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(self.sender_email,self.password)
            server.sendmail(self.sender_email, receiver_email, message)