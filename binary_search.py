def binary_search(list_for_search: list, item: int):
    low = 0  # Хранится нижняя граница списка
    high = len(list_for_search) - 1  # Хранится верхняя граница списка

    while low <= high:  # Условие Пока эта часть не сократится до одного элемента
        mid = (low + high) // 2  # Проверяем средний элемент
        guess = list_for_search[mid]
        if guess == item:  # Значение найдено
            return mid
        if guess > item:  # Значение больше
            high = mid - 1
        else:  # Значение меньше
            low = mid + 1

    return None  # Значение не найдено в списке


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Список должен быть отсортирован!!
test = binary_search(my_list, 3)  # Протестируем функцию попробуем найти число 3 в списке
print(test)  # Позиция на которой находится число которое мы искали
print(my_list[test])  # Проверяем
print(binary_search(my_list, -1))  # Если числа нет в списке то функция вернет None
