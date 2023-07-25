import time as t

def redondear(numero):
    aux=numero-int(numero)
    if aux>0.5:
        return int(numero)+1
    else:
        return int(numero)

def suma_de_decimales():
    inicio=t.time()
    numero1=float(input("Ingrese el primer numero:\n"))
    numero2=float(input("Ingrese el segundo numero:\n"))
    suma=numero1+numero2
    sumaRedondeada=redondear(suma)
    tiempoDeEjecucion=t.time()-inicio
    print(f"Tiempo de Ejecución : {tiempoDeEjecucion}")
    return sumaRedondeada

if(__name__=="__main__"):
    print("Chau!!!!!!!!!!!!!!")