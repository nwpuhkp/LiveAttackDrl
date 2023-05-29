import csv
import matplotlib.pyplot as plt

# 定义csv路径
csv_path1 = "./backdoor_test_data/attack_data_clear_model.csv"
csv_path2 = "./live_attack_test_data/live_frozen_un_targeted_attack.csv"
# 打开csv文件
f1 = open(csv_path1, "r", encoding="utf-8")
f2 = open(csv_path2, "r", encoding="utf-8")
# 创建reader对象
reader1 = csv.reader(f1)
reader2 = csv.reader(f2)
# 创建空列表
data1 = []
data2 = []
# 遍历 reader 对象，将每一行的数据追加到列表中
for row in reader1:
    data1.append(float(row[0]))
for row in reader2:
    data2.append(float(row[0]))
# 关闭文件
f1.close()
f2.close()
# 绘制数据
plt.figure(figsize=(10, 6), dpi=200)
plt.plot(data1, color='#225d97', label='Clean Model', marker='o', linestyle='--')
plt.plot(data2, color='#bb4b19', label='Live Attack Model', marker='o', linestyle='--')
plt.title('Live Attack Model By Frozen Untargeted Attack under Attack Data')
plt.xlabel('Episode')
plt.ylabel('Reward')
plt.legend()
plt.ylim(-25, 25)
plt.grid(True, linestyle='--', color='gray', linewidth=0.5)
# 获取当前的坐标轴对象
ax = plt.gca()
# 设置 x 轴和 y 轴的刻度值，从而控制网格的大小
ax.set_xticks(range(0, 51, 5))
ax.set_yticks(range(-26, 26, 5))
# 设置背景颜色为浅蓝色
ax.set_facecolor('#e7e6f0')
# 显示图形
plt.show()

