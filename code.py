# Проверка массива на сортировку
def check_array(arr):
    # ИСПРАВЛЕНИЕ 1: проверка на пустой массив
    if not arr: 
        return True

    # ИСПРАВЛЕНИЕ 2: цикл до len(arr) - 1, чтобы не выходить за границы
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

# Поиск нужного массива среди пяти
def find_array(arr1, arr2, arr3, arr4, arr5):
    arrays = [arr1, arr2, arr3, arr4, arr5]
    for i in range(len(arrays)):
        if check_array(arrays[i]) == True:
            return i + 1
    return -1

# Тестовые данные для проверки
arr1 = ['a', 'b', 'c']  # Отсортирован
arr2 = ['c', 'b', 'a']  # Не отсортирован
arr3 = ['d', 'e', 'f']  # Отсортирован
arr4 = ['x', 'y']       # Отсортирован
arr5 = ['z']            # Отсортирован

# Вызов функции и вывод результата на экран
result = find_array(arr1, arr2, arr3, arr4, arr5)
print(result)
