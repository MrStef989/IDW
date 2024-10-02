import numpy as np


def idw(x, y, z, xi, yi, power=2):
    dist = np.sqrt((x - xi) ** 2 + (y - yi) ** 2)
    if np.any(dist == 0):
        return z[np.argmin(dist)]

    weights = 1 / dist ** power

    zi = np.sum(weights * z) / np.sum(weights)

    return zi


def get_user_input():

    n = int(input("Введите количество известных точек: "))
    x = np.zeros(n)
    y = np.zeros(n)
    z = np.zeros(n)

    for i in range(n):
        x[i] = float(input(f"Введите координату x для точки {i + 1}: "))
        y[i] = float(input(f"Введите координату y для точки {i + 1}: "))
        z[i] = float(input(f"Введите значение z для точки {i + 1}: "))

    return x, y, z


def generate_random_data(n):

    x = np.random.uniform(0, 10, n)
    y = np.random.uniform(0, 10, n)
    z = np.random.uniform(0, 10, n)
    return x, y, z



def main():
    print("Выберите способ задания данных:")
    print("1. Ввести координаты и значения вручную")
    print("2. Сгенерировать случайные данные")

    choice = input("Ваш выбор (1/2): ")

    if choice == "1":
        x, y, z = get_user_input()
    elif choice == "2":
        n = int(input("Введите количество точек для генерации: "))
        x, y, z = generate_random_data(n)
        print(f"Сгенерированные координаты X: {x}")
        print(f"Сгенерированные координаты Y: {y}")
        print(f"Сгенерированные значения Z: {z}")
    else:
        print("Некорректный выбор, завершение программы.")
        return

    xi = float(input("Введите координату X для интерполяции: "))
    yi = float(input("Введите координату Y для интерполяции: "))

    zi = idw(x, y, z, xi, yi)
    print(f"Интерполированное значение в точке ({xi}, {yi}): {zi}")


if __name__ == "__main__":
    main()
