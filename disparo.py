import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuração
host = 'smtp.nathyelle.com.br'
port = 587
user = 'pedrohenrique@nathyelle.com.br'
password = 'Papaalfa168191'

# Criando objeto
print('Criando objeto servidor...')
server = smtplib.SMTP(host, port)

# Login com servidor
print('Login...')
server.ehlo()
server.starttls()
server.login(user, password)

# Criando mensagem
message = 'Olá, mundo!'
print('Criando mensagem...')
email_msg = MIMEMultipart()
email_msg['From'] = user
email_msg['To'] = 'pedroaraujo0600@gmail.com'
email_msg['Subject'] = 'Teste de envio automático'
print('Adicionando texto...')
email_msg.attach(MIMEText(message, 'plain'))

# Enviando mensagem
print('Enviando mensagem...')
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
print('Mensagem enviada!')
server.quit()