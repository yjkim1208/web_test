import os
import pandas as pd
import numpy as np

df_gt = pd.read_csv('신생공업_정답지_230309_v3.csv')
df_pred = pd.read_csv('신생공업_pred_v2.csv')

list_columns_origin = df_gt.columns
df_gt.columns = list(map(lambda x : f"gt_{x}",list(df_gt.columns)))
df_pred.columns = list(map(lambda x : f"pred_{x}", list(df_pred.columns)))

df_merged = pd.concat([df_gt, df_pred], axis=1)
df_merged

for i, j in zip(df_gt.columns, df_pred.columns):
    df_merged[i.replace('gt_', 'result_')] = (df_merged[i]==df_merged[j])
    
list_merged_columns = []
for i in list_columns_origin:
    list_merged_columns.extend([f"gt_{i}", f"pred_{i}", f"result_{i}"])
df_merged = df_merged[list_merged_columns]
df_merged.to_csv('결과.csv')