# Definición de la función MTF
def MTF(configuracion, secuencia):
    # Inicializamos el costo total en 0
    costo_total = 0
    
    # Iteramos sobre cada solicitud en la secuencia
    for solicitud in secuencia:
        # Calculamos el costo como la posición de la solicitud en la configuración más 1
        costo = configuracion.index(solicitud) + 1  # Costo es la posición del elemento más 1
        
        # Imprimimos información sobre la configuración, la solicitud y su costo
        print("Configuración:", configuracion)
        print("Solicitud:", solicitud)
        print("Costo:", costo)
        
        # Imprimimos la lista después del acceso
        print("Lista después de acceso:", end=" ")
        print(solicitud, end=" ")  # Imprimimos la solicitud
        configuracion.remove(solicitud)  # Eliminamos la solicitud de la configuración
        configuracion.insert(0, solicitud)  # Insertamos la solicitud al principio de la configuración
        print(configuracion)  # Imprimimos la configuración actualizada
        
        # Actualizamos el costo total sumándole el costo de la solicitud actual
        costo_total += costo
    
    # Imprimimos el costo total de accesos usando MTF
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
secuencia_c = [0] * 20
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
    # Inicializamos el costo total en 0
    costo_total = 0
    
    # Iteramos sobre los índices de la secuencia
    for i in range(len(secuencia)):
        # Obtenemos la solicitud en el índice actual
        solicitud = secuencia[i]
        
        # Calculamos el costo como la posición de la solicitud en la configuración más 1
        costo = configuracion.index(solicitud) + 1 
        
        # Incrementamos el costo total
        costo_total += costo

        # Imprimimos información sobre el paso actual
        print("Configuración:", configuracion)
        print(f"Paso {i+1}:")
        print(f"Solicitud: {solicitud}")
        print(f"Costo: {costo}")
        print(f"Costo total hasta ahora: {costo_total}")

        # Mover el elemento accedido al frente de la lista si está en los próximos elementos de la configuración
        if solicitud in configuracion[1+i+10+i:]:
            configuracion.remove(solicitud)
            configuracion.insert(0, solicitud)
    
    return costo_total


# Secuencia de solicitudes para el mejor caso
print("====================================================")
print("Secuencia de solicitudes para el mejor caso")
print("====================================================")
configuracion_c1 = [0, 1, 2, 3, 4]
secuencia_c1 = [0] * 20
costo_total = IMTF(configuracion_c1, secuencia_c1)
print("Costo total de accesos usando IMTF:", costo_total)
print("====================================================")

# Secuencia de solicitudes para el peor caso
print("====================================================")
print("Secuencia de solicitudes para el peor caso")
print("====================================================")
configuracion_d1 = [0, 1, 2, 3, 4]
secuencia_d1 = [4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0]
costo_total = IMTF(configuracion_d1, secuencia_d1)
print("Costo total de accesos usando IMTF:", costo_total)
print("====================================================")
print("")
