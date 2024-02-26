#An application that attempts to connect to a website or server every so many minutes or a given time and check if it is up. 
#If it is down, it will notify you by posting a notice on screen. 
import requests
import time
from datetime import datetime

def check_website(url):
    try:
        response = requests.get(url) # Se intenta conectar al sitio web
        # Se comprueba si el código de estado devuelto es 2xx (indicando éxito)
        if response.status_code // 100 == 2:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False

def notify():
    print(f"[{datetime.now()}] El sitio web está caído!")

def main():
    # Se pide al usuario que introduzca la URL del sitio web a monitorear y el intervalo de comprobación
    website_url = input("Ingrese la URL del sitio web a monitorear, ejemplo(https://www.google.com/) : ") 
    check_interval_minutes = int(input("Ingrese el intervalo de comprobación en minutos: "))

    # Bucle infinito que comprueba el estado del sitio web y notifica al usuario si está caído
    while True:
        if not check_website(website_url): # Si el sitio web está caído, notifica al usuario usando la función notify()
            notify()
        else:
            # Si el sitio web está en línea, imprime un mensaje en la consola
            print(f"[{datetime.now()}] El sitio web está en línea!") 
            
        time.sleep(check_interval_minutes * 60)  # Se para el bucle durante el intervalo de tiempo especificado

if __name__ == "__main__":
    main()