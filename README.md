# Python Tasks

## №1
> На языке Python написать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.

Пример из условия:
```Python
def isEven(value):
    return value % 2 == 0
```

Альтернативный вариант функции:
```Python
def isEven2(value):
    return divmod(value, 2)[1] == 0
```

Сравнивая многократное (1000000) количество вызовов обеих функций показало, что на первый вариант функции уходит меньше времени, в то время как альтернативный вариант будет медленее из-за постоянного обращения к divmod.

Для проверки этого был выполнен вариант, где функция сохраняется в переменную с её последующим многократным вызовом:
```Python
dm = divmod
for i in range(1000000):
        dm(i, 2)[1] == 0
```
Такое решение уже +/- совпадает по скорости выполнения с первым примером.
 
В итоге оба варианта подходят для выполнения данной задачи, однако в случаях где нужен многократный вызов функции и нет возможности локализовать divmod в переменную (как в примере выше) - предпочтительнее использовать первый вариант.

## №2
> На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

Класс **FIFOList** - реализован с помощью списка и использованием стандартных функций *insert(0,item)* (с предварительной проверкой заполненности списка) для добавления элементов и *pop()*.

Класс **FIFODeque** - реализован с помощью двусторонней очереди *deque*. Реализация методов класса выполнена аналогично FIFOList, разве что уже нет необходимости проверять заполнен ли буфер или нет (добавление в deque автоматически убирает крайний элемент, если у него выставлен фиксированный размер).

Результары скорость работы обоих классов показали, что у класса **FIFODeque** есть преимущество в скорости заполнения, тогда как оба класса показали примерно одинаковое время для вывода элементов из буфера.

Это связано с тем, что в **FIFODeque** для заполнения используется *appendleft(item)* (с постоянной сложностью O(1)), но для вывода используется *pop()* (так же как и в **FIFOList**).

## №3
> На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить, почему вы считаете, что функция соответствует заданным критериям.
