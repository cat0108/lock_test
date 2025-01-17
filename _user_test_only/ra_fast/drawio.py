# import pandas as pd
# import matplotlib.pyplot as plt

# # 读取 CSV 文件
# df = pd.read_csv('output.csv')

# # 删除包含0的行
# df_cleaned = df[(df != 0).all(axis=1)]

# # 绘制折线图
# plt.figure(figsize=(10, 6))

# # 为每一列（对应每个CPU）绘制折线
# for column in df_cleaned.columns:
#     plt.plot(df_cleaned[column], label=column)

# # 添加图例
# plt.legend()

# # 添加标题和标签
# plt.title("CPU Wait Time")
# plt.xlabel("Sample Index")
# plt.ylabel("Wait Time (ns)")

# # 显示图形
# plt.grid(True)
# plt.savefig("output.png")



# # 统计每列的有效数据点（非零）
# valid_data_points = (df_cleaned != 0).sum().sum()

# # 输出总有效数据点数量
# print(f"总共有效的数据点数量: {valid_data_points}")

import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
df = pd.read_csv('output.csv')

non_zero_above_100 = df[(df > 200)].stack().values

# 绘制聚合后的折线图
plt.figure(figsize=(10, 6))

# 绘制非零且大于100的数据点的折线
plt.plot(non_zero_above_100, label='Non-zero and >100 Data')


# 添加标题和标签
plt.title("Non-zero CPU Wait Times")
plt.xlabel("Index")
plt.ylabel("Wait Time (ns)")

plt.savefig("output.png")

print(non_zero_above_100.max())