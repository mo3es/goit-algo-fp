import random


PREDEFINED_VALUES = { 2: '2,78% (1/36)', 3: '5.56% (2/36)', 4: '8,33% (3/36)', 5: '11,11% (4/36)',
                     6: '13.89% (5/36)', 7: '16,67% (6/36)', 8: '13.89% (5/36)', 9: '11,11% (4/36)',
                    10: '8,33% (3/36)', 11: '5.56% (2/36)',  12: '2,78% (1/36)'}
def two_dice_imitation(quantity: int) -> dict:

    results = {}

    for i in range(2, 13):
        results[i] = 0

    for _ in range(quantity):
        key = random.randint(1, 6) + random.randint(1, 6)
        results[key] += 1

    return results


def reformat_data(data: dict, quantity: int) -> dict:

    for key, value in data.items():
        data[key] = [value, value * 100 / quantity, PREDEFINED_VALUES[key]]

    return data


def display(data: dict):
    print('____' * 18)
    print("|\tСума\t|   Випадінь    |    Відсоток   |\tТеоретичні\t|")
    print('----' * 18)
    for key, value in data.items():
        print(f'|\t{key}\t|\t{value[0]}\t|\t{value[1]}\t|\t{value[2]}\t|')
        print('----' * 18)

    print("Як видно з таблиці, отримані методом симуляції випадкових випадінб відповідають теоретичним (розрахунковим) даним")
    


if __name__ == '__main__':
    n = 100000
    data = two_dice_imitation(n)

    display(reformat_data(data, n))