import pandas as pd

csv1 = "clear_data_clear_model.csv"
csv2 = "clear_data_strong_targeted_attack_model.csv"
csv3 = "clear_data_clear_vs_strong.csv"
# 合并两个各有一列的csv文件为一个两行的csv文件
df1 = pd.read_csv(csv1)
df2 = pd.read_csv(csv2)
# 将列转换为行
df1 = df1.T
df2 = df2.T
# 合并两个csv文件
df = pd.concat([df1, df2])
# 保存到csv
df.to_csv(csv3, index=False, header=False)
print("合并完成！")

