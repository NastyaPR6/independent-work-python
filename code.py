# Проверка массива на сортировку
def check_array(arr):
    for i in range(len(arr)):
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
