# Definición de la función MTF
def MTF(configuracion, secuencia):
    costo_total = 0
    for solicitud in secuencia:
        costo = configuracion.index(solicitud) + 1  # Costo es la posición del elemento más 1
        print("Configuración:", configuracion)
        print("Solicitud:", solicitud)
        print("Costo:", costo)
        print("Lista después de acceso:", end=" ")
        print(solicitud, end=" ")
        
        # Mover el elemento accedido al frente de la lista
        configuracion.remove(solicitud)
        configuracion.insert(0, solicitud)
        
        print(configuracion)
        
        costo_total += costo
    
    print("Costo total de accesos usando MTF:", costo_total)
    print()

print("****************************************************")
print("Proyecto 3 - Análisis y Diseño de Algoritmos")
print("Es un gusto saludarte, a continuación se presentan los resultados de la ejecución del proyecto 3")
print("Paulo es el mejor profesor de la vida")
print("****************************************************")
print()
# a) Secuencia de solicitudes a)
print("====================================================")
print("a) Secuencia de solicitudes a)")
print("====================================================")
configuracion_a = [0, 1, 2, 3, 4]
secuencia_a = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
MTF(configuracion_a, secuencia_a)
print("====================================================")
print("")
print("====================================================")
print("b) Secuencia de solicitudes b)")
print("====================================================")
# b) Secuencia de solicitudes b)
configuracion_b = [0, 1, 2, 3, 4]
secuencia_b = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
MTF(configuracion_b, secuencia_b)

print("====================================================")
print("c) Secuencia de solicitudes c)")
print("====================================================")
# c) Secuencia de 20 solicitudes para mínimo costo total
configuracion_c = [0, 1, 2, 3, 4]
secuencia_c = [0, 1, 2, 3, 4] * 4
MTF(configuracion_c, secuencia_c)
print("====================================================")
print("")

print("====================================================")
print("d) Secuencia de solicitudes d)")
print("====================================================")
# d) Secuencia de 20 solicitudes para peor caso
configuracion_d = [0, 1, 2, 3, 4]
secuencia_d = [4, 3, 2, 1, 0] * 4
MTF(configuracion_d, secuencia_d)
print("====================================================")
print("")

print("====================================================")
print("e) Secuencia de solicitudes e)")
print("====================================================")
# e) Secuencia de solicitudes e)
configuracion_e = [0, 1, 2, 3, 4]
secuencia_e = [2] * 20
MTF(configuracion_e, secuencia_e)

print("====================================================")
print("calculando el costo total de acceso si la secuencia fuera 3, 3, 3, ...")
print("====================================================")
# Calculo del costo total de acceso si la secuencia fuera 3, 3, 3, ...
secuencia_e_repetida = [3] * 20
MTF(configuracion_e, secuencia_e_repetida)
print("====================================================")
print("")

print("====================================================")
print("f) Implementación del algoritmo IMTF (Improved Move to Front)")
print("====================================================")
# f) Implementación del algoritmo IMTF (Improved Move to Front)
def IMTF(configuracion, secuencia):
    costo_total = 0
    for i, solicitud in enumerate(secuencia):
        costo = configuracion.index(solicitud) + 1  # Costo es la posición del elemento más 1
        print("Configuración:", configuracion)
        print("Solicitud:", solicitud)
        print("Costo:", costo)
        print("Lista después de acceso:", end=" ")
        print(solicitud, end=" ")
        
        # Mover el elemento accedido al frente de la lista si está en los próximos i - 1 elementos
        if solicitud in secuencia[i+1:i+1+i]:
            configuracion.remove(solicitud)
            configuracion.insert(0, solicitud)
        
        print(configuracion)
        
        costo_total += costo
    
    print("Costo total de accesos usando IMTF:", costo_total)
    print()

# Ejemplo de uso de IMTF con la misma secuencia que la parte a)
IMTF(configuracion_a, secuencia_a)
print("====================================================")
print("")
