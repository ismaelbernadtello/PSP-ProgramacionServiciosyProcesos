import smtplib  # Importa módulo para el envío de correos electrónicos

client = smtplib.SMTP(host='0.0.0.0', port=1025)  # Se conecta al servidor SMTP con los parámetros especificados
sender = 'alberto@salesianos.edu'  # Dirección del remitente
dest = 'apruebame@salesianos.edu'  # Dirección del destinatario
message = "hola soy alberto y soy bobo"  # Mensaje a enviar
message_template = 'From:%s\r\nTo:%s\r\n\r\n%s'  # Plantilla del mensaje
client.set_debuglevel(1)  # Establece el nivel de depuración en 1
# Envía el correo electrónico
client.sendmail(sender, dest, message_template % (sender, dest, message))
client.quit()  # Cierra la conexión SMTP
print("Enviar email end")