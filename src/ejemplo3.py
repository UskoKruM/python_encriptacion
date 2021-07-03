from cryptography.fernet import Fernet

texto = "x?1_P-1M.4!eM"

# Genera una clave en formato de secuencia de bytes:
key = Fernet.generate_key()
objeto_cifrado = Fernet(key)
texto_encriptado = objeto_cifrado.encrypt(str.encode(texto))
print(texto_encriptado)

texto_desencriptado_bytes = objeto_cifrado.decrypt(texto_encriptado)
print(texto_desencriptado_bytes)
texto_desencriptado = texto_desencriptado_bytes.decode()
print(texto_desencriptado)
print(type(texto_desencriptado))

# https://cryptography.io/en/latest/fernet/