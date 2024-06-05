def find_smallest(array: list) -> int:
    smallest = array[0]  # Хранение наимешьшего значения
    smallest_index = 0  # Хранение индекса наименьшего значения
    for i in range(1, len(array)):
        if array[i] < smallest:  # Сравниваем значение с первым числом которое стоит по индексы 0
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr: list) -> list:  # Сортируем массив
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)  # Находим наименьший элемент в массиве
        new_arr.append(arr.pop(smallest))  # Добавляем значение в новый массив и удаляем из старого
    return new_arr  # Возвращаем отсортированный массив


print(selection_sort([5, 3, 6, 2, 10]))
