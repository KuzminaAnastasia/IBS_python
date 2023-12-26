import csv
import statistics

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data


def calculate_average_age_by_position(arr):
    dic = dict()
    for row in arr:
        if row[2] in dic:
            dic[row[2]].append(int(row[1]))
        else:
            dic[row[2]] = [int(row[1])]
    res = dict()
    for key, value in dic.items():
        res[key] = statistics.mean(value)

    return res



file_path = 'data/employees.csv'
csv_data = read_csv_file(file_path)
csv_data = csv_data[1:]

print(calculate_average_age_by_position(csv_data))

