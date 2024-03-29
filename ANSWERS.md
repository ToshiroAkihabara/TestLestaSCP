# Тестовое задание на позицию Server Core Programmer.


# Ответ №1:

Использование побитового оператора & (AND) позволяет немного увеличить скорость  работы засчет низкоуровневой операции проверки последнего бита входного числа в двоичной системе счисления. В четных числах последним битом является 0, что в соответствии с таблицой истинности 0 & 1 == 0 будет являться истинным или четным числом.
Это и является главным плюсом данного подхода в определении четности целого числа. Минусом является сложность в понимании самого процесса работы побитовых операций в отличии от функции получения остатка от деления, которая реализована в первом алгоритме.

# Ответ №2:

Очередь FIFO, реализованная с помощью списка и встроенных операций append() и pop(), проста в исполнении и не требует импорта дополнительных модулей. Однако имеет существенный недостаток. В результате извлечения элемента из начала списка с помощью метода pop(0) все последующие за ним элементы сдвигаются влево за время O(n). В результате этого асимптотическая сложность работы такого алгоритма составит O(n), где n - это число элементов в очереди.
-   Время работы O(n): Линейная скорость работы

Очередь FIFO, реализованная с помощью класса deque (двухсторонней очереди) модуля collections имеет существенное преимущество в скорости работы по сравнение с предыдущим методом. За счет того, что он реализован на базе двухстороннего связного списка скорость работы такого алгоритма составляет O(1).
-   Время работы O(1): Константная скорость работы


# Ответ №3:

Существует несколько эффективных и стабильных сортировок у которых макимальная асимптотическая сложность 
работы составляет O(nlogn). Это быстрая сортировка, сортировка слияниеми и сортировка кучей. В зависимости от входного массива та или иная сортировка будет наиболее эффективна, однако при входных данных любого размера наиболее стабильнее и быстрее показывает себя сортировка слиянием. Она стабильнее, чем сортировка кучей и быстрее в худшем случае, чем быстрая сортировка. Кроме этого, сортировка слиянием используется в гибридной сортировке timsort, являющейся встроенной сортировкой языка программирования Python.