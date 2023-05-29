# 导入模块
import pandas as pd
import numpy as np

# 读取csv文件
df = pd.read_csv("./live_attack_test_data/live_weak_targeted_attack.csv", header=None)

# 获取第一列的数据
data = df[0]

# 对第7到第15的数据求和和平均数
data1 = data[6:15]
sum1 = np.sum(data1)
avg1 = np.mean(data1)

# 对第32到第40的数据求和和平均数
data2 = data[31:40]
sum2 = np.sum(data2)
avg2 = np.mean(data2)

# 对第1到第6的数据求和和平均数
data3 = data[:6]
sum3 = np.sum(data3)
avg3 = np.mean(data3)

# 对第41到最后的数据求和和平均数
data4 = data[40:]
sum4 = np.sum(data4)
avg4 = np.mean(data4)

# 打印结果
# print("第7到第15的数据之和为：", sum1)
# print("第7到第15的数据的平均数为：", avg1)
# print("第32到第40的数据之和为：", sum2)
# print("第32到第40的数据的平均数为：", avg2)
# print("第1到第6的数据之和为：", sum3)
# print("第1到第6的数据的平均数为：", avg3)
# print("第41到最后的数据之和为：", sum4)
# print("第41到最后的数据的平均数为：", avg4)

# 对第1到第6和第41到最后的数据求和和平均数
data34 = np.concatenate([data[:6], data[40:]]) # 合并两个数据段
sum34 = np.sum(data34) # 求和
avg34 = np.mean(data34) # 求平均数

# 对第7到第15和第32到第40的数据求和和平均数
data12 = np.concatenate([data[6:15], data[31:40]]) # 合并两个数据段
sum12 = np.sum(data12) # 求和
avg12 = np.mean(data12) # 求平均数

# 打印结果
print("第1到第6和第41到最后的数据之和为：", sum34)
print("第1到第6和第41到最后的数据的平均数为：", avg34)
print("第7到第15和第32到第40的数据之和为：", sum12)
print("第7到第15和第32到第40的数据的平均数为：", avg12)

print("差异:", (avg34 - avg12)/21)
