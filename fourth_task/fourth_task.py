import csv
import sys


def remove_description_column(extracted_csv):
    for row in extracted_csv:
        row.pop('description')

    return extracted_csv


def find_all_parameters(extracted_csv):
    sum_price = 0
    max_quantity = -1
    min_price = sys.maxsize
    for row in extracted_csv:
        price = float(row['price'])
        sum_price += price
        if price < min_price:
            min_price = price
        quantity = int(row['quantity'])
        if quantity > max_quantity:
            max_quantity = quantity

    avg_price = sum_price / len(extracted_csv)
    return avg_price, max_quantity, min_price


def filter_by_status(extracted_csv):
    result = []
    for row in extracted_csv:
        if row['status'] == 'Out of Stock':
            result.append(row)

    return result


def read_csv():
    extracted_csv = []
    with open("../data/fourth_task.txt", newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=',', quotechar='"')
        for row in reader:
            extracted_csv.append(row)

    return extracted_csv


def write_filtered_csv_to_file(filtered_data):
    with open("fourth_task_result.csv", "w", encoding="utf-8", newline='') as file:
        writer = csv.DictWriter(file, delimiter=',', quotechar='"', fieldnames=filtered_data[0].keys())
        writer.writeheader()
        writer.writerows(filtered_data)


def write_parameters_to_file(avg_price, max_quantity, min_price):
    with open("fourth_task_result.txt", "w", encoding="utf-8") as file:
        file.write(f"{avg_price}\n")
        file.write(f"{max_quantity}\n")
        file.write(f"{min_price}\n")


extracted_csv = read_csv()
extracted_csv = remove_description_column(extracted_csv)

avg_price, max_quantity, min_price = find_all_parameters(extracted_csv)
write_parameters_to_file(avg_price, max_quantity, min_price)

filtered_data = filter_by_status(extracted_csv)
write_filtered_csv_to_file(filtered_data)
