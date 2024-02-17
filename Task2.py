def binary_search_with_upper_bound(arr, target):
    """
    Функція двійкового пошуку, що повертає кількість ітерацій, необхідних для знаходження елемента,
    та "верхню межу" для заданого значення в відсортованому масиві.
    
    :param arr: Відсортований масив, у якому ведеться пошук.
    :param target: Значення, яке потрібно знайти.
    :return: Кортеж, де перший елемент - кількість ітерацій пошуку, другий - "верхня межа".
    """
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    if upper_bound is None:  # Якщо елемент не знайдено, верхня межа буде першим елементом, який більший за максимальний у масиві
        upper_bound = float('inf')

    return iterations, upper_bound

# Приклад використання:
arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
target = 3.5
result = binary_search_with_upper_bound(arr, target)
print(f"Ітерації: {result[0]}, Верхня межа: {result[1]}")