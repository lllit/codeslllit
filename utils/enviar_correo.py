import os
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import base64
from dotenv import load_dotenv
import os


# Cargar variables de entorno desde el archivo .env
load_dotenv()

def enviar_correo(correo_destinatario, code):
    remitente = os.getenv('EMAIL_USER')
    codigo = os.getenv('EMAIL_PASSWORD')

    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = correo_destinatario
    msg['Subject'] = 'Código de Bandcamp'

    with open("temp_correo/correo.html", encoding='utf-8') as file:
        html = file.read()

    html = html.replace("{code}", code)

    msg.attach(MIMEText(html, 'html', 'utf-8'))
    
    try:
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(remitente, codigo)

        smtp.sendmail(remitente, correo_destinatario, msg.as_string())
        smtp.quit()
        print("Correo enviado exitosamente")

    except Exception as e:
        print(f"Error al enviar el correo: {e}")