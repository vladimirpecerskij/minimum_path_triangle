class TriangleSolver:
    """
    Класс для нахождения минимальной суммы пути в треугольнике
    """
    
    def minimum_path_sum(self, triangle):
        """
        Находит минимальную сумму пути от вершины до основания треугольника
        
        Args:
            triangle: список списков, представляющий треугольник
            
        Returns:
            int: минимальная сумма пути
        """
        if not triangle:
            return 0
        
        # Создаем копию треугольника для динамического программирования
        dp = [row[:] for row in triangle]
        
        # Начинаем с предпоследней строки и движемся вверх
        for i in range(len(dp) - 2, -1, -1):
            for j in range(len(dp[i])):
                # Для каждого элемента прибавляем минимум из двух возможных путей ниже
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1])
        
        return dp[0][0]
    
    def minimum_path_sum_optimized(self, triangle):
        """
        Оптимизированная версия с O(n) по памяти
        """
        if not triangle:
            return 0
        
        # Используем только одну дополнительную строку
        dp = triangle[-1][:]
        
        # Поднимаемся снизу вверх
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        
        return dp[0]
    
    def find_actual_path(self, triangle):
        """
        Находит сам путь с минимальной суммой
        
        Returns:
            tuple: (минимальная сумма, список пути)
        """
        if not triangle:
            return 0, []
        
        n = len(triangle)
        dp = [[0] * len(row) for row in triangle]
        path = [[0] * len(row) for row in triangle]
        
        # Инициализируем последнюю строку
        for j in range(len(triangle[-1])):
            dp[-1][j] = triangle[-1][j]
        
        # Заполняем снизу вверх
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                if dp[i + 1][j] < dp[i + 1][j + 1]:
                    dp[i][j] = triangle[i][j] + dp[i + 1][j]
                    path[i][j] = j  # идем влево
                else:
                    dp[i][j] = triangle[i][j] + dp[i + 1][j + 1]
                    path[i][j] = j + 1  # идем вправо
        
        # Восстанавливаем путь
        actual_path = []
        current_col = 0
        for i in range(n):
            actual_path.append(triangle[i][current_col])
            if i < n - 1:
                current_col = path[i][current_col]
        
        return dp[0][0], actual_path


def solve_triangle(triangle):
    """
    Упрощенная функция для решения треугольника
    """
    solver = TriangleSolver()
    min_sum, path = solver.find_actual_path(triangle)
    return min_sum, path
