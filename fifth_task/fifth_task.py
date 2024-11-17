from bs4 import BeautifulSoup
import csv


def extract_data_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    headers = []
    header = soup.find("thead").find("tr")

    for item in header:
        value = item.get_text(strip=True)
        if len(value) > 0:
            headers.append(value)

    data = []
    rows = soup.find("tbody").find_all("tr")
    for row in rows:
        sub_data = {}
        i = 0
        for cell in row:
            value = cell.get_text(strip=True)
            if len(value) > 0:
                sub_data[headers[i]] = value
                i += 1
        data.append(sub_data)

    return data


def read_file():
    with open("../data/fifth_task.html", newline='', encoding="utf-8") as file:
        return file.read()


def write_data_to_csv(data):
    with open("fifth_task_result.csv", "w", encoding="utf-8", newline='') as file:
        writer = csv.DictWriter(file, delimiter=',', quotechar='"', fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


html = read_file()
data = extract_data_from_html(html)
write_data_to_csv(data)
