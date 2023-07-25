# 1. Escriba una función redondear() que permita redondear un número
# decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
# entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
# anterior (3).

# def redondear(numero):
#     aux=numero-int(numero)
#     if aux>0.5:
#         return int(numero)+1
#     else:
#         return int(numero)

# print(redondear(3.3))

# 2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un
# módulo que esté fuera de ese paquete, cree una función de suma de
# decimales que redondee el resultado haciendo uso de la función
# redondear() del paquete recién creado.

# import Funciones as f

# print(f.suma_de_decimales())

# 3. Usando el módulo datetime, escribe un programa que muestre la fecha
# y hora actuales del sistema.

# import datetime as fh

# def fecha_actual():
#     fecha_hora_actual=fh.datetime.now()
#     print(f"Fecha por defecto {fecha_hora_actual}")
#     fecha_formateada=fecha_hora_actual.strftime("%d/%m/%Y %H:%M:%S")
#     print(f"Fecha Formateada {fecha_formateada}")

# fecha_actual()

# 4. Escriba un programa que devuelva un número par al azar entre 2 y 10
# (pista: para comprobar si se pueden generar todos los números, pruebe
# ejecutar el programa dentro de un ciclo infinito).

# import random as r

# def numero_azar():
#     numero1=r.randint(2,10)
#     numero2=r.randint(2,10)
#     print(f"Par de numeros {numero1} {numero2}")

# numero_azar()

# 5. Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
# para la adivinación o para buscar consejo. Su mecanismo es muy simple:
# ante una pregunta del usuario, la bola responde con una de 8 posibles
# respuestas:
# - Es seguro que sí
# - Las chances son buenas
# - Puedes contar con ello
# - Pregúntame de nuevo más tarde
# - Concéntrate y pregunta de nuevo
# - No veo con claridad, intenta de nuevo
# - Mi respuesta es no
# - Mis fuentes me dicen que no
# Escriba una función en Python para simular la bola mágica.

# import random as r

# def bola_magica():
#     respuestas=["Es seguro que sí","Las chances son buenas","Puedes contar con ello","Pregúntame de nuevo más tarde","Concéntrate y pregunta de nuevo","No veo con claridad, intenta de nuevo","Mi respuesta es no","Mis fuentes me dicen que no"]
#     respuesta=r.choice(respuestas)
#     print(f"RESPUESTA: {respuesta}")

# bola_magica()

# 6. Encuentre el tiempo de ejecución de los programas de los ejercicios
# anteriores (pista: use el módulo time)

#EJERCICIO 2
# import Funciones as f

# print(f.suma_de_decimales())

#EJERCICIO 3
# import datetime as fh
# import time as t

# def fecha_actual():
#     inicio=t.time()
#     fecha_hora_actual=fh.datetime.now()
#     print(f"Fecha por defecto {fecha_hora_actual}")
#     fecha_formateada=fecha_hora_actual.strftime("%d/%m/%Y %H:%M:%S")
#     print(f"Fecha Formateada {fecha_formateada}")
#     tiempoDeEjecucion=t.time()-inicio
#     print(f"Tiempo de Ejecución : {tiempoDeEjecucion}")

# fecha_actual()

#EJERCICIO 4
# import random as r
# import time as t

# def numero_azar():
#     inicio=t.time()
#     numero1=r.randint(2,10)
#     numero2=r.randint(2,10)
#     print(f"Par de numeros {numero1} {numero2}")
#     tiempoDeEjecucion=t.time()-inicio
#     print(f"Tiempo de Ejecución : {tiempoDeEjecucion}")

# numero_azar()

#EJERCICIO 5
# import random as r
# import time as t

# def bola_magica():
#     inicio=t.time()
#     respuestas=["Es seguro que sí","Las chances son buenas","Puedes contar con ello","Pregúntame de nuevo más tarde","Concéntrate y pregunta de nuevo","No veo con claridad, intenta de nuevo","Mi respuesta es no","Mis fuentes me dicen que no"]
#     respuesta=r.choice(respuestas)
#     print(f"RESPUESTA: {respuesta}")
#     tiempoDeEjecucion=t.time()-inicio
#     print(f"Tiempo de Ejecución : {tiempoDeEjecucion}")

# bola_magica()

# 7. (Opcional) Sorteo: Escriba un programa que simule un sorteo donde
# toman uno o más papeles al azar de un pozo para elegir los ganadores.

# import random as r

# def sorteo():
#     cantidad=1
#     print("Numeros Ganadores")
#     while cantidad<=10:
#         numero=r.randint(1,9999)
#         numeroGanador=str(numero).zfill(4)
#         print(f"{cantidad}. {numeroGanador}")
#         cantidad+=1

# sorteo()

# 8. (Opcional) Escriba una función que pida al usuario ingresar su fecha de
# nacimiento y sea capaz de devolver la cantidad de días desde su
# nacimiento hasta hoy.

# import datetime as d

# def dias_desde_nacimiento():
#     fecha_nacimiento=input("Ingrese su fecha de nacimiento (formato: DD/MM/AAAA): \n")
#     fecha_nacimiento = d.datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
#     fecha_de_hoy = d.datetime.now()

#     dias=fecha_de_hoy-fecha_nacimiento
#     print(f"Tienes {dias.days} dias de edad")

# dias_desde_nacimiento()


# 9. (Opcional) Implemente el programa del ejercicio 6 usando un diccionario.

import random as r
import time as t

def bola_magica():
    inicio=t.time()
    respuestas={1:"Es seguro que sí",2:"Las chances son buenas",3:"Puedes contar con ello",4:"Pregúntame de nuevo más tarde",5:"Concéntrate y pregunta de nuevo",6:"No veo con claridad, intenta de nuevo",7:"Mi respuesta es no",8:"Mis fuentes me dicen que no"}
    llave=r.randint(1,8)
    print(f"RESPUESTA: {respuestas[llave]}")
    tiempoDeEjecucion=t.time()-inicio
    print(f"Tiempo de Ejecución : {tiempoDeEjecucion}")

bola_magica()