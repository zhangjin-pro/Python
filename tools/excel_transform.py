"""
excel数据转置
指标ID	BJ_SL_A21	BJ_SL_A22	BJ_SL_A23
2023-07	-11.40 	-9.50 	1.20
2023-08	-11.30 	-9.50 	0.90
转换为
2023-07	-11.40 	BJ_SL_A21
2023-07	-9.50 	BJ_SL_A22
2023-07	1.20 	BJ_SL_A23
2023-08	-11.30 	BJ_SL_A21
2023-08	-9.50 	BJ_SL_A22
2023-08	0.90 	BJ_SL_A23
"""
import tkinter as tk
from tkinter import filedialog
import pandas as pd
# 创建tkinter根窗口(隐藏起来)
root = tk.Tk()
root.withdraw()
# 打开文件选择对话框
file_path = filedialog.askopenfilename()
if file_path:
    # 读取excel文件
    xls = pd.ExcelFile(file_path)
    # 初始化结果列表
    results = []
    # 遍历每个sheet
    for sheet_name in xls.sheet_names:
        # 读取sheet
        df = xls.parse(sheet_name)
        # 定义列名
        cols = df.columns.tolist()
        # 读取第一列 作为时间列
        time_id = cols[0]
        # 删除Date列
        cols.remove(time_id)
        # 遍历每一行
        for index, row in df.iterrows():
            # 遍历每一列
            for col in cols:
                # 如果不是NaN就提取值并组装结果
                # if not pd.isna(row[col]):
                results.append({'time_id': row[time_id], 'fact_value': row[col], 'indicator_id': col})
    # 关闭文件
    xls.close()
else:
    print("没有选择文件")
# 转为DataFrame
new_df = pd.DataFrame(results)
# 输出到Excel
new_df.to_excel('C:/Users/zhang/Desktop/transformed_data.xlsx', index=False)
