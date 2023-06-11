from sys import argv
import sem_tasks.task2 as t2
import sem_tasks.task4 as t4
import sem_tasks.task5 as t5
import sem_tasks.task6 as t6
import sem_tasks.task7 as t7

import home_tasks.h_task1 as ht1
import home_tasks.h_task2_3 as ht2

if __name__ == "__main__":
    """Семинар"""
    # print(t2.choice_num(*(int(i) for i in argv[1:])))

    # print(t4.task4("2X2=?", ["4", "четыре", "four"]))

    # t5.ask_dict_riddles()

    # t6.write_history()
    # for i in t6.return_history():
    #     print(i)

    # print(t7.input_year("05.12.1984"))

    """"Домашние"""

    # print(ht1.input_year(input("Enter date: ")))

    COUNT_BOARDS = 4
    counter = 0
    while counter < COUNT_BOARDS:
        current_board = ht2.generate_board()
        if ht2.is_valid(current_board):
            counter += 1
            print(f"Solution {counter}:")
            ht2.print_board(current_board)
