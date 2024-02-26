# SI TENEMOS QUE HACER QUE SE INSTALEN LOS MÓDULOS AL EJECUTAR EL ARCHIVO TENEMOS QUE PONER LO SIGUIENTE:
# !pip3 install scp/paramiko/pycrypto/pycryptodome/ftplib/smtplib

# Importación de módulos necesarios
# Importa el cliente SCP para transferencia segura de archivos
from scp import SCPClient
# Importa clases para crear un servidor HTTP
from http.server import BaseHTTPRequestHandler, HTTPServer
import paramiko  # Importa el módulo para realizar conexiones SSH
# Importa la clase RSA para gestionar claves públicas/privadas RSA
from Crypto.PublicKey import RSA
# Importa módulos para encriptación AES y RSA
from Crypto.Cipher import AES, PKCS1_OAEP
import smtplib  # Importa módulo para el envío de correos electrónicos
from ftplib import FTP  # Importa módulo para transferencia de archivos FTP

# Definición de un manejador de peticiones HTTP personalizado


class HelloHandler(BaseHTTPRequestHandler):
    # Método para manejar peticiones HEAD
    def do_HEAD(self):
        self.send_response(200)  # Responde con un código 200 (OK)
        # Especifica el tipo de contenido como HTML
        self.send_header('Content-type', 'text/html')
        self.end_headers()  # Finaliza las cabeceras de la respuesta

    # Método para manejar peticiones GET
    def do_GET(self):
        self.do_HEAD()  # Ejecuta la función para enviar cabeceras
        # Envía una respuesta HTML al cliente
        self.wfile.write("""<html><head><title>Hello
            Gorka</title><meta charset="UTF-8"></head><body><p>¿Funcionará?</p>
            <form method="POST" >
            <input type="submit" value="Click me">
                <img style="width:200px" src="https://media.tenor.com/R4Ky10OWvpQAAAAM/vegeta-raining.gif">
                        </input>
            </form>
            </body></html>""".encode("utf-8"))  # Codifica la respuesta como UTF-8 y la envía

    # Método para manejar peticiones POST
    def do_POST(self):
        self.do_HEAD()  # Ejecuta la función para enviar cabeceras
        # Respuesta HTML para peticiones POST
        self.wfile.write("""<html><head><title>Hello
            World</title><meta charset="UTF-8"></head><body> <p> Yo lo soñé </p>
            <img style="width:200px" src="https://i.pinimg.com/736x/ee/12/a9/ee12a906d097550141060360ccc54fd2.jpg">
            </body></html>""".encode("utf-8"))  # Codifica la respuesta como UTF-8 y la envía
        self.get_Documents()  # Llama al método para obtener documentos

    # ? A partir de aquí, jugamos.
    # Método para obtener documentos
    def get_Documents(self):
        # self.subirArchivoSSH()
        self.recuperarArchivoSSH()  # ? Primero.
        #! Descargar archivos a través de SSH

        self.desEncrypt()  # ? Segundo.
        #!Desencripta datos

        # self.writeEncryptedDataTofile()  # Escribe datos encriptados en un archivo

        self.subirArchivoFTP()  # Sube archivos a través de FTP
        # self.recuperarArchivoFTP()  # Descargar archivos a través de FTP

        self.sendEmail()  # Envía un correo electrónico

        return  # Lo uso para parar la ejecución del método e ir controlando paso a paso el código y lo que se va ejecutando

    # Método para subir archivos a un servidor SSH
    def subirArchivoSSH(self):
        print("Subiendo archivos al SSH")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Se conecta al servidor SSH con los parámetros especificados
        ssh.connect(hostname='127.0.0.1', port=2222,
                    username='linuxserver', password='password')

        # Crea un cliente SCP para la transferencia segura de archivos
        # Un cliente SCP es un cliente que permite la transferencia segura de archivos entre un host local y un host remoto
        scp = SCPClient(ssh.get_transport())

        print("Subiendo archivo suelto al SSH")
        # Sube el archivo al servidor SSH y lo renombra como prueba.txt en la carpeta /config/test (.put es como el método .get)
        scp.put('examen.txt', remote_path='/config/test/prueba.txt')

        print("Subiendo archivos con carpeta al SSH")

        #! Si no sabes que carpetas hay en el servidor, usa recursive.

        """
        # Crea un directorio en el servidor SSH
        ssh.exec_command('mkdir -p /config/examen')
        """

        # Si necesitamos subir una carpeta con su contenido, usamos el parámetro recursive=True
        scp.put('carpeta', recursive=True, remote_path='/config/test')
        """
        carpeta es el nombre de la carpeta local y /config/test es el nombre de la carpeta remota que se crea
        
        Por defecto sino indicamos carpeta se guarda en el directorio raíz del servidor SSH que es config
        Si las carpetas no existen, se crean automáticamente al usar el parámetro recursive=True 
        """

        scp.close()  # Cierra la conexión SCP
        ssh.close()  # Cierra la conexión SSH
        print("SSH end")

    # Método para recuperar archivos de un servidor SSH mediante SCP

    def recuperarArchivoSSH(self):
        # Para conectarnos por ssh tenemos que poner esto en la terminal: ssh -p 2222 linuxserver@localhost
        # Para subir un archivo por ssh tenemos que poner esto en la terminal: scp -P 2222 /home/albertosaz.bin linuxserver@localhost:/home
        print("connect SSH")

        ssh = paramiko.SSHClient()  # Crea un cliente SSH
        # Configura la política de claves faltantes
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Se conecta al servidor SSH con los parámetros especificados
        ssh.connect(hostname='127.0.0.1', port=2222,
                    username='linuxserver', password='password')

        # Crea un cliente SCP para la transferencia segura de archivos
        # Un cliente SCP es un cliente que permite la transferencia segura de archivos entre un host local y un host remoto
        scp = SCPClient(ssh.get_transport())

        # Descarga el archivo encriptado desde el servidor SSH y lo guarda en el directorio local con el nombre encriptado.bin
        scp.get('/config/encrypted_data.bin', local_path='encrypted_data.bin')
        # Descarga el archivo de clave privada desde el servidor SSH
        scp.get('/config/private.pem')

        scp.close()  # Cierra la conexión SCP
        ssh.close()  # Cierra la conexión SSH
        print("SSH end")

    # Método para desencriptar datos usando la clave privada RSA

    def desEncrypt(self):
        print("Desencriptar")

        # Abre el archivo de datos encriptados en modo lectura binaria. ESTE ARCHIVO LO HEMOS DESCARGADO DEL SERVIDOR SSH O FTP
        file_in = open("encrypted_data.bin", "rb")
        # Importa la clave privada RSA. ESTE ARCHIVO LO HEMOS DESCARGADO DEL SERVIDOR SSH O FTP
        private_key = RSA.import_key(open("private.pem").read())

        # Sacamos la información encriptada y la guardamos en la variable enc_session_key (se guarda aun encriptado, pero se lee su contenido)
        enc_session_key = file_in.read(private_key.size_in_bytes())

        # Cerramos el archivo con los datos encriptados
        file_in.close()

        # Guardamos la clave privada en la variable cipher_rsa (n se sabe porque, pero se usa para desencriptar)
        cipher_rsa = PKCS1_OAEP.new(private_key)

        # Desencripta el archivo obteniendo el contenido y lo guardamos en la variable session_key
        self.session_key = cipher_rsa.decrypt(enc_session_key)

        # transformamos la variable session_key a string
        self.session_key = self.session_key.decode("utf-8")

        # Imprime el contenido del archivo desencriptado
        print("Desencriptar finalizado. ESTE ES EL CONTENIDO DEL ARCHIVO : /n" + self.session_key)

    # Método para escribir datos encriptados en un archivo
    def writeEncryptedDataTofile(self):
        # Escribe la clave de sesión en un archivo
        # Abre un archivo para escritura binaria wb=(write binary)
        file_out = open("desencriptado.txt", "wb")
        # Escribe la clave de sesión en el archivo
        file_out.write(self.session_key)
        file_out.close()  # Cierra el archivo

    # Método para cargar archivos a través de FTP
    def subirArchivoFTP(self):
        # Para subir un archivo al ftp podemos usar la app FileZilla, que es un cliente FTP, y nos conectamos con los datos que nos da el servidor
        print("Subir archivos al FTP")

        # Dirección del servidor FTP
        url = '127.0.0.1'
        port = 21  # Puerto del servidor FTP

        # Se conecta al servidor FTP con los parámetros especificados y al finalizar la conexión se cierra automáticamente
        with FTP() as conn:
            # Se conecta al servidor FTP con los parámetros especificados
            conn.connect(url, port)
            # Información del login del servidor FTP
            conn.login('admin', 'preguntaraalberto')
            # Cambia al directorio raíz del servidor FTP o al que le indiquemos
            conn.cwd('/')
            # Imprime el directorio actual
            print(conn.pwd())
            # Obtiene el mensaje de bienvenida del servidor FTP
            print(conn.getwelcome())

            # Crea una carpeta en el servidor FTP si no existe
            if not conn.nlst('/pruebaCarpeta1'):
                conn.mkd('/pruebaCarpeta1')

            # Abre el archivo binario en modo lectura rb=(read binary) y lo sube al servidor FTP
            with open('encrypted_data.bin', 'rb') as file:
                conn.storbinary('STOR /pruebaCarpeta1/encrypted.bin', file)
                # Sube el archivo al servidor FTP con el nombre albertosaz.bin STOR=(store) hace que se guarde el archivo en el servidor FTP

            # Obtiene y muestra el listado de archivos en el servidor FTP con el método listCallback
            # Se envia al servidor FTP el comando LIST para obtener el listado de archivos en el servidor FTP
            conn.retrlines('LIST')

        print("Upload FTP end")

    def recuperarArchivoFTP(self):
        print("Recuperar archivos del FTP")

        # Dirección del servidor FTP
        url = '127.0.0.1'
        port = 21  # Puerto del servidor FTP

        # Se conecta al servidor FTP con los parámetros especificados y al finalizar la conexión se cierra automáticamente
        with FTP() as conn:
            # Se conecta al servidor FTP con los parámetros especificados
            conn.connect(url, port)
            # Información del login del servidor FTP
            conn.login('admin', 'preguntaraalberto')
            # Cambia al directorio raíz del servidor FTP o al que le indiquemos
            conn.cwd('/')
            # Imprime el directorio actual
            print(conn.pwd())
            # Obtiene el mensaje de bienvenida del servidor FTP
            print(conn.getwelcome())

            # Crea un archivo binario en modo escritura wb=(write binary) y lo descarga del servidor FTP con el nombre downloaded_file.txt
            with open("encryptedDescargado.bin", "wb") as file:
                # Descarga el archivo del servidor FTP con el nombre remote_file.txt
                conn.retrbinary("RETR encrypted.bin", file.write)
            """ si fuera guardar en una variable el contenido del archivo, se haría así:
            variable = ""
            conn.retrbinary("RETR encrypted.bin", variable)
            """

            # Obtiene y muestra el listado de archivos en el servidor FTP con el método listCallback
            # Se envia al servidor FTP el comando LIST para obtener el listado de archivos en el servidor FTP
            conn.retrlines('LIST')

    # Método para enviar correos electrónicos

    def sendEmail(self):
        print("Enviar email")
        # Se conecta al servidor SMTP con los parámetros especificados
        client = smtplib.SMTP(host='0.0.0.0', port=1025)
        sender = 'alberto@salesioanos.edu'  # Dirección del remitente
        dest = 'apruebame@salesianos.edu'  # Dirección del destinatario
        subject = 'Asunto del correo'  # Asunto del correo
        # Mensaje a enviar con el contenido del archivo desencriptado
        message = self.session_key
        message_template = 'From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s'  # Plantilla del mensaje

        # Establece el nivel de depuración en 1. Esto sirve para ver los mensajes que se envían y reciben en la consola
        client.set_debuglevel(1)

        # Envía el correo electrónico
        client.sendmail(sender, dest, message_template %
                        (sender, dest, subject, message))
        client.quit()  # Cierra la conexión SMTP
        print("Enviar email end")


# Definición de parámetros para el servidor HTTP
params = '', 8083
# Creación del servidor HTTP con el manejador definido
server = HTTPServer(params, HelloHandler)

# Intento de mantener el servidor en funcionamiento indefinidamente
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass

# Cierre del servidor
server.server_close()
