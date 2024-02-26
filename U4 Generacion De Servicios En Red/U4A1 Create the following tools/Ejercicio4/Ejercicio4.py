#Enter an IP or host address and have it look it up through whois and return the results to you.  
import whois

# Función que realiza una búsqueda WHOIS
def whois_lookup(target):
    try:
        # Perform WHOIS lookup
        result = whois.whois(target)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

# Función principal que pide al usuario que introduzca una dirección IP o un nombre de host 
# y llama a la función que realiza la búsqueda WHOIS
def main():
    target = input("Ingrese una dirección IP o un nombre de host: ")
    result = whois_lookup(target)

    if isinstance(result, dict):
        print("\nWHOIS Lookup Results:")
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print(result)

# Si el script se ejecuta directamente, se llama a la función principal
if __name__ == "__main__":
    main()
