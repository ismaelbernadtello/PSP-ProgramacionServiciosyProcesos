#Enter an IP address and a port range where the program will then attempt to find open ports on the given computer by connecting to each of them. On any successful connections mark the port as open. 
import socket

# Función que escanea los puertos de una dirección IP
def scan_ports(ip_address, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error:
            pass
    return open_ports

# Inputs que se piden al usuario para realizar el escaneo de puertos
ip_address = input("Introduce la dirección IP que deseas escanear: ")
start_port = int(input("Introduce el puerto inicial desde el que se va a escanear: "))
end_port = int(input("Introduce el puerto final: "))

# Llamada a la función que escanea los puertos y se imprime el resultado
open_ports = scan_ports(ip_address, start_port, end_port)
print("Puertos abiertos:", open_ports)