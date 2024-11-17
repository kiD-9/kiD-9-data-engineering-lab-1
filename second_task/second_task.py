import sys
from math import sqrt


def calc_lines_result(lines):
    results = []
    for line in lines:
        result = 0
        for word in  line.split():
            num = int(word)
            if num > 0:
                result += sqrt(num)
        results.append(int(result))
    return results



def read_file_lines():
    with open("../data/second_task.txt", encoding="utf-8") as file:
        return file.readlines()


def write_result_to_file(lines_result):
    with open("second_task_result.txt", "w", encoding="utf-8") as file:
        sum_value = 0
        max_value = -1
        min_value = sys.maxsize
        for line_result in lines_result:
            sum_value += line_result
            max_value = max(max_value, line_result)
            min_value = min(min_value, line_result)
            file.write(f"{line_result}\n")

        file.write("-----------\n")
        file.write(f"{sum_value}\n\n")
        file.write(f"{max_value}\n")
        file.write(f"{min_value}")


lines = read_file_lines()
lines_result = calc_lines_result(lines)
write_result_to_file(lines_result)
