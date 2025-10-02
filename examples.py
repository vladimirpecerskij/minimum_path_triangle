
from triangle_solver import solve_triangle

def main():
    print("Минимальный путь в треугольнике")
    print("=" * 40)
    
    # Пример 1
    triangle1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    min_sum1, path1 = solve_triangle(triangle1)
    
    print("Пример 1:")
    print("Треугольник:")
    for row in triangle1:
        print(" " * (len(triangle1) - len(row)), row)
    print(f"Минимальный путь: {' → '.join(map(str, path1))}")
    print(f"Результат: {min_sum1}")
    print()
    
    # Пример 2
    triangle2 = [[-1], [2, 3], [1, -1, -3], [4, 2, 1, 3]]
    min_sum2, path2 = solve_triangle(triangle2)
    
    print("Пример 2:")
    print("Треугольник:")
    for row in triangle2:
        print(" " * (len(triangle2) - len(row)), row)
    print(f"Минимальный путь: {' → '.join(map(str, path2))}")
    print(f"Результат: {min_sum2}")
    print()
    
    # Дополнительный пример
    triangle3 = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]
    min_sum3, path3 = solve_triangle(triangle3)
    
    print("Пример 3:")
    print("Треугольник:")
    for row in triangle3:
        print(" " * (len(triangle3) - len(row)), row)
    print(f"Минимальный путь: {' → '.join(map(str, path3))}")
    print(f"Результат: {min_sum3}")

if __name__ == "__main__":
    main()
