"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""
import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    return[i for i, a in enumerate(nums) if a % 2 == 0]

nums = [a for a in range(10000)]

print(timeit.timeit("func_1(nums)",
                    globals=globals(),
                    number=1000)) #-> 1.2889613

print(timeit.timeit("func_2(nums)",
                    globals=globals(),
                    number=1000)) #-> 1.1655398

"""С помощью ls мы сразу создаем список и его содержимоев вместо последовательного создания, это ускоряет процесс проценвот на 20"""