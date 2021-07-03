from passlib.context import CryptContext

# Round: Iteraciones para reducir la posibilidad de cracking.
contexto = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000
)

texto = "x?1_P-1M.4!eM"

texto_encriptado = contexto.hash(texto)
print(texto_encriptado)
print(contexto.verify(texto, texto_encriptado))

# https://passlib.readthedocs.io/en/stable/narr/context-tutorial.html
