import smtplib
import ssl
import mimetypes
from email.message import EmailMessage

#1- Dados do E-mail
password = open("senha", "r").read()# função de leitura do arquivo com a senha de aplicação do e-mail remente
print(password)
from_email="emailremetente.com"
to_email="emaildestinatário.com"
subject = "Automação Planilha"
body = """
Olá,
Segue em anexo a automação da planilha para a empresa XYZ Automação.

Atenciosamente,
"""

# 2- Montando a estutura do e-mail
message = EmailMessage()
message["From"] = from_email
message["To"] = to_email
message["Subject"] = subject

message.set_content(body)
safe = ssl.create_default_context()#Critério de segurança exigido pelo Gmail

# 3-Adicionar Anexo
anexo = "relatorio.xlsx"
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split("/")# A função insere o nome e o tipo e o subtipo do arquivo do arquivo
with open(anexo, "rb") as a:
    message.add_attachment(
        a.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=anexo
    )

# 4- Envio do E-mail
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=safe) as smtp:# Deve colocar as informções do servidor do Email
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )