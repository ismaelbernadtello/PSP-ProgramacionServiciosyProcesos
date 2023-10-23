# Ejercicio 12: Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular y cantidad (puede tener decimales). 
# El titular será obligatorio y la cantidad es opcional. 
# Crea sus métodos get, set y toString. 
#     Tendrá dos métodos especiales:
#                 - ingresar(double cantidad): se ingresa una cantidad a la cuenta si la cantidad introducida es negativa, no se hará nada.
#                 - retirar(double cantidad): se retira una cantidad a la cuenta, si restando la cantidad actual a la que nos pasan es negativa, 
#                                             la cantidad de la cuenta pasa a ser 0.

class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular  # Guardo el titular que se pasa como parámetro
        self.cantidad = cantidad  # Guardo la cantidad que se pasa como parámetro

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad  # Ingresa una cantidad a la cuenta si es positiva


    def retirar(self, cantidad):
        if cantidad > 0:
            if self.cantidad - cantidad < 0:
                self.cantidad = 0  # Si al restar la cantidad actual a la que nos pasan es negativa, la cantidad de la cuenta pasa a ser 0
            else:
                self.cantidad -= cantidad  # Si hay fondos en la cuenta se retira la cantidad deseada

    def __str__(self):
        return f"Titular: {self.titular}, Cantidad: {self.cantidad}" 

    
# Getters y setters
    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    def get_cantidad(self):
        return self.cantidad  

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad 


# Ejemplo de uso
cuenta1 = Cuenta("Juan Pérez", 1000)
print(cuenta1)  # Resultado-> Titular: Juan Pérez, Cantidad: 1000

cuenta1.ingresar(500)
print(cuenta1)  # Resultado-> Titular: Juan Pérez, Cantidad: 1500

cuenta1.retirar(2000)
print(cuenta1)  # Resultado-> Titular: Juan Pérez, Cantidad: 0