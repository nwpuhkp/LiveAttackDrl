import csv
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

# live frozen attack
csv_path1 = "backdoor_test_data/attack_data_clear_model.csv"
csv_path2 = "live_attack_test_data/live_frozen_strong_targeted_attack.csv"
csv_path3 = "live_attack_test_data/live_frozen_weak_targeted_attack.csv"
csv_path4 = "live_attack_test_data/live_frozen_un_targeted_attack.csv"
# # live attack
# csv_path1 = "backdoor_test_data/attack_data_clear_model.csv"
# csv_path2 = "live_attack_test_data/live_strong_targeted_attack.csv"
# csv_path3 = "live_attack_test_data/live_weak_targeted_attack.csv"
# csv_path4 = "live_attack_test_data/live_un_targeted_attack.csv"
# # backdoor frozen attack
# csv_path1 = "backdoor_test_data/attack_data_clear_model.csv"
# csv_path2 = "backdoor_test_data/attack_data_frozen_strong_targeted_attack_model.csv"
# csv_path3 = "backdoor_test_data/attack_data_frozen_weak_targeted_attack_model.csv"
# csv_path4 = "backdoor_test_data/attack_data_frozen_un_targeted_attack_model.csv"
# # backdoor attack
# csv_path1 = "backdoor_test_data/attack_data_clear_model.csv"
# csv_path2 = "backdoor_test_data/attack_data_strong_targeted_attack_model.csv"
# csv_path3 = "backdoor_test_data/attack_data_weak_targeted_attack_model.csv"
# csv_path4 = "backdoor_test_data/attack_data_un_targeted_attack_model.csv"
# # clear frozen attack
# csv_path1 = "backdoor_test_data/attack_data_clear_model.csv"
# csv_path2 = "backdoor_test_data/clear_data_frozen_strong_targeted_attack_model.csv"
# csv_path3 = "backdoor_test_data/clear_data_frozen_weak_targeted_attack_model.csv"
# csv_path4 = "backdoor_test_data/clear_data_frozen_un_targeted_attack_model.csv"
# # clear attack
# csv_path1 = "backdoor_test_data/attack_data_clear_model.csv"
# csv_path2 = "backdoor_test_data/clear_data_strong_targeted_attack_model.csv"
# csv_path3 = "backdoor_test_data/clear_data_weak_targeted_attack_model.csv"
# csv_path4 = "backdoor_test_data/clear_data_un_targeted_attack_model.csv"
# 打开csv文件
f1 = open(csv_path1, "r", encoding="utf-8")
f2 = open(csv_path2, "r", encoding="utf-8")
f3 = open(csv_path3, "r", encoding="utf-8")
f4 = open(csv_path4, "r", encoding="utf-8")
# 创建reader对象
reader1 = csv.reader(f1)
reader2 = csv.reader(f2)
reader3 = csv.reader(f3)
reader4 = csv.reader(f4)
# 创建空列表
data1 = []
data2 = []
data3 = []
data4 = []
# 遍历 reader 对象，将每一行的数据追加到列表中
for row in reader1:
    data1.append(float(row[0]))
for row in reader2:
    data2.append(float(row[0]))
for row in reader3:
    data3.append(float(row[0]))
for row in reader4:
    data4.append(float(row[0]))
