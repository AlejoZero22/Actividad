def bubble_sort(notas):
    n = len(notas)
    for i in range(n - 1):  
        clave = False
        for j in range(n - 1 - i):  
            if notas[j] > notas[j + 1]:
                notas[j], notas[j + 1] = notas[j + 1], notas[j]
                clave = True
        if not clave:
            break  
    return notas

# Ejemplo de uso
calificaciones = [50, 20, 44, 5, 100, 1, 95]
ordenadas = bubble_sort(calificaciones)
print("Calificaciones ordenadas:", ordenadas)
