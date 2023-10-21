import random

# Crear un arreglo vacío

#Descomentar o comentar esta seccion de codigo si quiere Shell sort mas rapido
arreglo = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,20,23,22,24,25,26,27,28,29,30,31,32,33,34,35]
arr_hib = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,20,23,22,24,25,26,27,28,29,30,31,32,33,34,35]

#Descomentar o comentar esta seccion del codigo si quiere Hibbrad mas rapido
"""arreglo = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
arr_hib = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]"""



def shell_sort(arr):
    n = len(arr)
    gap = n // 2
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