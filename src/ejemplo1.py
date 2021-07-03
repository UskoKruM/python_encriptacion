from werkzeug.security import generate_password_hash, check_password_hash

texto = "x?1_P-1M.4!eM"
texto_encriptado1 = generate_password_hash(texto)
texto_encriptado2 = generate_password_hash(texto, 'sha256')
texto_encriptado3 = generate_password_hash(texto, 'sha256', 30)
texto_encriptado4 = generate_password_hash(texto, 'pbkdf2:sha256')
texto_encriptado5 = generate_password_hash(texto, 'pbkdf2:sha256', 30)
texto_encriptado6 = generate_password_hash(texto, 'pbkdf2:sha256:30', 30)
print(texto_encriptado1)
print(texto_encriptado2)
print(texto_encriptado3)
print(texto_encriptado4)
print(texto_encriptado5)
print(texto_encriptado6)

# https://werkzeug.palletsprojects.com/en/2.0.x/utils/

print(check_password_hash(texto_encriptado1, texto))
print(check_password_hash(texto_encriptado2, texto))
print(check_password_hash(texto_encriptado3, texto))
print(check_password_hash(texto_encriptado4, texto))
print(check_password_hash(texto_encriptado5, texto))
print(check_password_hash(texto_encriptado6, texto))
