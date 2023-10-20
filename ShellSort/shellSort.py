import random

# Crear un arreglo vacío
arreglo = []
arr_hib=[]

# Llenar el arreglo con 35 números enteros aleatorios entre 1 y 100
for i in range(35):
    numero_entero = random.randint(1, 100)  # Se puede ajustar segun los gustos
    arreglo.append(numero_entero)
    arr_hib.append(numero_entero)

def shell_sort(arr):
    n = len(arr)
    gap = n// 2
    iter=0
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        iter+=1
        print("En la iteracion",iter,"el arreglo es",arr)
        gap //= 2


# Hibbrad
def hibbard_shell_sort(arr):
    n = len(arr)
    gap = 1
    iter=0
    while gap < n:
        gap = (gap * 2) + 1
    gap //= 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        iter+=1
        print("En la iteracion",iter,"el arreglo es",arr)
        gap = (gap - 1) // 2

# Ejemplo de uso
print("Shell sort")
print("Lista original:", arreglo)
shell_sort(arreglo)
print("Lista ordenada:", arreglo)
print("-----------------------------------------")
print("-----------------------------------------")
print("-----------------------------------------")
print("Hibbrad")
print("Lista orignal:", arr_hib)
hibbard_shell_sort(arr_hib)
print("Lista ordenada:", arr_hib)