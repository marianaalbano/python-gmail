import imaplib
import email
from Model import Mensagens, session

class BuscaEmail():
    def __init__(self):
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        self.mail.login(user, passwd)
        self.mail.list()
        # Out: list of "folders" aka labels in gmail.
        self.mail.select("inbox") # connect to inbox.


    def procura_mensagens(self, search):
        result, data = self.mail.search(None, search)
        
        ids = data[0] # data is a list.
        id_mensagens = ids.split() # ids is a space separated string
        return id_mensagens



    def grava_informacoes(self,id_mensagens):
        try:
            mensagem = Mensagens()
            for id in id_mensagens:
                result, data = self.mail.fetch(id, "(RFC822)")
                raw_email = data[0][1]

                email_message = email.message_from_string(raw_email)

                mensagem.data = email_message['Date']
                mensagem.origem = email.utils.parseaddr(email_message['From'])[1]
                mensagem.assunto = email_message['Subject']
                session.add(mensagem)
                session.commit()
        except Exception as e:
            print ("Erro: %s"%e)
            session.rollback()

if __name__ == '__main__':
    be = BuscaEmail()
    conteudo = be.procura_mensagens('(BODY "Devops")')
    be.grava_informacoes(conteudo)
    assunto = be.procura_mensagens('(HEADER Subject "Devops")')
    be.grava_informacoes(assunto)