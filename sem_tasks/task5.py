# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

def ask_riddle(riddle: str, guesses: list[str], count_tryes: int = 3):
    print(riddle)
    for i in range(count_tryes):
        current_guess = input("Введите отгадку:")
        if current_guess in guesses:
            print(f"Вы угадали с попытки №{i + 1}")
            return i + 1
        else:
            print("Неправильно")
    print("Попытки кончились")
    return 0


def ask_dict_riddles():
    COUNT_TRYES = 3
    DICT_RIDDLES = {
        "2X2=": ["4", "four"],
        "3X3=": ["9", "nine"],
        "5+5=": ["10", "ten"]
    }
    for key, value in DICT_RIDDLES.items():
        print(ask_riddle(key, value, COUNT_TRYES))


if __name__ == "__main__":
    print(ask_riddle("2X2=?", ["4", "четыре", "four"]))
    ask_dict_riddles()
