def remove_nans(lines):
    matrix = []
    for line in lines:
        split = line.split()
        for i in range(len(split)):
            if split[i] == 'N/A':
                split[i] = (split[i - 1] + int(split[i + 1])) / 2
            else:
                split[i] = int(split[i])
        matrix.append(split)

    return matrix


def filter_matrix(matrix):
    for i in range(len(matrix)):
        filtered_row = []
        for cell in matrix[i]:
            if cell % 3 == 0:
                filtered_row.append(cell)
        matrix[i] = filtered_row

    return matrix


def read_file_lines():
    with open("../data/third_task.txt", encoding="utf-8") as file:
        return file.readlines()


def write_result_to_file(matrix):
    with open("third_task_result.txt", "w", encoding="utf-8") as file:
        for row in matrix:
            file.write(f"{sum(row)}\n")


lines = read_file_lines()
matrix = remove_nans(lines)
matrix = filter_matrix(matrix)
write_result_to_file(matrix)
