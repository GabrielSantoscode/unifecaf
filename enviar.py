import email.message
import smtplib


def enviar_email():
    corpo_email = """
    <p> Olá Gabriel </p>
    <p> Segue meu email automatico </p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'gabriel.santosxj@gmail.com'
    msg['To'] = 'gabriel.santosxj@gmail.com'
    password = 'zwdkuagjpmavpinp'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

    enviar_email()
