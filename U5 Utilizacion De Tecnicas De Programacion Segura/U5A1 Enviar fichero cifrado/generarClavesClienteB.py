from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# Generar las claves pública y privada para el cliente B
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()

# Guardar la clave privada en un archivo
with open("private_key.pem", "wb") as private_key_file:
    private_key_file.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
    )

# Guardar la clave pública en un archivo
with open("public_key.pem", "wb") as public_key_file:
    public_key_file.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
    )

# Crear un archivo de texto
with open("archivo.txt", "w") as file:
    file.write("Contenido del archivo")

# Leer el contenido del archivo
with open("archivo.txt", "rb") as file:
    message = file.read()

# Cifrar el archivo usando la clave pública de B
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Guardar el archivo cifrado
with open("archivo_cifrado.txt", "wb") as file:
    file.write(ciphertext)