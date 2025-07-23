from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')
print(message)


def CalculateSquareRoot(num: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(num)


def calc(your_number: float) -> str:
    """Dockstring."""
    if your_number <= 0:
        return
    final_calc: float = CalculateSquareRoot(your_number)
    print(f'Мы вычислили квадратный корень из '
          f'введённого вами числа. Это будет: {final_calc}')


calc(25.5)