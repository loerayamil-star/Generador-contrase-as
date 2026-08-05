import re
import secrets
import string

# generador de contraseña segura ===================================================


def generar_contraseña(longitud=16, mayusculas=True, numeros=True, simbolos=True) -> str:
    if longitud <= 0:
        raise ValueError("longitud debe ser mayor a 0")

    alfabeto = string.ascii_lowercase

    if mayusculas:
        alfabeto += string.ascii_uppercase
    if numeros:
        alfabeto += string.digits
    if simbolos:
        alfabeto += string.punctuation

    caracteres = []

    for _ in range(longitud):
        caracteres.append(secrets.choice(alfabeto))

    return ''.join(caracteres)


# criterios a evaluar para la seguridad de la contraseña ===========================

def evaluar_contraseña(contraseña: str) -> dict:
    criterios = {
        'longitud': len(contraseña) >= 8,
        'mayusculas': bool(re.search(r'[A-Z]', contraseña)),
        'numeros': bool(re.search(r'\d', contraseña)),
        'simbolos': bool(re.search(f'[{re.escape(string.punctuation)}]', contraseña)),
        'minusculas': bool(re.search(r'[a-z]', contraseña))
    }

    razones = []
    puntuacion = 100

    if not criterios['longitud']:
        razones.append('La contraseña es muy corta')
        puntuacion -= 25
    if not criterios['mayusculas']:
        razones.append('La contraseña no contiene mayúsculas')
        puntuacion -= 25
    if not criterios['numeros']:
        razones.append('La contraseña no contiene números')
        puntuacion -= 25
    if not criterios['simbolos']:
        razones.append('La contraseña no contiene símbolos')
        puntuacion -= 25
    if not criterios['minusculas']:
        razones.append('La contraseña no contiene minúsculas')
        puntuacion -= 25

# Puntuacion o nivel de la contraseña ==================================================

    if puntuacion >= 80:
        nivel = "Muy fuerte"
    elif puntuacion >= 60:
        nivel = "Fuerte"
    elif puntuacion >= 40:
        nivel = "Media"
    else:
        nivel = "Débil"

    puntuacion = max(0, puntuacion)

    return {"puntuacion": puntuacion, "nivel": nivel, "razones": razones}
