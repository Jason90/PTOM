from business import Base

class Mail(Base):

   def __init__(self):
      super(Mail,self).__init__("mail.json")
      
   def send(self):
      print("send mail from "+self.data.mail.fo.name +" to "+self.data.mail.to[0].name)
      return True
   