# 关闭文件
f1.close()
f2.close()
f3.close()
f4.close()
# 绘制数据
plt.figure(figsize=(10, 6), dpi=600)
plt.rc('font', family='Times New Roman')
# live frozen attack
plt.plot(data1, color='#0072bd', label='Clean', linestyle='-', linewidth=3, marker='o')
plt.plot(data2, color='#7e2f8e', label='Frozen Strong Targeted', linestyle='-', linewidth=3, marker='o')
plt.plot(data3, color='#77ac30', label='Frozen Weak Targeted', linestyle='-', linewidth=3, marker='o')
plt.plot(data4, color='#d95319', label='Frozen Untargeted', linestyle='-', linewidth=3, marker='o')
plt.title('Clean Model vs Frozen Retrained Attack Model under Live Attack Data', fontsize=22)
# # live attack
# plt.plot(data1, color='#0072bd', label='Clean', linestyle='-', linewidth=3, marker='o')
# plt.plot(data2, color='#7e2f8e', label='Strong Targeted', linestyle='-', linewidth=3, marker='o')
# plt.plot(data3, color='#77ac30', label='Weak Targeted', linestyle='-', linewidth=3, marker='o')
# plt.plot(data4, color='#d95319', label='Untargeted', linestyle='-', linewidth=3, marker='o')
# plt.title('Clean Model vs Attack Model under Live Attack Data', fontsize=22)
# # backdoor frozen attack
# plt.plot(data1, color='#0072bd', label='Clean', linestyle='-', linewidth=3, marker='o')
# plt.plot(data2, color='#7e2f8e', label='Frozen Strong Targeted', linestyle='-', linewidth=3, marker='o')
# plt.plot(data3, color='#77ac30', label='Frozen Weak Targeted', linestyle='-', linewidth=3, marker='o')
# plt.plot(data4, color='#d95319', label='Frozen Untargeted', linestyle='-', linewidth=3, marker='o')
# plt.title('Clean Model vs Frozen Retrained Attack Model under Backdoor Attack Data', fontsize=22)
# # backdoor attack
# plt.plot(data1, color='#0072bd', label='Clean', linestyle='-', linewidth=3, marker='o')
# plt.plot(data2, color='#7e2f8e', label='Strong Targeted', linestyle='-', linewidth=3, marker='o')
# plt.plot(data3, color='#77ac30', label='Weak Targeted', linestyle='-', linewidth=3, marker='o')
# plt.plot(data4, color='#d95319', label='Untargeted', linestyle='-', linewidth=3, marker='o')
# plt.title('Clean Model vs Attack Model under Backdoor Attack Data', fontsize=22)
# # clear frozen attack
# plt.plot(data1, color='#0072bd', label='Clean', linestyle='-', linewidth=3, marker='o')
# plt.plot(data2, color='#7e2f8e', label='Frozen Strong Targeted', linestyle='-', linewidth=3, marker='o')
# plt.plot(data3, color='#77ac30', label='Frozen Weak Targeted', linestyle='-', linewidth=3, marker='o')
# plt.plot(data4, color='#d95319', label='Frozen Untargeted', linestyle='-', linewidth=3, marker='o')
# plt.title('Clean Model vs Frozen Retrained Attack Model under Clean Data', fontsize=22)
# # clear attack
# plt.plot(data1, color='#0072bd', label='Clean', linestyle='-', linewidth=3, marker='o')
# plt.plot(data2, color='#7e2f8e', label='Strong Targeted', linestyle='-', linewidth=3, marker='o')
# plt.plot(data3, color='#77ac30', label='Weak Targeted', linestyle='-', linewidth=3, marker='o')
# plt.plot(data4, color='#d95319', label='Untargeted', linestyle='-', linewidth=3, marker='o')
# plt.title('Clean Model vs Attack Model under Clean Data', fontsize=22)

plt.xlabel('Episode', fontsize=22)
plt.ylabel('Reward', fontsize=22, labelpad=1.0)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.legend(loc='lower right', fontsize=18)
plt.ylim(-25, 25)
plt.grid(True, linestyle='--', color='gray', linewidth=1)
# 获取当前的坐标轴对象
ax = plt.gca()
# 设置 x 轴和 y 轴的刻度值，从而控制网格的大小
ax.set_xticks(range(0, 51, 5))
ax.set_yticks(range(-26, 26, 5))
# plt.tight_layout()
plt.subplots_adjust(left=0.088, bottom=0.12, right=0.975, top=0.94)
plt.annotate(r"Recover", xy=(40, 4), xytext=(36, -8),
             arrowprops=dict(facecolor="green", shrink=0.05, width=8, headwidth=20, headlength=20)
             , fontsize=28, color='green')
plt.annotate(r"Replace", xy=(7, 2), xytext=(3.3, -8),
             arrowprops=dict(facecolor="red", shrink=0.05, width=8, headwidth=20, headlength=20)
             , fontsize=28, color='red')
plt.savefig("frozen_live_attack.pdf", format="pdf")
# 设置背景颜色为浅蓝色
# ax.set_facecolor('#e7e6f0')
# 显示图形
plt.show()
