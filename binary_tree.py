import math
import matplotlib.pyplot as plt


DEFAULT_DEGREE = 90
DEFAULT_LENGTH = 20
DEFAULT_DEGREE_DELTA = 45
DEFAULT_DEEP = 10

tree_coordinates = []


def build_binary_tree(length, degree, delta, deep, x_start=0, y_start=0):
   
    degree_in_rad = math.radians(degree)
    x_end = x_start + length * math.cos(degree_in_rad)
    y_end = y_start + length * math.sin(degree_in_rad)

    tree_coordinates.append(([x_start, x_end], [y_start, y_end]))

    if deep == 0 or length < 2:
        return

    build_binary_tree(length * 0.8, degree - delta, delta, deep - 1, x_end, y_end)
    build_binary_tree(length * 0.8, degree + delta, delta, deep - 1, x_end, y_end)


def get_digital_input(message, default_value):

    while True:
        user_input = input(f'{message} (Натисніть ENTER для встановлення значення за замовчуванням: {default_value}): ')
        if user_input.strip() == "":
            return default_value
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Некоректне введення (необхідно ввести ціле число).")




if __name__ == '__main__':

    degree = get_digital_input('Введіть початковий кут розташування дерева (вважаємо, що 90 - вертикально вгору)', DEFAULT_DEGREE)
    length = get_digital_input('Введіть початкову довжину стовбура дерева', DEFAULT_LENGTH)
    delta = get_digital_input('Введіть початковий кут росту дочірніх гілок', DEFAULT_DEGREE_DELTA)
    deep = get_digital_input('Введіть глибину рекурсії (кількість розгалуджень)', DEFAULT_DEEP)

    tree_coordinates.clear()

    build_binary_tree(length, degree, delta, deep)

    print("\nTree coordinates generated!")
    # print(tree_coordinates) # Тестове виведення списку координат, за необхідності виведення треба розкоментувати на початку строки


    fig, ax = plt.subplots(figsize=(10, 10)) 

    for segment in tree_coordinates:
        x_coords = segment[0]
        y_coords = segment[1]
        ax.plot(x_coords, y_coords, color='green', linewidth=1)

    ax.set_aspect('equal', adjustable='box')
    ax.set_title(f'Бінарне дерево \n(Глибина рекурсії: {deep}, початкова довжина стовбура: {length} \nпочатковий кут росту: {degree}, кут відгалудження гілок: {delta})')
    ax.set_xlabel('X-coordinate')
    ax.set_ylabel('Y-coordinate')
    plt.grid(False)
    plt.show()