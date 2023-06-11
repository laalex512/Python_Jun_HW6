# Добавьте в модуль с загадками функцию, которая принимает на вход строку
# (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания
# из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.


_DICT_GUESSES = dict()


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


def write_history():
    COUNT_TRYES = 3
    DICT_RIDDLES = {
        "2X2=": ["4", "four"],
        "3X3=": ["9", "nine"],
        "5+5=": ["10", "ten"]
    }
    for key, value in DICT_RIDDLES.items():
        _DICT_GUESSES[key] = ask_riddle(key, value, COUNT_TRYES)
    print(_DICT_GUESSES)


def return_history():
    for key, value in _DICT_GUESSES.items():
        yield f'Загадка "{key}" угадана c попытки № {value}'


if __name__ == "__main__":
    print(ask_riddle("2X2=?", ["4", "четыре", "four"]))
