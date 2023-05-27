import csv


def calculate_positive_sum(path):
    positive_sum = 0
    num = 0
    with open(path, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            value = float(row[0])
            if value > 0:
                num += 1
                positive_sum += value
    return positive_sum, num


# 参考上述函数，写一个只计算负数的函数
def calculate_negative_sum(path):
    negative_sum = 0
    num = 0
    with open(path, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            value = float(row[0])
            if value < 0:
                num += 1
                negative_sum += value
    return negative_sum, num


file_path = "./backdoor_test_data/attack_data_strong_targeted_attack_model.csv"
# total_sum, total_num = calculate_positive_sum(file_path)
# print("Positive sum: ", total_sum)
# print("Positive sum/num: ", total_sum/total_num)
total_sum, total_num = calculate_negative_sum(file_path)
print("Negative sum: ", total_sum)
print("Negative sum/num: ", total_sum/total_num)
