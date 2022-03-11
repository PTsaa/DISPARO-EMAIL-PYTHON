
# Essas serão as bibliotecas usadas neste exemplo
import smtplib # módulo
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Aqui serão configurados todos os dados
print('Para login pelo Gmail, se sua conta possuir verificação em duas etapas, gere uma senha de APP e use no lugar da sua senha. <https://support.google.com/accounts/answer/185833?hl=pt-BR>')
print('Este método NÃO usa autenticação SSL, somente TLS ou nenhuma.')
print('O Gmail usa o método TLS.')
print('O host do Gmail é smtp.gmail.com')
print('A porta padrão é para TLS é 587')
print('A porta padrão é para sem autenticação é 25')
host = str(input('Digite o host: '))
porta = int(input('Digite a porta: '))
usuario = str(input('Digite o seu e-mail: '))
senha = str(input('Digite a senha do seu e-mail: '))
assunto = str(input('Digite o assunto da mensagem: '))
msg = str(input('Digite a mensagem do e-mail: '))
destinatario = str(input('Digite o e-mail do destinatário: '))

# Aqui se cria o objeto servidor
server = smtplib.SMTP(host, porta)

# Aqui se inicia o procedimento de login
print('Realizando login...')
server.ehlo() # Para método sem autenticação
server.starttls() # Para método de autenticação TLS
server.login(usuario, senha)
print('Login realizado!')

# Aqui se configura a mensagem
email_msg = MIMEMultipart()
email_msg['From'] = usuario
email_msg['To'] = destinatario
email_msg['Subject'] = assunto
email_msg.attach(MIMEText(msg, 'plain'))

# Ação de envio
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
print('E-mail enviado com sucesso!')
server.quit() # Fechando o servidor