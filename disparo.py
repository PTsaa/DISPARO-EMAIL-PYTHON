import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuração
host = 'smtp.nathyelle.com.br'
port = 587
with open("email.txt", "r") as arquivo:
    user = str(arquivo.read())

with open("senha.txt", "r") as arquivo:
    password = arquivo.read()

with open('msg.txt', 'r') as arquivo:
    assunto = arquivo.readline(1)

with open('msg.txt', 'r') as arquivo:
    msg = arquivo.read()

with open('destinatario.txt', 'r') as arquivo:
    destinatario = arquivo.read()


# Criando objeto
print('Criando objeto servidor...')
server = smtplib.SMTP(host, port)

# Login com servidor
print('Login...')
server.ehlo()
server.starttls()
server.login(user, password)

# Criando mensagem
message = msg
print('Criando mensagem...')
email_msg = MIMEMultipart()
email_msg['From'] = user
email_msg['To'] = destinatario
email_msg['Subject'] = assunto
print('Adicionando texto...')
email_msg.attach(MIMEText(message, 'plain'))

# Enviando mensagem
print('Enviando mensagem...')
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
print('Mensagem enviada!')
server.quit()