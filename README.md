Решение задачи поиска минимальной суммы пути в треугольнике с использованием динамического программирования.

## Описание задачи

Дан треугольник в виде списка списков. Необходимо найти минимальную сумму пути от вершины до основания, где на каждом шаге можно перемещаться только на соседний элемент в строке ниже.

## Алгоритмическая сложность

- **Время:** O(n²), где n - количество строк
- **Память:** O(n²) для полного пути или O(n) для оптимизированной версии

## Использование

### Базовое использование

#python
from triangle_solver import solve_triangle

triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
min_sum, path = solve_triangle(triangle)

print(f"Минимальная сумма: {min_sum}")
print(f"Путь: {path}")
Расширенное использование
python
from triangle_solver import TriangleSolver

solver = TriangleSolver()

# Только минимальная сумма
result = solver.minimum_path_sum(triangle)

# Оптимизированная версия (меньше памяти)
result = solver.minimum_path_sum_optimized(triangle)

# Полный путь
min_sum, path = solver.find_actual_path(triangle)
Примеры
Пример 1
text
    [2]
   [3,4]
  [6,5,7]
 [4,1,8,3]
Минимальный путь: 2 → 3 → 5 → 1
Результат: 11

Пример 2
text
    [-1]
   [2,3]
  [1,-1,-3]
 [4,2,1,3]
Минимальный путь: -1 → 3 → -3 → 1
Результат: 0

Запуск тестов
bash
python test_triangle.py
Запуск примеров
bash
python examples.py
Требования
Python 3.6+

text

## Инструкции по запуску:

1. Создайте папку проекта:
bash:
mkdir minimum_path_triangle
cd minimum_path_triangle
Создайте файлы с кодом как указано выше

Запустите тесты:

bash:
python test_triangle.py
Запустите примеры:

bash:
python examples.py
Проект готов к использованию и соответствует всем требованиям задачи!

