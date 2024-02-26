#A file transfer program which can transfer files back and forth from a remote ftp sever. 
from ftplib import FTP

# Función que realiza la transferencia de archivos entre un cliente y un servidor FTP
def transferir_archivos(url, username, password, local_file, remote_file):
    # EStablecer conexión con el servidor FTP
    ftp = FTP(url)
    ftp.login(username, password)

    # Subida del archivo local al servidor y renombrado como remote_file en el servidor
    with open(local_file, "rb") as file:
        ftp.storbinary(f"STOR {remote_file}", file)

    # Descarga del archivo remote_file del servidor y guardado como downloaded_file en el cliente
    with open("downloaded_file.txt", "wb") as file:
        ftp.retrbinary(f"RETR {remote_file}", file.write)

    # Listado de archivos en el directorio actual del servidor
    ftp.retrlines('LIST')

    # Desconexión del servidor FTP
    ftp.quit()

# Ejemplo de uso con los datos de conexión y archivos de ejemplo. 
url = "127.0.0.1"
username = "admin"
password = "password"
local_file = "local_file.txt"
remote_file = "remote_file.txt"

# Llamada a la función para transferir los archivos con los parámetros de ejemplo
transferir_archivos(url, username, password, local_file, remote_file)