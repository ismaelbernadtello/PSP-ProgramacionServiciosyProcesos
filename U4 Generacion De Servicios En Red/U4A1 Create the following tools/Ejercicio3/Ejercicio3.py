# Enter an IP address and find the country that IP is registered in.   
import requests
import ipaddress

# Función que obtiene el país de una dirección IP
def obtener_pais_por_ip(ip):
    try:
        ipaddress.ip_address(ip)  # Valida la dirección IP ingresada
    except ValueError:
        return "La dirección IP ingresada no es válida."

    url = f"http://ipinfo.io/{ip}/json"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza una excepción si la respuesta no es exitosa
        datos = respuesta.json()  # Se obtiene la información en formato JSON
        pais = datos.get('country', 'No se pudo determinar el país')  # Se obtiene el país de la información
        return pais
    except requests.exceptions.RequestException as e:
        return f"No se pudo obtener la información: {str(e)}"


# Si el script se ejecuta directamente, se pide al usuario que introduzca una dirección IP
if __name__ == "__main__":
    # Se pide al usuario que introduzca una dirección IP
    ip_usuario = input("Ingrese una dirección IP: ")
    # Se llama a la función que obtiene el país de la IP
    pais = obtener_pais_por_ip(ip_usuario)
    # Se imprime el resultado
    print(f"La dirección IP {ip_usuario} está registrada en el país: {pais}")
