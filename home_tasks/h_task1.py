# В модуль с проверкой даты добавьте возможность
# запуска в терминале с передачей даты на проверку.


def input_year(date: str) -> bool:
    day, month, year = (int(i) for i in date.split("."))
    if 1 <= year <= 9999 and 0 < day <= max_days(month, year):
        return True
    return False


def max_days(month: int, year: int) -> int:
    DICT_MONTHS = {
        30: [4, 6, 9, 11],
        31: [1, 3, 5, 7, 8, 10, 12],
        28: [2]
        }
    for key, value in DICT_MONTHS.items():
        if month in value:
            if key == 28 and is_leap(year):
                return key + 1
            return key
    return 0


def is_leap(year: int) -> bool:
    CHECK_FOUR = 4
    CHECK_HUNDRED = 100
    CHECK_4HUNDRED = 400
    if year % CHECK_FOUR == 0 and (year % CHECK_HUNDRED != 0 or year % CHECK_4HUNDRED == 0):
        return True
    return False
