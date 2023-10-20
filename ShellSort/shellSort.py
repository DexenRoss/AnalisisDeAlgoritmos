import random

# Crear un arreglo vacío
arreglo = []

# Llenar el arreglo con 35 números enteros aleatorios entre 1 y 100
for i in range(35):
    numero_entero = random.randint(1, 100)  # Puedes ajustar el rango según tus necesidades
    arreglo.append(numero_entero)

def shell_sort(arr):
    n = len(arr)
    gap = n// 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
            print("En la iteracion",i,"el arreglo es",arr)
        gap //= 2

# Ejemplo de uso

print("Lista original:", arreglo)
shell_sort(arreglo)
print("Lista ordenada:", arreglo)