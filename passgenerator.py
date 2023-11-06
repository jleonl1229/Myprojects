import random

minus = "abcdefghijklmnñopqrstuvwxyz"
mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!#$%&/()=;:_"

salida = minus+mayus+numeros+simbolos
longitud = 16

password = "".join(random.sample(salida,longitud))
print("Tu nueva y segura contraseña puede ser: "+password)

