import smtplib, ssl

def send_email(message):

    host = "smtp.gmail.com" # Configura las variables host y port con la información del servidor SMTP de Gmail y el puerto SSL correspondiente (siempre así)
    port = 465

    username = "smanzano250800@gmail.com" #  Establece tu nombre de usuario y contraseña de Gmail para esta aplicación
    password = "razl xzkv ggfz dqbw"

    receiver = "smanzano250800@gmail.com" # Define la dirección de correo electrónico del destinatario.
    context = ssl.create_default_context() # Crea un contexto SSL seguro. Esto es necesario para establecer una conexión segura con el servidor SMTP de Gmail.

    with smtplib.SMTP_SSL(host, port, context = context) as server: # Abre una conexión al servidor SMTP de Gmail utilizando el protocolo SSL y crea un objeto server que puedes utilizar para enviar correos electrónicos. El bloque with garantiza que la conexión se cierre adecuadamente después de su uso
        server.login(username, password) # Inicia sesión en tu cuenta de Gmail utilizando el nombre de usuario y la contraseña proporcionados.
        server.sendmail(username, receiver, message) # Envía el correo electrónico utilizando el método sendmail. El remitente (quien envía el correo) es tu dirección de correo electrónico, el destinatario es la dirección del destinatario y el cuerpo del correo electrónico es el mensaje proporcionado como argumento a la función.
                                                     # username y receiver tienen que ser el mismo correo ya que lo manda mi correo a mi propio correo, para saber quién me ha escrito el correo