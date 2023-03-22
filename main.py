def binary_search(array, element, left, right):  # функция - алгоритм двоичного поиска
    global midd
    if left > right:
        return midd - 1
    middle = (right + left) // 2
    midd = middle
    if array[middle] == element:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


def sorted_array():  # функция - алгоритм сортировки вставками.
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    print("отсортированный список:", array)
    return array


def changeText(
        text):  # Функция убирает все лишнее и возвращает список из цифр + защита от ошибочного ввода пользователем.
    for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя':
        text = text.replace(i, ' ')
    return text.split()


numbers = input("Введите через пробел целые числа")  # Ввод чисел пользователем
listnum = changeText(numbers)
array = list(map(int, listnum))  # список чисел
array_len = len(array)
print("Вы ввели следующие числа", array)
print("Максимальное число в списке -", max(array))
print("Минимальное число в списке -", min(array))
element = int(input("Введите число, чтобы получить номер позиции элемента, который меньше введенного Вами числа, \n а следующий за ним больше или равен этому числу. \n Число должно быть меньше максимального и больше минимального в списке:"))  # введенное пользователем число

if min(array)<=element<=max(array):
    print(f"Вы ввели число -  {element} ")
    print("Номер позиции элемента: ", binary_search(sorted_array(), element, 1, array_len))  # применяем алгоритм двоичного поиска и получаем ответ
else:
    print("Число за границами списка чисел")



